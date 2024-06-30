# -*- coding: utf-8 -*-

# Główny plik programu do obsługi Magazynu Scenicznego.
# W pliku tym przywołane jest główne okno programu, a także wszystkie okna dialogowe.
# Przywołanie to następuje z pliku "clear_gui" (ostatnia linia importu)

import datetime
import hashlib
import sys

from PyQt5.QtCore import Qt, QPoint, QRectF
from PyQt5.QtGui import QFont, QLinearGradient, QColor, QPolygonF, QBrush, QPen, QTransform
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsItem, QGraphicsItemGroup, QGraphicsTextItem

import logbaza
import slotbaza
from clear_gui import MainWindow, LoginDialog, Dialog, InputDialog, QuestionDialog, AreaEditDialog, AreaListSmall, \
    AreaList, ItemList, OrchList, OrchEditDialog, CreateUserDialog

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
        codemin = int(settings['areamin'])
        codemax = int(settings['areamax'])
    elif typ == 'item':
        typcode = '20'
        codemin = int(settings['itemmin'])
        codemax = int(settings['itemmax'])
    elif typ == 'orch':
        typcode = '30'
        codemin = int(settings['orchmin'])
        codemax = int(settings['orchmax'])
    elif typ == 'user':
        typcode = '40'
        codemin = 1
        codemax = 100
    else:
        pass
    if code is None or code == '':
        status = 1
        statustxt = 'Nie wprowadzono żadnego kodu!'
    else:
        if len(code) == 9:
            if code[0:4] == year:
                if code[4:6] == typcode:
                    try:
                        int(code[6:9])
                        if int(code[6:9]) < codemin or int(code[6:9]) > codemax:
                            status = 5
                            statustxt = 'Wprowadzono kod spoza zakresu'
                        else:
                            status = 0
                            statustxt = 'Wprowadzono właściwy kod'
                    except:
                        status = 2
                        statustxt = 'Wprowadzono niewłaściwy kod!'
                else:
                    status = 4
                    statustxt = 'Wprowadzono kod niewłaściwego typu!'
            else:
                status = 3
                statustxt = "Wprowadzono kod z innego roku!"
        else:
            status = 2
            statustxt = 'Wprowadzono niewłaściwy kod!'
    return status, statustxt


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
        self.config = {}
        self.loadconfig()
        self.setupUI()
        self.applyrotation(int(self.config['viewangle']))
        self.selected = 0
        self.rysujobszary()
        # Domyślnie po włączeniu programu nikt nie jest zalogowany
        self.loginbypass = False  # Jeśli True to do obsługi programu niewymagane jest logowanie
        self.loginstatus = False
        self.username = ''
        self.usertype = 'user'
        self.logstatus.setText("<FONT COLOR=\'#FF4444\'> Niezalogowany")
        self.updateorchcounters()

        # Połączenie przycisków z odpowiednimi funkcjami
        self.connectbuttons()

    def loadconfig(self):
        with open('data/config.cfg') as configfile:
            for line in configfile:
                try:
                    (key, val) = line.split('=')
                    key = key.strip()
                    val = val.strip()
                    self.config[key] = val
                except ValueError:
                    pass

    def saveconfig(self):
        with open('data/config.cfg', 'w') as configfile:
            for key, val in self.config.items():
                configfile.write(f"{key} = {val}\n")

    # Połączenie przycisków z odpowiednimi funkcjami
    def connectbuttons(self):
        self.btn_login.clicked.connect(self.logowanie)
        self.btn_logout.clicked.connect(self.logowanie)
        self.btn_addarea.clicked.connect(self.addarea)
        self.btn_listofareas.clicked.connect(self.listofareas)
        self.btn_editarea.clicked.connect(self.editarea)
        self.btn_finditem.clicked.connect(self.finditem)
        self.btn_lookinside.clicked.connect(self.lookinside)
        self.btn_comein.clicked.connect(self.comein)
        self.btn_comeout.clicked.connect(self.comeout)
        self.btn_orchestra.clicked.connect(self.orchestra)
        self.btn_exit.clicked.connect(self.close)
        # self.btn_exit2.clicked.connect(self.close)
        self.orchestramodule.btn_orchtable.clicked.connect(self.orchtable)
        self.orchestramodule.btn_orchfirstcomein.clicked.connect(self.orchfirstcomein)
        self.orchestramodule.btn_orchcomein.clicked.connect(self.orchcomein)
        self.orchestramodule.btn_orchcomeout.clicked.connect(self.orchcomeout)
        self.btn_fillmode.clicked.connect(self.changefillmode)
        self.btn_labelmode.clicked.connect(self.changelabelmode)
        self.btn_rotateview.clicked.connect(self.rotateview)
        self.btn_sound_ok.clicked.connect(self.changesoundconfig)
        self.btn_sound_warn.clicked.connect(self.changesoundconfig)
        self.btn_sound_error.clicked.connect(self.changesoundconfig)
        self.btn_sound_info.clicked.connect(self.changesoundconfig)
        self.btn_sound_other.clicked.connect(self.changesoundconfig)
        self.btn_sound_txt.clicked.connect(self.changesoundconfig)
        self.btn_sound_barcode.clicked.connect(self.changesoundconfig)
        self.btn_adminpanel.clicked.connect(self.adminpanel)
        self.viewer.rectChanged.connect(self.areadrawend)
        self.adminmodule.btn_adduser.clicked.connect(self.createuser)
        self.adminmodule.btn_changeuserpassword.clicked.connect(self.changepassword)

    def userlist(self):
        print('user list')

    def createuser(self):
        self.blurwindow()
        login, haslo, ok = CreateUserDialog.getloginhaslo(self)
        if not ok:
            self.unblurwindow()
            return
        if slotbaza.isuserexist(login):
            Dialog.komunikat('warn', 'Użytkownik o podanej nazwie już istnieje!', self, audio=45)
            self.unblurwindow()
            return
        slotbaza.createuser('user', login, hashpassword(haslo))
        Dialog.komunikat('ok', 'Pomyślnie dodano użytkownika!', self, audio=14)
        self.unblurwindow()

    def changepassword(self):
        self.blurwindow()
        login, haslo, ok = CreateUserDialog.getloginhaslo(self)
        if not ok:
            self.unblurwindow()
            return
        if not slotbaza.isuserexist(login):
            Dialog.komunikat('warn', 'Użytkownik o podanej nazwie nie istnieje!', self, audio=46)
            self.unblurwindow()
            return
        uzytkownik = slotbaza.loaduser(login)
        uzytkownik['password'] = hashpassword(haslo)
        slotbaza.saveuser(uzytkownik)
        Dialog.komunikat('ok', 'Pomyślnie zmieniono haslo!', self, audio=17)
        self.unblurwindow()

    def adminpanel(self):
        if self.adminmodule.isVisible():
            self.adminmodule.toggleshow()
        else:
            self.blurwindow()
            login, haslo, ok = LoginDialog.getloginhaslo(self)
            if not ok:
                self.unblurwindow()
                return
            if not slotbaza.isuserexist(login):
                logbaza.userchange(self.username, 'Admin Login Fail', login)
                Dialog.komunikat('warn', 'Logowanie Administratora nieudane', self, audio=26)
                self.unblurwindow()
                return
            if not login == 'admin':
                logbaza.userchange(self.username, 'Admin Login Fail', login)
                Dialog.komunikat('warn', 'Logowanie Administratora nieudane', self, audio=26)
                self.unblurwindow()
                return
            if not slotbaza.loginvalidate(login, hashpassword(haslo))['login']:
                logbaza.userchange(self.username, 'Admin Login Fail', login)
                Dialog.komunikat('warn', 'Logowanie Administratora nieudane', self, audio=26)
                self.unblurwindow()
                return
            logbaza.userchange(self.username, 'Admin Login Succes')
            Dialog.komunikat('ok', 'Pomyslnie zalogowano', self, audio=13)
            self.unblurwindow()
            self.adminmodule.toggleshow()

    # Moduł logowania do programu
    def logowanie(self):
        sender = self.sender()
        # jeśli wysyłającym jest przycisk ZALOGUJ
        if sender.objectName() == 'btn_login':
            if self.loginstatus:
                self.blurwindow()
                Dialog.komunikat('warn', 'Nie można się zalogować będąc zalogowanym', self, audio=31)
                self.unblurwindow()
            else:
                self.blurwindow()
                login, haslo, ok = LoginDialog.getloginhaslo(self)
                if ok:
                    if slotbaza.isuserexist(login):
                        if slotbaza.loginvalidate(login, hashpassword(haslo))['login']:
                            self.loginstatus = True
                            self.username = login
                            self.usertype = slotbaza.loginvalidate(login, hashpassword(haslo))['usertype']
                            self.logstatus.setText("<FONT COLOR=\'#44FF44\'> Zalogowany jako " + login)
                            logbaza.userchange(login, 'Log In')
                            Dialog.komunikat('ok', 'Pomyślnie zalogowano do systemu', self, audio=16)
                            self.unblurwindow()
                        else:
                            logbaza.userchange(login, 'Failed Log In (wrong password)')
                            Dialog.komunikat('warn', 'Logowanie nieudane! Niepoprawne hasło.', self, audio=27)
                            self.unblurwindow()
                    else:
                        logbaza.userchange(login, 'Failed Log In (wrong username)')
                        Dialog.komunikat('warn', 'Użytkownik o podanym loginie nie istnieje.', self, audio=46)
                        self.unblurwindow()
                else:
                    self.unblurwindow()
        # jeśli wysyłającym jest przycisk WYLOGUJ
        elif sender.objectName() == 'btn_logout':
            if self.loginstatus:
                login = self.username
                self.loginstatus = False
                self.username = ''
                self.usertype = 'user'
                self.logstatus.setText("<FONT COLOR=\'#FF4444\'> Niezalogowany")
                self.blurwindow()
                logbaza.userchange(login, 'Log Out')
                Dialog.komunikat('ok', 'Pomyślnie wylogowano z systemu', self, audio=15)
                self.unblurwindow()
            else:
                self.blurwindow()
                Dialog.komunikat('warn', 'Nie można się wylogować nie będąc wcześniej zalogowanym', self, audio=30)
                self.unblurwindow()

    # Wyświetlenie listy wszystkich obszarów
    def listofareas(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.blurwindow()
            model = slotbaza.getqareamodel()
            AreaList.showtable(model)
            self.unblurwindow()

    # Dodanie nowego obszaru
    def addarea(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.blurwindow()
            areaid, areaok = InputDialog.komunikat('txt', 'Podaj numer obszaru:', self, audio=59)
            if areaok:
                areabarcode = idtobarcode(areaid, 'area')
                areastatus, areastatustxt = barcodevalcheck(areabarcode, 'area')
                if areastatus == 0:
                    if slotbaza.isareaexist(areaid):
                        logbaza.areachange(self.username, 'Override Trial', areaid)
                        Dialog.komunikat('warn', 'Obszar o wprowadzonym numerze już istnieje!', self, audio=35)
                        self.unblurwindow()
                    else:
                        areaname, nameok = InputDialog.komunikat('txt', 'Podaj nazwę nowego obszaru:', self, audio=57)
                        if nameok:
                            Dialog.komunikat('info', 'Narysuj obszar na mapie magazynu', self, audio=12)
                            # Zapisanie danych podanych przez użytkownika - rozwiązane brzydko, ale lepiej nie umiem
                            self.newareaname = areaname
                            self.newareaid = areaid
                            self.newareabarcode = areabarcode

                            self.unblurwindow()

                            # przełączenie viewera w tryb rysowania. Po narysuwoaniu wywołana jest funkcja areadrawend
                            self.viewer.addareamode()
                        else:
                            self.unblurwindow()
                else:
                    Dialog.komunikat('warn', areastatustxt, self)
                    self.unblurwindow()
            else:
                self.unblurwindow()

    # Zakończenie rysowania obszaru, okno dodawania obszaru
    def areadrawend(self, pos):
        self.viewer.normalmode()  # przełączenie viewera w normalny tryb pracy
        coords = self.viewer.mapToScene(pos)  # viewer zwraca coordy globalne, trzeba je zmapować na scene

        # sprawdzenie czy użytkownik narysował prostokąt
        if len(coords) == 0:
            self.viewer.rubberBand.hide()
            self.blurwindow()
            Dialog.komunikat('warn', 'Narysowano niepoprawny prostokąt! Obszar nie został utworzony', self, audio=29)
            self.unblurwindow()
        else:
            # Przeliczenie współrzędnych punktów na format posx,posy,sizex,sizey. Mozlwa kontrola zaookrąglania
            rect = coords.boundingRect()
            roundfactor = 5
            posx = roundfactor * round(rect.x() / roundfactor)
            posy = roundfactor * round(rect.y() / roundfactor)
            sizex = roundfactor * round(rect.width() / roundfactor)
            sizey = roundfactor * round(rect.height() / roundfactor)

            # Stowrzenie obszaru w bazie danych
            slotbaza.createarea(self.newareaid, self.newareabarcode, self.newareaname, posx, posy, sizex, sizey,
                                self.username)

            # Narysowanie obszaru na mapie
            self.viewer.rubberBand.hide()
            self.rysujobszary()
            self.blurwindow()

            # Wczytanie obszaru do edycji - w celu uzupełnienia szczegółowych danych
            obszar = slotbaza.loadarea(self.newareaid)
            logbaza.areachange(self.username, 'Create', self.newareaid, '', obszar)
            nowyobszar, ok = AreaEditDialog.editarea(obszar, self)
            if ok:
                slotbaza.savearea(nowyobszar)
                logbaza.areachange(self.username, 'Create edit', self.newareaid, obszar, nowyobszar)
                Dialog.komunikat('ok', 'Poprawnie stworzono obszar.', self, audio=20)
                self.unblurwindow()
            else:
                Dialog.komunikat('warn', 'Przerwano proces edycji obszaru! '
                                         'Obszar został utworzony, ale zmiany nie zostały zapisane.', self, audio=37)
                self.unblurwindow()

    # Edycja wybranego na liście obszaru
    def editarea(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            obszary = slotbaza.loadallareas()
            self.blurwindow()
            areaid, ok = AreaListSmall.showlist(obszary, self)
            if ok:
                if areaid == 0:
                    self.unblurwindow()
                else:
                    if slotbaza.isareaexist(areaid):
                        obszar = slotbaza.loadarea(areaid)
                        self.selected = areaid
                        self.rysujobszary()
                        self.selected = 0
                        nowyobszar, ok = AreaEditDialog.editarea(obszar, self)
                        self.rysujobszary()
                        if ok:
                            logbaza.areachange(self.username, 'Edit', areaid, obszar, nowyobszar)
                            slotbaza.savearea(nowyobszar)
                            Dialog.komunikat('ok', 'Poprawnie zmodyfikowano obszar.', self, audio=22)
                            self.unblurwindow()
                        else:
                            Dialog.komunikat('warn', 'Przerwano proces edycji obszaru! Zmiany nie zostały zapisane.',
                                             self, audio=38)
                            self.unblurwindow()
                    else:
                        Dialog.komunikat('warn',
                                         'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                         'do niego przedmioty.', self, audio=49)
                        self.unblurwindow()
            else:
                self.unblurwindow()

    # Wyszukiwanie przedmiotów
    def finditem(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.blurwindow()
            itembarcode, itemok = InputDialog.komunikat('barcode', 'Wczytaj kod przedmiotu:', self, audio=54)
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
                        self.selected = area['areaid']
                        self.rysujobszary()
                        self.selected = 0
                        Dialog.komunikat('ok', 'Znaleziono przedmiot!\n' +
                                         '\nID przedmiotu: ' + str(przedmiot['itemid']) +
                                         '\nNazwa przedmiotu: ' + przedmiot['itemname'] +
                                         '\n' +
                                         '\nID obszaru: ' + str(areaid) +
                                         '\nNazwa obszaru: ' + area['areaname'] +
                                         '\n' +
                                         '\nStan: ' + stan, audio=25)
                        self.rysujobszary()
                        self.unblurwindow()
                    else:
                        Dialog.komunikat('error', 'Wczytany przedmiot nie znajduje się w bazie. '
                                                  'Jeśli nie wiesz dlaczego, skontaktuj się z szefem ekipy', self,
                                         audio=11)
                        self.unblurwindow()
                else:
                    Dialog.komunikat('warn', itemstatustxt, self)
                    self.unblurwindow()
            else:
                self.unblurwindow()
            pass

    # Moduł zaglądania do obszarów
    def lookinside(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            obszary = slotbaza.loadallareas()
            self.blurwindow()
            areaid, ok = AreaListSmall.showlist(obszary, self)
            if ok:
                if areaid == 0:
                    self.unblurwindow()
                else:
                    if slotbaza.isareaexist(areaid):
                        self.selected = areaid
                        self.rysujobszary()
                        self.selected = 0
                        self.itemlist(areaid)
                        self.rysujobszary()
                    else:
                        Dialog.komunikat('warn',
                                         'Wskazany obszar nie istnieje! \n'
                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy', self, audio=48)
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
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.blurwindow()
            areabarcode, areaok = InputDialog.komunikat('barcode', 'Wczytaj kod obszaru:', self, audio=53)
            if areaok:
                areastatus, areastatustxt = barcodevalcheck(areabarcode, 'area')
                if areastatus == 0:
                    areaid = barcodetoid(areabarcode, 'int')
                    if slotbaza.isareaexist(areaid):
                        kolejnyprzedmiot = True
                        self.selected = areaid
                        self.rysujobszary()
                        self.selected = 0
                        while kolejnyprzedmiot:
                            kolejnyprzedmiot = False
                            itembarcode, itemok = InputDialog.komunikat('barcode', 'Wczytaj kod przedmiotu:', self,
                                                                        audio=54)
                            if itemok:
                                itemstatus, itemstatustxt = barcodevalcheck(itembarcode, 'item')
                                if itemstatus == 0:
                                    itemid = barcodetoid(itembarcode, 'int')
                                    if slotbaza.isitemexist(itemid):
                                        przedmiot = slotbaza.loaditem(itemid)
                                        if przedmiot['areaass'].areaid == areaid:
                                            if przedmiot['itemstate']:
                                                logbaza.itemchange(self.username, 'Override Come In', areaid, itemid)
                                                Dialog.komunikat('error',
                                                                 'Ten przedmiot jest już przyjęty na stan magazynu! '
                                                                 'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!', self,
                                                                 audio=7)
                                                self.rysujobszary()
                                                self.unblurwindow()
                                            else:
                                                istniejacyprzedmiotok = QuestionDialog.pytanie('Ten przedmiot znajduje '
                                                                                               'się w bazie:\n'
                                                                                               'Nazwa przedmiotu: '
                                                                                               + przedmiot['itemname']
                                                                                               + '\nStan: Wydany'
                                                                                                 '\nUwagi: '
                                                                                               + przedmiot['item'
                                                                                                           'comments']
                                                                                               + '\n\nCzy chcesz '
                                                                                                 'przyjąć '
                                                                                                 'przedmiot?', self,
                                                                                               audio=63)
                                                if istniejacyprzedmiotok:
                                                    przedmiot['itemstate'] = True
                                                    przedmiot['dateoflastincome'] = datetime.datetime.now()
                                                    przedmiot['useroflastincome'] = self.username
                                                    slotbaza.saveitem(przedmiot)
                                                    logbaza.itemchange(self.username, 'Come In', areaid, itemid)
                                                    Dialog.komunikat('ok', 'Przedmiot został przyjęty na stan magazynu',
                                                                     self, audio=23)
                                                    kolejnyprzedmiot = QuestionDialog.pytanie('Czy chcesz przyjąć '
                                                                                              'kolejny przedmiot '
                                                                                              'do obszaru'
                                                                                              ' ' + str(areaid) + '?',
                                                                                              self, audio=60)
                                                else:
                                                    logbaza.itemchange(self.username, 'Failed Come In', areaid, itemid)
                                                    Dialog.komunikat('warn', 'Przerwano proces przyjmowania przedmiotu.'
                                                                             '\nPrzedmiot nie został przyjęty', self,
                                                                     audio=41)
                                                    self.rysujobszary()
                                                    self.unblurwindow()
                                        else:
                                            Dialog.komunikat('error', 'Próbujesz przyjąć przedmiot, '
                                                                      'który jest przypisany do innego obszaru! '
                                                                      'Jeśli nie wiesz dlaczego, wezwij szefa ekipy.',
                                                             self, audio=4)
                                    else:
                                        nowyprzedmiotok = QuestionDialog.pytanie(
                                            'Wprowadzony przedmiot nie znajduje się na żadnym obszarze. '
                                            'Czy chcesz go dodać do obszaru ' + str(
                                                areaid) + '?', self, audio=64)
                                        if nowyprzedmiotok:
                                            nazwaprzedmiotu, nazwaprzedmiotuok = InputDialog.komunikat('txt',
                                                                                                       'Podaj nazwę '
                                                                                                       'nowego '
                                                                                                       'przedmiotu:',
                                                                                                       self, audio=58)
                                            if nazwaprzedmiotuok:
                                                slotbaza.createitem(itemid, idtobarcode(itemid, 'item'),
                                                                    nazwaprzedmiotu,
                                                                    areaid)
                                                przedmiot = slotbaza.loaditem(itemid)
                                                logbaza.itemchange(self.username, 'Create', areaid, itemid, '',
                                                                   przedmiot)
                                                przedmiot['itemstate'] = True
                                                przedmiot['dateoffirstincome'] = datetime.datetime.now()
                                                przedmiot['useroffirstincome'] = self.username
                                                przedmiot['useroflastincome'] = self.username
                                                przedmiot['dateoflastincome'] = datetime.datetime.now()
                                                logbaza.itemchange(self.username, 'First Come In', areaid, itemid, '',
                                                                   przedmiot)
                                                slotbaza.saveitem(przedmiot)
                                                Dialog.komunikat('ok',
                                                                 'Poprawnie dodano przedmiot.'
                                                                 '\nPredmiot został przyjęty na stan magazynu.',
                                                                 self, audio=18)
                                                kolejnyprzedmiot = QuestionDialog.pytanie(
                                                    'Czy chcesz przyjąć kolejny przedmiot do obszaru ' + str(
                                                        areaid) + '?',
                                                    self, audio=60)
                                            else:
                                                logbaza.itemchange(self.username, 'Creation Trial', areaid, itemid)
                                                Dialog.komunikat('warn',
                                                                 'Przerwano proces dodawania przedmiotu. '
                                                                 'Przedmiot nie został dodany.',
                                                                 self, audio=36)
                                                self.rysujobszary()
                                                self.unblurwindow()
                                            pass
                                        else:
                                            logbaza.itemchange(self.username, 'Creation Trial', areaid, itemid)
                                            Dialog.komunikat('error',
                                                             'W takim razie albo zeskanowałeś zły kod, '
                                                             'albo coś się popsuło... \nWezwij szefa ekipy.',
                                                             self, audio=10)
                                            self.rysujobszary()
                                            self.unblurwindow()
                                else:
                                    Dialog.komunikat('warn', itemstatustxt, self)
                                    self.rysujobszary()
                                    self.unblurwindow()
                            else:
                                pass
                        self.rysujobszary()
                        self.unblurwindow()
                    else:
                        logbaza.itemchange(self.username, 'Assignment Fail during come in', areaid, 0)
                        Dialog.komunikat('warn',
                                         'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                         'do niego przedmioty.', self, audio=49)
                        self.unblurwindow()
                else:
                    Dialog.komunikat('warn', areastatustxt, self)
                    self.unblurwindow()
            else:
                self.unblurwindow()

    # Obsługa wydawania przedmiotów
    def comeout(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.blurwindow()
            areabarcode, areaok = InputDialog.komunikat('barcode', 'Wczytaj kod obszaru:', self, audio=53)
            if areaok:
                areastatus, areastatustxt = barcodevalcheck(areabarcode, 'area')
                if areastatus == 0:
                    areaid = barcodetoid(areabarcode, 'int')
                    if slotbaza.isareaexist(areaid):
                        kolejnyprzedmiot = True
                        self.selected = areaid
                        self.rysujobszary()
                        self.selected = 0
                        while kolejnyprzedmiot:
                            kolejnyprzedmiot = False

                            itembarcode, itemok = InputDialog.komunikat('barcode', 'Wczytaj kod przedmiotu:', self,
                                                                        audio=54)
                            if itemok:
                                itemstatus, itemstatustxt = barcodevalcheck(itembarcode, 'item')
                                if itemstatus == 0:
                                    itemid = barcodetoid(itembarcode, 'int')
                                    if slotbaza.isitemexist(itemid):
                                        przedmiot = slotbaza.loaditem(itemid)
                                        if przedmiot['areaass'].areaid == areaid:
                                            if przedmiot['itemstate']:
                                                istniejacyprzedmiotok = QuestionDialog.pytanie(
                                                    'Ten przedmiot znajduje się w bazie:\nNazwa przedmiotu: ' +
                                                    przedmiot[
                                                        'itemname'] + '\nStan: Przyjęty\nUwagi: ' + przedmiot[
                                                        'itemcomments'] + '\n\nCzy chcesz wydać przedmiot?', self,
                                                    audio=62)
                                                if istniejacyprzedmiotok:
                                                    przedmiot['itemstate'] = False
                                                    przedmiot['dateoflastoutcome'] = datetime.datetime.now()
                                                    przedmiot['useroflastoutcome'] = self.username
                                                    slotbaza.saveitem(przedmiot)
                                                    logbaza.itemchange(self.username, 'Come Out', areaid, itemid)
                                                    Dialog.komunikat('ok', 'Przedmiot został wydany z magazynu', self,
                                                                     audio=24)
                                                    kolejnyprzedmiot = QuestionDialog.pytanie(
                                                        'Czy chcesz wydać kolejny przedmiot z obszaru ' + str(
                                                            areaid) + '?',
                                                        self, audio=61)
                                                else:
                                                    logbaza.itemchange(self.username, 'Failed Come Out', areaid, itemid)
                                                    Dialog.komunikat('warn',
                                                                     'Przerwano proces wydawania przedmiotu.'
                                                                     '\nPrzedmiot nie został wydany',
                                                                     self, audio=43)
                                                    self.rysujobszary()
                                                    self.unblurwindow()
                                            else:
                                                logbaza.itemchange(self.username, 'Override Come Out', areaid, itemid)
                                                Dialog.komunikat('error',
                                                                 'Ten przedmiot jest już wydany z magazynu! '
                                                                 'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                                 self, audio=8)
                                                self.rysujobszary()
                                                self.unblurwindow()
                                        else:
                                            Dialog.komunikat('error', 'Próbujesz wydać przedmiot, '
                                                                      'który jest przypisany do innego obszaru! '
                                                                      'Jeśli nie wiesz dlaczego, wezwij szefa ekipy.',
                                                             self, audio=4)
                                    else:
                                        logbaza.itemchange(self.username, 'Failed Come Out Critical', areaid, itemid)
                                        Dialog.komunikat('error',
                                                         'Próbujesz wydać przedmiot, który nie znajduje się w bazie! '
                                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                         self, audio=5)
                                        self.rysujobszary()
                                        self.unblurwindow()
                                else:
                                    Dialog.komunikat('warn', itemstatustxt, self)
                                    self.rysujobszary()
                                    self.unblurwindow()
                            else:
                                self.rysujobszary()
                                self.unblurwindow()
                        self.rysujobszary()
                        self.unblurwindow()
                    else:
                        logbaza.itemchange(self.username, 'Assignment Fail during come out', areaid, 0)
                        Dialog.komunikat('warn',
                                         'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                         'do niego przedmioty.', self, audio=49)
                        self.unblurwindow()
                else:
                    Dialog.komunikat('warn', areastatustxt, self)
                    self.unblurwindow()
            else:
                self.unblurwindow()

    # Moduł SLOT Orkiestry
    def orchestra(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.orchestramodule.toggleshow()
            self.updateorchcounters()

    # Funkcja odświeżająca liczniki w module SLOT Orkiestry
    def updateorchcounters(self):
        overall = slotbaza.orchcountall()
        present = slotbaza.orchcountpresent()
        nonpresent = overall - present
        self.orchestramodule.le_overall.setText(str(overall))
        self.orchestramodule.le_onmagazine.setText(str(present))
        self.orchestramodule.le_outmagazine.setText(str(nonpresent))

    # Wyświetlenie listy przedmiotów ze SLOT Orkiestry
    def orchtable(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.blurwindow()
            model = slotbaza.getqorchmodel()
            OrchList.showtable(model)
            self.unblurwindow()

    # SLOT Orkiestra - pierwsze przyjęcie przedmiotu
    def orchfirstcomein(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.blurwindow()
            orchbarcode, orchok = InputDialog.komunikat('barcode', 'Naklej kod kreskowy na plakietkę uczestnika, '
                                                                   'a następnie go zeskanuj:', self, audio=50)
            if orchok:
                orchstatus, orchstatustxt = barcodevalcheck(orchbarcode, 'orch')
                if orchstatus == 0:
                    orchid = barcodetoid(orchbarcode, 'int')
                    if slotbaza.isorchexist(orchid):
                        logbaza.orchchange(self.username, 'Override Trial during first come in', orchid)
                        Dialog.komunikat('error',
                                         'Ten przedmiot jest już przyjęty na stan magazynu! '
                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                         self, audio=7)
                        self.unblurwindow()
                    else:
                        slotbaza.createorch(orchid, idtobarcode(orchid, 'orch'), self.username)
                        orchitem = slotbaza.loadorch(orchid)
                        logbaza.orchchange(self.username, 'Creation', orchid, '', orchitem)
                        nowyorchitem, ok = OrchEditDialog.firstcomein(orchitem, self)
                        if ok:
                            slotbaza.saveorch(nowyorchitem)
                            logbaza.orchchange(self.username, 'Creation Edit', orchid, orchitem, nowyorchitem)
                            orchitembarcode, orchitemok = InputDialog.komunikat('barcode',
                                                                                'Naklej kod kreskowy na przedmiot, '
                                                                                'a następnie go zeskanuj:',
                                                                                self, audio=55)
                            if orchitemok:
                                orchitemstatus, orchitemstatustxt = barcodevalcheck(orchitembarcode, 'orch')
                                if orchitemstatus == 0:
                                    orchitemid = barcodetoid(orchitembarcode, 'int')
                                    if orchid == orchitemid:
                                        nowyorchitem['itemstate'] = True
                                        nowyorchitem['dateoflastincome'] = datetime.datetime.now()
                                        nowyorchitem['useroflastincome'] = self.username
                                        slotbaza.saveorch(nowyorchitem)
                                        logbaza.orchchange(self.username, 'First Come In', orchid)
                                        Dialog.komunikat('ok', 'Poprawnie przyjęto przedmiot do SLOT Orkiestry', self,
                                                         audio=19)
                                        self.unblurwindow()
                                        self.updateorchcounters()
                                    else:
                                        logbaza.orchchange(self.username, 'Differential during first come in', orchid)
                                        Dialog.komunikat('error',
                                                         'Kod naklejony na plakietkę i na przedmiot Różnią się! Jeśli '
                                                         'nie wiesz dlaczego, wezwij szefa ekipy!',
                                                         self, audio=1)
                                        self.unblurwindow()
                                        self.updateorchcounters()
                                else:
                                    Dialog.komunikat('warn', orchitemstatustxt, self)
                                    Dialog.komunikat('warn',
                                                     'Nie wczytano kodu z przedmiotu! Wpis w bazie został utworzony, '
                                                     'ale przedmiot nie został przyjety na magazyn!',
                                                     self, audio=32)
                                    self.unblurwindow()
                                    self.updateorchcounters()
                            else:
                                Dialog.komunikat('warn',
                                                 'Nie wczytano kodu z przedmiotu! Wpis w bazie został utworzony, '
                                                 'ale przedmiot nie został przyjety na magazyn!',
                                                 self, audio=32)
                                self.unblurwindow()
                                self.updateorchcounters()
                        else:
                            Dialog.komunikat('warn',
                                             'Przerwano proces edycji obszaru! Wpis w bazie został utworzony, '
                                             'ale żadne zmiany nie zostały zapisane.',
                                             self, audio=40)
                            self.unblurwindow()
                            self.updateorchcounters()
                else:
                    Dialog.komunikat('warn', orchstatustxt, self)
                    self.unblurwindow()
                    self.updateorchcounters()
            else:
                Dialog.komunikat('warn', 'Przerwano proces edycji obszaru! Żadne zmiany nie zostały zapisane.', self,
                                 audio=39)
                self.unblurwindow()
                self.updateorchcounters()

    # SLOT Orkiestra - przyjęcie przedmiotu
    def orchcomein(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.blurwindow()
            orchbarcode, orchok = InputDialog.komunikat('barcode', 'Wczytaj kod kreskowy z plakietki uczestnika:', self,
                                                        audio=52)
            if orchok:
                orchstatus, orchstatustxt = barcodevalcheck(orchbarcode, 'orch')
                if orchstatus == 0:
                    orchid = barcodetoid(orchbarcode, 'int')
                    if slotbaza.isorchexist(orchid):
                        orchitem = slotbaza.loadorch(orchid)
                        nowyorchitem, ok = OrchEditDialog.comein(orchitem, self)
                        if ok:
                            if nowyorchitem['itemstate']:
                                logbaza.orchchange(self.username, 'Override Trial during come in', orchid)
                                Dialog.komunikat('error',
                                                 'Próbujesz przyjąć przedmiot, '
                                                 'który już jest przyjęty na stan magazynu! '
                                                 'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                 self, audio=3)
                                self.unblurwindow()
                            else:
                                orchitembarcode, orchitemok = InputDialog.komunikat('barcode',
                                                                                    'Wczytaj kod kreskowy '
                                                                                    'z naklejki na przedmiocie',
                                                                                    self, audio=51)
                                if orchitemok:
                                    orchitemstatus, orchitemstatustxt = barcodevalcheck(orchitembarcode, 'orch')
                                    if orchitemstatus == 0:
                                        orchitemid = barcodetoid(orchitembarcode, 'int')
                                        if orchid == orchitemid:
                                            nowyorchitem['itemstate'] = True
                                            nowyorchitem['dateoflastincome'] = datetime.datetime.now()
                                            nowyorchitem['useroflastincome'] = self.username
                                            slotbaza.saveorch(nowyorchitem)
                                            logbaza.orchchange(self.username, 'Come In', orchid)
                                            Dialog.komunikat('ok', 'Poprawnie przyjęto przedmiot do SLOT Orkiestry',
                                                             self, audio=19)
                                            self.unblurwindow()
                                            self.updateorchcounters()
                                        else:
                                            logbaza.orchchange(self.username, 'Differential during come in', orchid)
                                            Dialog.komunikat('error',
                                                             'Kod naklejony na plakietkę i na przedmiot Różnią się! '
                                                             'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                             self, audio=1)
                                            self.unblurwindow()
                                            self.updateorchcounters()
                                    else:
                                        Dialog.komunikat('warn', orchitemstatustxt, self)
                                        Dialog.komunikat('warn',
                                                         'Nie wczytano kodu z przedmiotu! '
                                                         'Przedmiot nie został przyjety na magazyn!',
                                                         self, audio=33)
                                        self.unblurwindow()
                                        self.updateorchcounters()
                                else:
                                    Dialog.komunikat('warn',
                                                     'Nie wczytano kodu z przedmiotu! '
                                                     'Przedmiot nie został przyjety na magazyn!',
                                                     self, audio=33)
                                    self.unblurwindow()
                                    self.updateorchcounters()
                        else:
                            Dialog.komunikat('warn',
                                             'Przerwano proces przyjmowania przedmiotu! '
                                             'Przedmiot nie został przyjety na magazyn!',
                                             self, audio=33)
                            self.unblurwindow()
                            self.updateorchcounters()
                    else:
                        logbaza.orchchange(self.username, 'Failed Come In Critical', orchid)
                        Dialog.komunikat('error',
                                         'Ten przedmiot nie znajduje się w bazie! '
                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                         self, audio=9)
                        self.unblurwindow()
                else:
                    Dialog.komunikat('warn', orchstatustxt, self)
                    self.unblurwindow()
                    self.updateorchcounters()
            else:
                Dialog.komunikat('warn',
                                 'Przerwano proces przyjmowania przedmiotu! Przedmiot nie został przyjęty na magazyn.',
                                 self, audio=42)
                self.unblurwindow()
                self.updateorchcounters()

    # SLOT Orkiestra - wydanie przedmiotu
    def orchcomeout(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!', self, audio=28)
            self.unblurwindow()
        else:
            self.blurwindow()
            orchbarcode, orchok = InputDialog.komunikat('barcode', 'Wczytaj kod kreskowy z plakietki uczestnika:', self,
                                                        audio=52)
            if orchok:
                orchstatus, orchstatustxt = barcodevalcheck(orchbarcode, 'orch')
                if orchstatus == 0:
                    orchid = barcodetoid(orchbarcode, 'int')
                    if slotbaza.isorchexist(orchid):
                        orchitem = slotbaza.loadorch(orchid)
                        nowyorchitem, ok = OrchEditDialog.comeout(orchitem, self)
                        if ok:
                            if not (nowyorchitem['itemstate']):
                                logbaza.orchchange(self.username, 'Override Trial during come out', orchid)
                                Dialog.komunikat('error',
                                                 'Próbujesz wydać przedmiot, '
                                                 'który już jest wydany z magazynu! '
                                                 'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                 self, audio=6)
                                self.unblurwindow()
                            else:
                                orchitembarcode, orchitemok = InputDialog.komunikat('barcode',
                                                                                    'Wczytaj kod kreskowy z '
                                                                                    'naklejki na przedmiocie',
                                                                                    self, audio=51)
                                if orchitemok:
                                    orchitemstatus, orchitemstatustxt = barcodevalcheck(orchitembarcode, 'orch')
                                    if orchitemstatus == 0:
                                        orchitemid = barcodetoid(orchitembarcode, 'int')
                                        if orchid == orchitemid:
                                            nowyorchitem['itemstate'] = False
                                            nowyorchitem['dateoflastoutcome'] = datetime.datetime.now()
                                            nowyorchitem['useroflastoutcome'] = self.username
                                            slotbaza.saveorch(nowyorchitem)
                                            logbaza.orchchange(self.username, 'Come Out', orchid)
                                            Dialog.komunikat('ok', 'Poprawnie wydano przedmiot ze SLOT Orkiestry', self,
                                                             audio=21)
                                            self.unblurwindow()
                                            self.updateorchcounters()
                                        else:
                                            logbaza.orchchange(self.username, 'Differential during come out', orchid)
                                            Dialog.komunikat('error',
                                                             'Kod naklejony na plakietkę i na przedmiot Różnią się! '
                                                             'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                             self, audio=1)
                                            self.unblurwindow()
                                            self.updateorchcounters()
                                    else:
                                        Dialog.komunikat('warn', orchitemstatustxt, self)
                                        Dialog.komunikat('warn',
                                                         'Nie wczytano kodu z przedmiotu! '
                                                         'Przedmiot nie został wydany z magazynu!',
                                                         self, audio=34)
                                        self.unblurwindow()
                                        self.updateorchcounters()
                                else:
                                    Dialog.komunikat('warn',
                                                     'Nie wczytano kodu z przedmiotu! '
                                                     'Przedmiot nie został wydany z magazynu!',
                                                     self, audio=34)
                                    self.unblurwindow()
                                    self.updateorchcounters()
                        else:
                            Dialog.komunikat('warn',
                                             'Przerwano proces wydawania przedmiotu! '
                                             'Przedmiot nie został wydany z magazynu!',
                                             self, audio=34)
                            self.unblurwindow()
                            self.updateorchcounters()
                    else:
                        logbaza.orchchange(self.username, 'Failed Come Out Critical', orchid)
                        Dialog.komunikat('error',
                                         'Ten przedmiot nie znajduje się w bazie! '
                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                         self, audio=9)
                        self.unblurwindow()
                else:
                    Dialog.komunikat('warn', orchstatustxt, self)
                    self.unblurwindow()
                    self.updateorchcounters()
            else:
                Dialog.komunikat('warn',
                                 'Przerwano proces wydawania przedmiotu! Przedmiot nie został wydany z magazynu!',
                                 self, audio=44)
                self.unblurwindow()
                self.updateorchcounters()

    def changefillmode(self):
        if self.viewer.fill == 'hide':
            self.viewer.fill = 'show'
            self.rysujobszary()
        elif self.viewer.fill == 'show':
            self.viewer.fill = 'hide'
            self.rysujobszary()

    def changelabelmode(self):
        if self.viewer.labels == 'number':
            self.viewer.labels = 'name'
        elif self.viewer.labels == 'name':
            self.viewer.labels = 'number'
        self.rysujobszary()

    def changesoundconfig(self):
        self.config['sound_ok'] = int(self.btn_sound_ok.isChecked())
        self.config['sound_warn'] = int(self.btn_sound_warn.isChecked())
        self.config['sound_error'] = int(self.btn_sound_error.isChecked())
        self.config['sound_info'] = int(self.btn_sound_info.isChecked())
        self.config['sound_other'] = int(self.btn_sound_other.isChecked())
        self.config['sound_txt'] = int(self.btn_sound_txt.isChecked())
        self.config['sound_barcode'] = int(self.btn_sound_barcode.isChecked())
        self.saveconfig()

    # Funkcja rysująca obszary, po wcześniejszym wyczyszczeniu sceny
    def rysujobszary(self):
        self.wyczyscscene()
        obszary = slotbaza.getareageometries()  # Wczytanie geometrii obszarów

        # Wybór czcionki
        font = QFont()
        font.setPixelSize(18)
        font.setBold(True)
        orkiestra = {'posx': 370, 'posy': 750, 'sizex': 260, 'sizey': 100}
        orchgrupa = QGraphicsItemGroup()
        orchprosto = QGraphicsRectItem(
            QRectF(orkiestra['posx'], orkiestra['posy'], orkiestra['sizex'], orkiestra['sizey']))
        orchgradient = QLinearGradient(QPoint(orkiestra['posx'], orkiestra['posy']),
                                       QPoint(orkiestra['posx'], orkiestra['posy'] + orkiestra['sizey']))
        orchgradient.setColorAt(0, QColor('#33FF48FF'))
        orchgradient.setColorAt(1, QColor('#55BB48FF'))
        orchprosto.setBrush(orchgradient)

        orchlabel = QGraphicsTextItem('SLOT Orkiestra')
        orchlabel.setDefaultTextColor(Qt.white)
        orchlabel.setFont(font)

        orchlabel_br = orchlabel.boundingRect()
        orchlabel.setPos(orkiestra['posx'] + orkiestra['sizex'] / 2 - orchlabel_br.width() / 2,
                         orkiestra['posy'] + orkiestra['sizey'] / 2 - orchlabel_br.height() / 2)
        orchlabel.setTransformOriginPoint(orchlabel_br.width() / 2, orchlabel_br.height() / 2)
        orchlabel.setRotation(round((-int(self.config['viewangle']))/180)*180)
        # Dodanie prostokąta i etykiety do grupy
        orchgrupa.addToGroup(orchprosto)
        orchgrupa.addToGroup(orchlabel)

        orchgrupa.setFlag(QGraphicsItem.ItemIsMovable, True)  # Ustawienie grupy jako możliwej do przesunięcia
        self.scena.addItem(orchgrupa)  # dodanie grupy do sceny

        for obszar in obszary:
            grupa = QGraphicsItemGroup()  # Tworzy grupę
            itempresent = slotbaza.areacountitemspresent(obszar['areaid'])
            itemall = slotbaza.areacountitemsall(obszar['areaid'])
            tooltiptxt = obszar['areaname'] + '\n' + str(itempresent) + ' / ' + str(itemall)
            grupa.setToolTip(tooltiptxt)
            # Stworzenie prostokąta
            prosto = QGraphicsRectItem(QRectF(obszar['posx'], obszar['posy'], obszar['sizex'], obszar['sizey']))
            gradient = QLinearGradient(QPoint(int(obszar['posx']), int(obszar['posy'])),
                                       QPoint(int(obszar['posx']), int(obszar['posy'] + obszar['sizey'])))
            if self.viewer.fill == 'show':
                if slotbaza.areacountitemsall(obszar['areaid']) == 0:
                    gradient.setColorAt(0, QColor('#99000000'))
                    gradient.setColorAt(1, QColor('#BB000000'))
                else:
                    procent = (itempresent / itemall) * 100
                    if procent == 0:
                        gradient.setColorAt(0, QColor('#22006600'))
                        gradient.setColorAt(1, QColor('#33006600'))
                    elif procent < 20:
                        gradient.setColorAt(0, QColor('#44FF5500'))
                        gradient.setColorAt(1, QColor('#44FF5500'))
                    elif procent < 40:
                        gradient.setColorAt(0, QColor('#66FF4400'))
                        gradient.setColorAt(1, QColor('#77FF4400'))
                    elif procent < 60:
                        gradient.setColorAt(0, QColor('#88FF3300'))
                        gradient.setColorAt(1, QColor('#99FF3300'))
                    elif procent < 80:
                        gradient.setColorAt(0, QColor('#AAFF2200'))
                        gradient.setColorAt(1, QColor('#BBFF2200'))
                    elif procent < 100:
                        gradient.setColorAt(0, QColor('#CCFF1100'))
                        gradient.setColorAt(1, QColor('#DDFF1100'))
                    else:
                        gradient.setColorAt(0, QColor('#EEFF0000'))
                        gradient.setColorAt(1, QColor('#FFFF0000'))
            else:
                if self.selected == 0:
                    gradient.setColorAt(0, QColor('#220087FF'))
                    gradient.setColorAt(1, QColor('#440048FF'))
                else:
                    if obszar['areaid'] == self.selected:
                        gradient.setColorAt(0, QColor('#AAFFAA22'))
                        gradient.setColorAt(1, QColor('#FFFF5522'))
                    else:
                        gradient.setColorAt(0, QColor('#220087FF'))
                        gradient.setColorAt(1, QColor('#440048FF'))
            prosto.setBrush(gradient)

            # Stworzenie etykiety
            if self.viewer.labels == 'number':
                etykieta = QGraphicsTextItem(str(obszar['areaid']))
                etykieta.setDefaultTextColor(Qt.white)
                etykieta.setFont(font)
            elif self.viewer.labels == 'name':
                font.setPixelSize(12)
                font.setFamily('arial')
                font.setBold(False)
                etykieta = QGraphicsTextItem(obszar['areaname'])
                etykieta.setDefaultTextColor(Qt.white)
                etykieta.setFont(font)
                # etykieta.setTextWidth(obszar['sizex'])

            etykieta_br = etykieta.boundingRect()
            etykieta.setPos(obszar['posx'] + obszar['sizex'] / 2 - etykieta_br.width() / 2,
                            obszar['posy'] + obszar['sizey'] / 2 - etykieta_br.height() / 2)
            etykieta.setTransformOriginPoint(etykieta_br.width() / 2, etykieta_br.height() / 2)
            etykieta.setRotation(-int(self.config['viewangle']))
            # Dodanie prostokąta i etykiety do grupy
            grupa.addToGroup(prosto)
            grupa.addToGroup(etykieta)

            grupa.setFlag(QGraphicsItem.ItemIsMovable, True)  # Ustawienie grupy jako możliwej do przesunięcia
            self.scena.addItem(grupa)  # dodanie grupy do sceny

    def rotateview(self):
        self.applyrotation(90)
        self.config['viewangle'] = (int(self.config['viewangle']) + 90) % 360
        self.saveconfig()
        self.rysujobszary()

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
