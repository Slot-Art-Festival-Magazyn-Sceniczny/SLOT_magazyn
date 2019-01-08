import hashlib
import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont, QLinearGradient, QColor, QPolygonF, QBrush, QPen
from PyQt5.QtWidgets import QApplication

import slotbaza
from gui import UI_widget, LoginDialog, Dialog


def hashpassword(password):
    code = hashlib.md5(password.encode('utf-8')).hexdigest()
    return code


class Magazyn(UI_widget):

    def __init__(self):
        super().__init__()
        self.setupUI()
        self.loginstatus = False
        self.usertype = 'user'
        self.logstatus.setText("<FONT COLOR=\'#FF4444\'> Niezalogowany")
        self.rysujobszary()
        self.btn_login.clicked.connect(self.logowanie)
        self.btn_logout.clicked.connect(self.logowanie)
        self.btn_addarea.clicked.connect(self.rysujobszary)
        self.btn_areaedit.clicked.connect(self.wyczyscscene)

    # Moduł logowania do programu
    def logowanie(self):
        sender = self.sender()
        # jeśli wysyłającym jest przycisk ZALOGUJ
        if sender.objectName() == 'btn_login':
            login, haslo, ok = LoginDialog.getloginhaslo(self)
            if ok:
                if slotbaza.isuserexist(login):
                    if slotbaza.loginvalidate(login, hashpassword(haslo))['login']:
                        self.loginstatus = True
                        self.usertype = slotbaza.loginvalidate(login, hashpassword(haslo))['usertpe']
                        self.logstatus.setText("<FONT COLOR=\'#44FF44\'> Zalogowany")
                        Dialog.komunikat('ok', 'Pomyślnie zalogowano do systemu', self)
                    else:
                        Dialog.komunikat('warn', 'Logowanie nieudane! Niepoprawne hasło.', self)
                else:
                    Dialog.komunikat('warn', 'Użytkownik o podanym loginie nie istnieje.', self)
            else:
                pass
        # jeśli wysyłającym jest przycisk WYLOGUJ
        elif sender.objectName() == 'btn_logout':
            if self.loginstatus:
                self.loginstatus = False
                self.usertype = 'user'
                self.logstatus.setText("<FONT COLOR=\'#FF4444\'> Niezalogowany")
                Dialog.komunikat('ok', 'Pomyślnie wylogowano z systemu', self)
            else:
                Dialog.komunikat('warn', 'Nie można się wylogować nie będąc wcześniej zalogowanym', self)

    def rysujobszary(self):
        self.wyczyscscene()
        obszary = slotbaza.getareageometries()
        font = QFont()
        font.setPixelSize(18)
        font.setBold(True)
        for obszar in obszary:
            a = self.scena.addRect(obszar['posx'], obszar['posy'], obszar['sizex'], obszar['sizey'])
            b = self.scena.addText(str(obszar['areaid']))
            b.setDefaultTextColor(Qt.white)
            b.setFont(font)
            br = b.boundingRect()
            b.setPos(obszar['posx'] + obszar['sizex'] / 2 - br.width() / 2,
                     obszar['posy'] + obszar['sizey'] / 2 - br.height() / 2)
            gradient = QLinearGradient(QPoint(obszar['posx'], obszar['posy']),
                                       QPoint(obszar['posx'], obszar['posy'] + obszar['sizey']))
            gradient.setColorAt(0, QColor('#AA0087FF'))
            gradient.setColorAt(1, QColor('#CC0048FF'))
            a.setBrush(gradient)

    def wyczyscscene(self):
        self.scena.clear()
        self.pomieszczeniedosceny()

    def pomieszczeniedosceny(self):
        # self.scena.setBackgroundBrush(Qt.darkGray)
        pomieszczenie_poly = QPolygonF(
            [QPoint(0, 100), QPoint(700, 100), QPoint(700, 0), QPoint(900, 0), QPoint(900, 100), QPoint(1000, 100),
             QPoint(1000, 850), QPoint(880, 850), QPoint(880, 950), QPoint(630, 950), QPoint(630, 850),
             QPoint(370, 850), QPoint(370, 950), QPoint(120, 950), QPoint(120, 850), QPoint(0, 850)])
        pomieszczenie = self.scena.addPolygon(pomieszczenie_poly)
        pomieszczenie.setBrush(QBrush(Qt.white))
        pen = QPen()
        pen.setWidth(4)
        pomieszczenie.setPen(pen)


if __name__ == '__main__':
    app = QApplication([])
    magazyn = Magazyn()
    sys.exit(app.exec_())
