import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QFont, QLinearGradient, QColor, QPolygonF, QBrush, QPen
from PyQt5.QtCore import Qt, QPoint
from gui import UI_widget
import slotbaza

class Magazyn(UI_widget):

    def __init__(self):
        super().__init__()
        self.setupUI()
        self.loginstatus = False
        self.logstatus.setText("<FONT COLOR=\'#FF4444\'> Niezalogowany")
        self.rysujobszary()
        self.btn_login.clicked.connect(self.logowanie)
        self.btn_logout.clicked.connect(self.logowanie)
        self.btn_addarea.clicked.connect(self.rysujobszary)
        self.btn_areaedit.clicked.connect(self.wyczyscscene)


    def logowanie(self):
        sender=self.sender()
        if sender.objectName()=='btn_login':
            self.loginstatus = True
            self.logstatus.setText("<FONT COLOR=\'#44FF44\'> Zalogowany")
        elif sender.objectName()=='btn_logout':
            self.loginstatus = False
            self.logstatus.setText("<FONT COLOR=\'#FF4444\'> Niezalogowany")

    def rysujobszary(self):
        self.wyczyscscene()
        obszary = slotbaza.getareageometries()
        font = QFont()
        font.setPixelSize(18)
        font.setBold(True)
        for obszar in obszary:
            a=self.scena.addRect(obszar['posx'],obszar['posy'],obszar['sizex'],obszar['sizey'])
            b=self.scena.addText(str(obszar['areaid']))
            b.setDefaultTextColor(Qt.white)
            b.setFont(font)
            br = b.boundingRect()
            b.setPos(obszar['posx']+obszar['sizex']/2-br.width()/2,obszar['posy']+obszar['sizey']/2-br.height()/2)
            gradient = QLinearGradient(QPoint(obszar['posx'], obszar['posy']), QPoint(obszar['posx'], obszar['posy']+obszar['sizey']))
            gradient.setColorAt(0, QColor('#AA0087FF'))
            gradient.setColorAt(1, QColor('#CC0048FF'))
            a.setBrush(gradient)

    def wyczyscscene(self):
        self.scena.clear()
        self.pomieszczeniedosceny()

    def pomieszczeniedosceny(self):
        # self.scena.setBackgroundBrush(Qt.darkGray)
        pomieszczenie_poly=QPolygonF([QPoint(0,100),QPoint(700,100),QPoint(700,0),QPoint(900,0),QPoint(900,100),QPoint(1000,100), QPoint(1000,850), QPoint(880,850),QPoint(880,950),QPoint(630,950),QPoint(630,850),QPoint(370,850),QPoint(370,950),QPoint(120,950),QPoint(120,850),QPoint(0,850)])
        pomieszczenie=self.scena.addPolygon(pomieszczenie_poly)
        pomieszczenie.setBrush(QBrush(Qt.white))
        pen=QPen()
        pen.setWidth(4)
        pomieszczenie.setPen(pen)

if __name__ == '__main__':
    app = QApplication([])
    magazyn = Magazyn()
    sys.exit(app.exec_())