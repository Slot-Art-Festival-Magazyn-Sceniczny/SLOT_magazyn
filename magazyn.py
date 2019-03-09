# -*- coding: utf-8 -*-

# Główny plik programu do obsługi Magazynu Scenicznego.
# W pliku tym przywołane jest główne okno programu, a także wszystkie okna dialogowe.
# Przywołanie to następuje z pliku "clear_gui" (ostatnia linia importu)

import datetime
import hashlib
import sys

from PyQt5.QtCore import Qt, QPoint, QRectF
from PyQt5.QtGui import QFont, QLinearGradient, QColor, QPolygonF, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsItem

import slotbaza
from clear_gui import MainWindow, LoginDialog, Dialog, InputDialog, QuestionDialog, AreaEditDialog, AreaListSmall, \
    AreaList, ItemList

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Poniżej znajduje się część kodu wykonywana przed uruchomieniem głównego okna programu
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Wczytanie pliku z ustawieniami
# Plik ten zawiera podstawowe ustawienia programu w formacie klucz = wartość
# Poniżej znajduje się prosty parser tego pliku, który tworzy zmienną "settings", która zawiera wartości przypisane
# do odpowiednich kluczy.
# Podstawową wartością przechowywaną w pliku settings jest rok (klucz: year).
# Pozwala to w dalszej części programu na poprawne odczytywanie kodów kreskowych
settings = {}
with open('data/settings.cfg') as settingsfile:
    for line in settingsfile:
        try:
            (key, val) = line.split('=')
            key = key.strip()
            val = val.strip()
            settings[key] = val
        except ValueError:
            pass


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Poniżej napisano kilka przydatnych funkcji, które wykorzystywane są w dalszych częściach programu
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Funkcja haszująca hasła (MD5)
# W bazie danych nie chcemy przechowywać haseł, a jedynie ich hasze.
def hashpassword(password):
    code = hashlib.md5(password.encode('utf-8')).hexdigest()
    return code


# Zamiana kodu kreskowego na ID
# W programie bardzo często pojawia się potrzeba zamiany kodu kreskowego np. obszaru na ID obszaru
# dlatego postanowiono stworzyć do tego funkcję. Funkcja przyjmuje wartość kodu kreskowego w postaci stringa
# oraz typ - określający czy funkcja ma zwrócić ID w postaci stringa, czy integera
def barcodetoid(barcode, typ):
    codetxt = barcode[-3:]
    try:
        code = int(codetxt)
        if typ == 'int':
            return code
        elif typ == 'string':
            codetxt2 = str(code)
            return codetxt2
        else:
            pass
    except:
        pass


# Zamiana ID na kod kreskowy
# W programie bardzo często pojawia się potrzeba zamiany ID np. obszaru na wartość kodu kreskowego obszaru
# dlatego postanowiono stworzyć do tego funkcję. Funkcja przyjmuje ID w postaci stringa lub integera
# oraz typ - określający czy jest to obszar, przedmiot, orkiestra, czy user (user aktualnie niewykorzystywany)
def idtobarcode(code, typ):
    year = settings['year']
    if typ == 'area':
        typcode = '10'
    elif typ == 'item':
        typcode = '20'
    elif typ == 'orch':
        typcode = '30'
    elif typ == 'user':
        typcode = '40'
    else:
        pass
    try:
        stringid = str(code)
    except:
        try:
            int(code)
            stringid = code
        except:
            pass
    elementcode = stringid.zfill(3)
    barcode = year + typcode + elementcode
    return barcode
    pass


# Walidacja wprowadzonego kodu kreskowego, zwraca kody błędów z zakresu 0-4
# Żeby zapobiec "głupim zabawom" oraz omyłkowym zeskoanowaniem niepoprawnego kod kreskowego funkcja ta sprawdza, czy
# kod kreskowy ma 9 cyfr, czy pierwsze 4 cyfry zawierają rok, czy kolejne 2 cyfry odpowiadają typowi kodu.
# W przypadku, gdy kod jest właściwy, funkcja zwraca kod 0, kody 1-4 zarezerwowane są dla błędów.
def barcodevalcheck(code, typ):
    year = settings['year']
    if typ == 'area':
        typcode = '10'
    elif typ == 'item':
        typcode = '20'
    elif typ == 'orch':
        typcode = '30'
    elif typ == 'user':
        typcode = '40'
    else:
        pass
    if code == '':
        status = 1
        statustxt = 'Nie wprowadzono żadnego kodu!'
    else:
        if len(code) == 9:
            if code[0:4] == year:
                if code[4:6] == typcode:
                    status = 0
                    statustxt = 'Wprowadzono właściwy kod'
                else:
                    status = 4
                    statustxt = 'Wprowadzono kod niewłaściwego typu!'
            else:
                status = 3
                statustxt = "Wprowadzono kod z innego roku!"
        else:
            status = 2
            statustxt = 'Wprowadzono niewłaściwy kod!'
    return (status, statustxt)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Główna część programu
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Klasa opisująca główne okno programu
class Magazyn(MainWindow):

    # Konstruktor klasy
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.rysujobszary()

        # Domyślnie po włączeniu programu nikt nie jest zalogowany
        self.loginstatus = False
        self.username = ''
        self.usertype = 'user'
        self.logstatus.setText("<FONT COLOR=\'#FF4444\'> Niezalogowany")

        # Połączenie przycisków z odpowiednimi funkcjami
        self.connectbuttons()

    # Połączenie przycisków z odpowiednimi funkcjami
    def connectbuttons(self):
        self.btn_login.clicked.connect(self.logowanie)
        self.btn_logout.clicked.connect(self.logowanie)
        self.btn_addarea.clicked.connect(self.rysujobszary)
        self.btn_listofareas.clicked.connect(self.listofareas)
        self.btn_editarea.clicked.connect(self.editarea)
        self.btn_finditem.clicked.connect(self.finditem)
        self.btn_lookinside.clicked.connect(self.lookinside)
        self.btn_comein.clicked.connect(self.comein)
        self.btn_comeout.clicked.connect(self.comeout)
        self.btn_exit.clicked.connect(self.close)

    # Moduł logowania do programu
    def logowanie(self):
        sender = self.sender()
        # jeśli wysyłającym jest przycisk ZALOGUJ
        if sender.objectName() == 'btn_login':
            self.blurwindow()
            login, haslo, ok = LoginDialog.getloginhaslo(self)
            if ok:
                if slotbaza.isuserexist(login):
                    if slotbaza.loginvalidate(login, hashpassword(haslo))['login']:
                        self.loginstatus = True
                        self.usertype = slotbaza.loginvalidate(login, hashpassword(haslo))['usertype']
                        self.logstatus.setText("<FONT COLOR=\'#44FF44\'> Zalogowany jako " + login)
                        Dialog.komunikat('ok', 'Pomyślnie zalogowano do systemu', self)
                        self.unblurwindow()
                    else:
                        Dialog.komunikat('warn', 'Logowanie nieudane! Niepoprawne hasło.', self)
                        self.unblurwindow()
                else:
                    Dialog.komunikat('warn', 'Użytkownik o podanym loginie nie istnieje.', self)
                    self.unblurwindow()
            else:
                self.unblurwindow()
        # jeśli wysyłającym jest przycisk WYLOGUJ
        elif sender.objectName() == 'btn_logout':
            if self.loginstatus:
                self.loginstatus = False
                self.usertype = 'user'
                self.logstatus.setText("<FONT COLOR=\'#FF4444\'> Niezalogowany")
                self.blurwindow()
                Dialog.komunikat('ok', 'Pomyślnie wylogowano z systemu', self)
                self.unblurwindow()
            else:
                self.blurwindow()
                Dialog.komunikat('warn', 'Nie można się wylogować nie będąc wcześniej zalogowanym', self)
                self.unblurwindow()

    # Wyszukiwanie przedmiotów
    def finditem(self):
        self.blurwindow()
        itembarcode, itemok = InputDialog.komunikat('barcode', 'Wczytaj kod przedmiotu:', self)
        if itemok:
            itemstatus, itemstatustxt = barcodevalcheck(itembarcode, 'item')
            if itemstatus == 0:
                itemid = barcodetoid(itembarcode, 'int')
                if slotbaza.isitemexist(itemid):
                    przedmiot = slotbaza.loaditem(itemid)
                    if przedmiot['itemstate']:
                        stan = 'przyjęty'
                    else:
                        stan = 'wydany'
                    areaid = przedmiot['areaass']
                    area = slotbaza.loadarea(areaid)
                    Dialog.komunikat('ok', 'Znaleziono przedmiot!\n' +
                                     '\nID przedmiotu: ' + str(przedmiot['itemid']) +
                                     '\nNazwa przedmiotu: ' + przedmiot['itemname'] +
                                     '\n' +
                                     '\nID obszaru: ' + str(areaid) +
                                     '\nNazwa obszaru: ' + area['areaname'] +
                                     '\n' +
                                     '\nStan: ' + stan)
                    self.unblurwindow()
                else:
                    Dialog.komunikat('error', 'Wczytany przedmiot nie znajduje się w bazie. '
                                              'Jeśli nie wiesz dlaczego, skontaktuj się z szefem ekipy', self)
                    self.unblurwindow()
            else:
                Dialog.komunikat('warn', itemstatustxt, self)
                self.unblurwindow()
        else:
            self.unblurwindow()
        pass

    # Moduł zaglądania do obszarów
    def lookinside(self):
        obszary = slotbaza.loadallareas()
        self.blurwindow()
        areaid, ok = AreaListSmall.showlist(obszary, self)
        if ok:
            if areaid == 0:
                self.unblurwindow()
            else:
                if slotbaza.isareaexist(areaid):
                    self.itemlist(areaid)
                else:
                    Dialog.komunikat('warn', 'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                             'do niego przedmioty.', self)
                    self.unblurwindow()
        else:
            self.unblurwindow()

    # Wyświetlenie listy przedmiotów w obszarze od zadanym ID
    def itemlist(self, areaid):
        model = slotbaza.getqitemmodel(areaid)
        ItemList.showtable(model)
        self.unblurwindow()

    # Obsługa przyjmowania przedmiotów
    def comein(self):
        self.blurwindow()
        areabarcode, areaok = InputDialog.komunikat('barcode', 'Wczytaj kod obszaru:', self)
        if areaok:
            areastatus, areastatustxt = barcodevalcheck(areabarcode, 'area')
            if areastatus == 0:
                areaid = barcodetoid(areabarcode, 'int')
                if slotbaza.isareaexist(areaid):
                    kolejnyprzedmiot = True
                    while kolejnyprzedmiot:
                        kolejnyprzedmiot = False
                        itembarcode, itemok = InputDialog.komunikat('barcode', 'Wczytaj kod przedmiotu:', self)
                        if itemok:
                            itemstatus, itemstatustxt = barcodevalcheck(itembarcode, 'item')
                            if itemstatus == 0:
                                itemid = barcodetoid(itembarcode, 'int')
                                if slotbaza.isitemexist(itemid):
                                    przedmiot = slotbaza.loaditem(itemid)
                                    if przedmiot['itemstate']:
                                        Dialog.komunikat('error', 'Ten przedmiot jest już przyjęty na stan magazynu! '
                                                                  'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!', self)
                                        self.unblurwindow()
                                    else:
                                        istniejacyprzedmiotok = QuestionDialog.pytanie('Ten przedmiot znajduje się '
                                                                                       'w bazie:\nNazwa przedmiotu: '
                                                                                       + przedmiot['itemname']
                                                                                       + '\nStan: Wydany\nUwagi: '
                                                                                       + przedmiot['itemcomments']
                                                                                       + '\n\nCzy chcesz przyjąć '
                                                                                         'przedmiot?', self)
                                        if istniejacyprzedmiotok:
                                            przedmiot['itemstate'] = True
                                            przedmiot['dateoflastincome'] = datetime.datetime.now()
                                            przedmiot['useroflastincome'] = self.username
                                            slotbaza.saveitem(przedmiot)
                                            Dialog.komunikat('ok', 'Przedmiot został przyjęty na stan magazynu', self)
                                            kolejnyprzedmiot = QuestionDialog.pytanie('Czy chcesz przyjąć '
                                                                                      'kolejny przedmiot do obszaru'
                                                                                      ' ' + str(areaid) + '?', self)
                                        else:
                                            Dialog.komunikat('warn', 'Przerwano proces przyjmowania przedmiotu.'
                                                                     '\nPrzedmiot nie został przyjęty', self)
                                            self.unblurwindow()
                                else:
                                    nowyprzedmiotok = QuestionDialog.pytanie(
                                        'Wprowadzony przedmiot nie znajduje się na żadnym obszarze. '
                                        'Czy chcesz go dodać do obszaru ' + str(
                                            areaid) + '?', self)
                                    if nowyprzedmiotok:
                                        nazwaprzedmiotu, nazwaprzedmiotuok = InputDialog.komunikat('txt',
                                                                                                   'Podaj nazwę '
                                                                                                   'nowego przedmiotu:',
                                                                                                   self)
                                        if nazwaprzedmiotuok:
                                            slotbaza.createitem(itemid, idtobarcode(itemid, 'item'), nazwaprzedmiotu,
                                                                areaid)
                                            przedmiot = slotbaza.loaditem(itemid)
                                            przedmiot['itemstate'] = True;
                                            przedmiot['dateoffirstincome'] = datetime.datetime.now()
                                            przedmiot['useroffirstincome'] = self.username
                                            przedmiot['useroflastincome'] = self.username
                                            przedmiot['dateoflastincome'] = datetime.datetime.now()
                                            slotbaza.saveitem(przedmiot)
                                            Dialog.komunikat('ok',
                                                             'Poprawnie dodano przedmiot.'
                                                             '\nPredmiot został przyjęty na stan magazynu.',
                                                             self)
                                            kolejnyprzedmiot = QuestionDialog.pytanie(
                                                'Czy chcesz przyjąć kolejny przedmiot do obszaru ' + str(areaid) + '?',
                                                self)
                                        else:
                                            Dialog.komunikat('warn',
                                                             'Przerwano proces dodawania przedmiotu. '
                                                             'Przedmiot nie został dodany.',
                                                             self)
                                            self.unblurwindow()
                                        pass
                                    else:
                                        Dialog.komunikat('error',
                                                         'W takim razie albo zeskanowałeś zły kod, '
                                                         'albo coś się popsuło...\nWezwij szefa ekipy.',
                                                         self)
                                        self.unblurwindow()
                            else:
                                Dialog.komunikat('warn', itemstatustxt, self)
                                self.unblurwindow()
                        else:
                            pass
                    self.unblurwindow()
                else:
                    Dialog.komunikat('warn', 'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                             'do niego przedmioty.', self)
                    self.unblurwindow()
            else:
                Dialog.komunikat('warn', areastatustxt, self)
                self.unblurwindow()
        else:
            self.unblurwindow()

    # Obsługa wydawania przedmiotów
    def comeout(self):
        self.blurwindow()
        areabarcode, areaok = InputDialog.komunikat('barcode', 'Wczytaj kod obszaru:', self)
        if areaok:
            areastatus, areastatustxt = barcodevalcheck(areabarcode, 'area')
            if areastatus == 0:
                areaid = barcodetoid(areabarcode, 'int')
                if slotbaza.isareaexist(areaid):
                    kolejnyprzedmiot = True
                    while kolejnyprzedmiot:
                        kolejnyprzedmiot = False
                        itembarcode, itemok = InputDialog.komunikat('barcode', 'Wczytaj kod przedmiotu:', self)
                        if itemok:
                            itemstatus, itemstatustxt = barcodevalcheck(itembarcode, 'item')
                            if itemstatus == 0:
                                itemid = barcodetoid(itembarcode, 'int')
                                if slotbaza.isitemexist(itemid):
                                    przedmiot = slotbaza.loaditem(itemid)
                                    if przedmiot['itemstate']:
                                        istniejacyprzedmiotok = QuestionDialog.pytanie(
                                            'Ten przedmiot znajduje się w bazie:\nNazwa przedmiotu: ' + przedmiot[
                                                'itemname'] + '\nStan: Przyjęty\nUwagi: ' + przedmiot[
                                                'itemcomments'] + '\n\nCzy chcesz wydać przedmiot?', self)
                                        if istniejacyprzedmiotok:
                                            przedmiot['itemstate'] = False
                                            przedmiot['dateoflastoutcome'] = datetime.datetime.now()
                                            przedmiot['useroflastoutcome'] = self.username
                                            slotbaza.saveitem(przedmiot)
                                            Dialog.komunikat('ok', 'Przedmiot został wydany z magazynu', self)
                                            kolejnyprzedmiot = QuestionDialog.pytanie(
                                                'Czy chcesz wydać kolejny przedmiot z obszaru ' + str(areaid) + '?',
                                                self)
                                        else:
                                            Dialog.komunikat('warn',
                                                             'Przerwano proces wydawania przedmiotu.'
                                                             '\nPrzedmiot nie został wydany',
                                                             self)
                                            self.unblurwindow()
                                    else:
                                        Dialog.komunikat('error',
                                                         'Ten przedmiot jest już wydany z magazynu! '
                                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                         self)
                                        self.unblurwindow()
                                else:
                                    Dialog.komunikat('error',
                                                     'Próbujesz wydać przedmiot, który nie znajduje się w bazie! '
                                                     'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                     self)
                                    self.unblurwindow()
                            else:
                                Dialog.komunikat('warn', itemstatustxt, self)
                                self.unblurwindow()
                        else:
                            self.unblurwindow()
                    self.unblurwindow()
                else:
                    Dialog.komunikat('warn', 'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                             'do niego przedmioty.', self)
                    self.unblurwindow()
            else:
                Dialog.komunikat('warn', areastatustxt, self)
                self.unblurwindow()
        else:
            self.unblurwindow()

    # Wyświetlenie listy wszystkich obszarów
    def listofareas(self):
        self.blurwindow()
        model = slotbaza.getqareamodel()
        AreaList.showtable(model)
        self.unblurwindow()

    # Edycja wybranego na liście obszaru
    def editarea(self):
        obszary = slotbaza.loadallareas()
        self.blurwindow()
        areaid, ok = AreaListSmall.showlist(obszary, self)
        if ok:
            if areaid == 0:
                self.unblurwindow()
            else:
                if slotbaza.isareaexist(areaid):
                    obszar = slotbaza.loadarea(areaid)
                    nowyobszar, ok = AreaEditDialog.editarea(obszar, self)
                    if ok:
                        slotbaza.savearea(nowyobszar)
                        Dialog.komunikat('ok', 'Poprawnie zmodyfikowano obszar.', self)
                        self.unblurwindow()
                    else:
                        Dialog.komunikat('warn', 'Przerwano proces edycji obszaru! Zmiany nie zostały zapisane.', self)
                        self.unblurwindow()
                else:
                    Dialog.komunikat('warn', 'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                             'do niego przedmioty.', self)
                    self.unblurwindow()
        else:
            self.unblurwindow()

    # Funkcja rysująca obszary, po wcześniejszym wyczyszczeniu sceny
    def rysujobszary(self):
        self.wyczyscscene()
        obszary = slotbaza.getareageometries()
        font = QFont()
        font.setPixelSize(18)
        font.setBold(True)
        for obszar in obszary:
            prosto = QGraphicsRectItem(QRectF(obszar['posx'], obszar['posy'], obszar['sizex'], obszar['sizey']))
            prosto.setFlag(QGraphicsItem.ItemIsMovable, True)
            prostokat = self.scena.addItem(prosto)
            etykieta = self.scena.addText(str(obszar['areaid']))
            etykieta.setDefaultTextColor(Qt.white)
            etykieta.setFont(font)
            br = etykieta.boundingRect()
            etykieta.setPos(obszar['posx'] + obszar['sizex'] / 2 - br.width() / 2,
                            obszar['posy'] + obszar['sizey'] / 2 - br.height() / 2)
            gradient = QLinearGradient(QPoint(obszar['posx'], obszar['posy']),
                                       QPoint(obszar['posx'], obszar['posy'] + obszar['sizey']))
            gradient.setColorAt(0, QColor('#220087FF'))
            gradient.setColorAt(1, QColor('#440048FF'))
            prosto.setBrush(gradient)

    # Funkcja czyszcząca scenę i rysująca pomieszczenie
    def wyczyscscene(self):
        self.scena.clear()
        self.pomieszczeniedosceny()

    # Funkcja rysująca pomieszczenia
    def pomieszczeniedosceny(self):
        # self.scena.setBackgroundBrush(Qt.darkGray)
        pomieszczenie_poly = QPolygonF(
            [QPoint(0, 100), QPoint(700, 100), QPoint(700, 0), QPoint(900, 0), QPoint(900, 100), QPoint(1000, 100),
             QPoint(1000, 850), QPoint(880, 850), QPoint(880, 950), QPoint(630, 950), QPoint(630, 850),
             QPoint(370, 850), QPoint(370, 950), QPoint(120, 950), QPoint(120, 850), QPoint(0, 850)])
        pomieszczenie = self.scena.addPolygon(pomieszczenie_poly)
        pomieszczenie.setBrush(QBrush(QColor('#22000000')))
        pen = QPen()
        pen.setWidth(4)
        pomieszczenie.setPen(pen)
        self.viewer.fitInView(self.scena.sceneRect(), Qt.KeepAspectRatio)
        self.viewer.scale(0.9, 0.9)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Wykonywalna część programu
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Uruchomienie programu, stoworzenie instancji klasy Magazyn
if __name__ == '__main__':
    app = QApplication([])
    magazyn = Magazyn()
    sys.exit(app.exec_())
