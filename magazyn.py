# -*- coding: utf-8 -*-

# Główny plik programu do obsługi Magazynu Scenicznego.
# W pliku tym przywołane jest główne okno programu, a także wszystkie okna dialogowe.
# Przywołanie to następuje z pliku "clear_gui" (ostatnia linia importu)

import datetime
import hashlib
import sys

from PyQt5.QtCore import Qt, QPoint, QRectF
from PyQt5.QtGui import QFont, QLinearGradient, QColor, QPolygonF, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsItem, QGraphicsItemGroup, QGraphicsTextItem

import slotbaza
import logbaza
from clear_gui import MainWindow, LoginDialog, Dialog, InputDialog, QuestionDialog, AreaEditDialog, AreaListSmall, \
    AreaList, ItemList, OrchList, OrchestraModule, OrchEditDialog, AdminPanel

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
                    try:
                        int(code[6:9])
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
        self.setupUI()
        self.rysujobszary()
        # Domyślnie po włączeniu programu nikt nie jest zalogowany
        self.loginbypass = True  # Jeśli True to do obsługi programu niewymagane jest logowanie
        self.loginstatus = False
        self.username = ''
        self.usertype = 'user'
        self.logstatus.setText("<FONT COLOR=\'#FF4444\'> Niezalogowany")
        self.updateorchcounters()

        # Połączenie przycisków z odpowiednimi funkcjami
        self.connectbuttons()

    # Połączenie przycisków z odpowiednimi funkcjami
    def connectbuttons(self):
        self.btn_login.clicked.connect(self.logowanie)
        self.btn_logout.clicked.connect(self.logowanie)
        self.btn_addarea.clicked.connect(self.addarea)
        self.btn_listofareas.clicked.connect(self.listofareas)
        self.btn_itemcounter.clicked.connect(self.itemcounter)
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
        self.btn_adminpanel.clicked.connect(self.adminpanel)
        self.viewer.rectChanged.connect(self.areadrawend)

    def adminpanel(self):
        self.blurwindow()
        login, haslo, ok = LoginDialog.getloginhaslo(self)
        if not ok:
            self.unblurwindow()
            return
        if not slotbaza.isuserexist(login):
            logbaza.userchange(self.username, 'Admin Login Fail', login)
            Dialog.komunikat('warn', 'Logowanie Administratora nieudane')
            self.unblurwindow()
            return
        if not login == 'admin':
            logbaza.userchange(self.username, 'Admin Login Fail', login)
            Dialog.komunikat('warn', 'Logowanie Administratora nieudane')
            self.unblurwindow()
            return
        if not slotbaza.loginvalidate(login, hashpassword(haslo))['login']:
            logbaza.userchange(self.username, 'Admin Login Fail', login)
            Dialog.komunikat('warn', 'Logowanie Administratora nieudane')
            self.unblurwindow()
            return
        logbaza.userchange(self.username, 'Admin Login Succes')
        Dialog.komunikat('ok', 'Pomyslnie zalogowano')
        AdminPanel.panel(self)

        self.unblurwindow()

    # Moduł logowania do programu
    def logowanie(self):
        sender = self.sender()
        # jeśli wysyłającym jest przycisk ZALOGUJ
        if sender.objectName() == 'btn_login':
            if self.loginstatus:
                Dialog.komunikat('warn', 'Nie można się zalogować będąc zalogowanym', self)
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
                            Dialog.komunikat('ok', 'Pomyślnie zalogowano do systemu', self)
                            self.unblurwindow()
                        else:
                            logbaza.userchange(login, 'Failed Log In (wrong password)')
                            Dialog.komunikat('warn', 'Logowanie nieudane! Niepoprawne hasło.', self)
                            self.unblurwindow()
                    else:
                        logbaza.userchange(login, 'Failed Log In (wrong username)')
                        Dialog.komunikat('warn', 'Użytkownik o podanym loginie nie istnieje.', self)
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
                Dialog.komunikat('ok', 'Pomyślnie wylogowano z systemu', self)
                self.unblurwindow()
            else:
                self.blurwindow()
                Dialog.komunikat('warn', 'Nie można się wylogować nie będąc wcześniej zalogowanym', self)
                self.unblurwindow()

    # Wyświetlenie listy wszystkich obszarów
    def listofareas(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
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
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
            self.unblurwindow()
        else:
            self.blurwindow()
            areaid, areaok = InputDialog.komunikat('txt', 'Podaj numer obszaru:', self)
            if areaok:
                areabarcode = idtobarcode(areaid, 'area')
                areastatus, areastatustxt = barcodevalcheck(areabarcode, 'area')
                if areastatus == 0:
                    if slotbaza.isareaexist(areaid):
                        logbaza.areachange(self.username, 'Override Trial', areaid)
                        Dialog.komunikat('warn', 'Obszar o wprowadzonym numerze już istnieje!', self)
                        self.unblurwindow()
                    else:
                        areaname, nameok = InputDialog.komunikat('txt', 'Podaj nazwę nowego obszaru:', self)
                        if nameok:
                            Dialog.komunikat('info', 'Narysuj obszar na mapie magazynu')

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

    def areadrawend(self, pos):
        self.viewer.normalmode()  # przełączenie viewera w normalny tryb pracy
        coords = self.viewer.mapToScene(pos)  # viewer zwraca coordy globalne, trzeba je zmapować na scene

        # sprawdzenie czy użytkownik narysował prostokąt
        if len(coords) == 0:
            self.viewer.rubberBand.hide()
            self.blurwindow()
            Dialog.komunikat('warn', 'Narysowano niepoprawny prostokąt! Obszar nie został utworzony', self)
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
                Dialog.komunikat('ok', 'Poprawnie stworzono obszar.', self)
                self.unblurwindow()
            else:
                Dialog.komunikat('warn', 'Przerwano proces edycji obszaru! '
                                         'Obszar został utworzony, ale zmiany nie zostały zapisane.', self)
                self.unblurwindow()

    # Edycja wybranego na liście obszaru
    def editarea(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
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
                        nowyobszar, ok = AreaEditDialog.editarea(obszar, self)
                        if ok:
                            logbaza.areachange(self.username, 'Edit', areaid, obszar, nowyobszar)
                            slotbaza.savearea(nowyobszar)
                            Dialog.komunikat('ok', 'Poprawnie zmodyfikowano obszar.', self)
                            self.unblurwindow()
                        else:
                            Dialog.komunikat('warn', 'Przerwano proces edycji obszaru! Zmiany nie zostały zapisane.',
                                             self)
                            self.unblurwindow()
                    else:
                        Dialog.komunikat('warn',
                                         'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                         'do niego przedmioty.', self)
                        self.unblurwindow()
            else:
                self.unblurwindow()

    # Wyszukiwanie przedmiotów
    def finditem(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
            self.unblurwindow()
        else:
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
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
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
                        self.itemlist(areaid)
                    else:
                        Dialog.komunikat('warn',
                                         'Wskazany obszar nie istnieje!\n'
                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy', self)
                        self.unblurwindow()
            else:
                self.unblurwindow()

    # Wyświetlenie listy przedmiotów w obszarze od zadanym ID
    def itemlist(self, areaid):
        model = slotbaza.getqitemmodel(areaid)
        ItemList.showtable(model)
        self.unblurwindow()

    def itemcounter(self):
        pass

    # Obsługa przyjmowania przedmiotów
    def comein(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
            self.unblurwindow()
        else:
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
                                            logbaza.itemchange(self.username, 'Override Come In', areaid, itemid)
                                            Dialog.komunikat('error',
                                                             'Ten przedmiot jest już przyjęty na stan magazynu! '
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
                                                logbaza.itemchange(self.username, 'Come In', areaid, itemid)
                                                Dialog.komunikat('ok', 'Przedmiot został przyjęty na stan magazynu',
                                                                 self)
                                                kolejnyprzedmiot = QuestionDialog.pytanie('Czy chcesz przyjąć '
                                                                                          'kolejny przedmiot do obszaru'
                                                                                          ' ' + str(areaid) + '?', self)
                                            else:
                                                logbaza.itemchange(self.username, 'Failed Come In', areaid, itemid)
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
                                                slotbaza.createitem(itemid, idtobarcode(itemid, 'item'),
                                                                    nazwaprzedmiotu,
                                                                    areaid)
                                                logbaza.itemchange(self.username, 'Create', areaid, itemid, '',
                                                                   przedmiot)
                                                przedmiot = slotbaza.loaditem(itemid)
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
                                                                 self)
                                                kolejnyprzedmiot = QuestionDialog.pytanie(
                                                    'Czy chcesz przyjąć kolejny przedmiot do obszaru ' + str(
                                                        areaid) + '?',
                                                    self)
                                            else:
                                                logbaza.itemchange(self.username, 'Creation Trial', areaid, itemid)
                                                Dialog.komunikat('warn',
                                                                 'Przerwano proces dodawania przedmiotu. '
                                                                 'Przedmiot nie został dodany.',
                                                                 self)
                                                self.unblurwindow()
                                            pass
                                        else:
                                            logbaza.itemchange(self.username, 'Creation Trial', areaid, itemid)
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
                        logbaza.itemchange(self.username, 'Assignment Fail during come in', areaid, 0)
                        Dialog.komunikat('warn',
                                         'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                         'do niego przedmioty.', self)
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
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
            self.unblurwindow()
        else:
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
                                                logbaza.itemchange(self.username, 'Come Out', areaid, itemid)
                                                Dialog.komunikat('ok', 'Przedmiot został wydany z magazynu', self)
                                                kolejnyprzedmiot = QuestionDialog.pytanie(
                                                    'Czy chcesz wydać kolejny przedmiot z obszaru ' + str(areaid) + '?',
                                                    self)
                                            else:
                                                logbaza.itemchange(self.username, 'Failed Come Out', areaid, itemid)
                                                Dialog.komunikat('warn',
                                                                 'Przerwano proces wydawania przedmiotu.'
                                                                 '\nPrzedmiot nie został wydany',
                                                                 self)
                                                self.unblurwindow()
                                        else:
                                            logbaza.itemchange(self.username, 'Override Come Out', areaid, itemid)
                                            Dialog.komunikat('error',
                                                             'Ten przedmiot jest już wydany z magazynu! '
                                                             'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                             self)
                                            self.unblurwindow()
                                    else:
                                        logbaza.itemchange(self.username, 'Failed Come Out Critical', areaid, itemid)
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
                        logbaza.itemchange(self.username, 'Assignment Fail during come out', areaid, 0)
                        Dialog.komunikat('warn',
                                         'Wskazany obszar nie istnieje!\nDodaj najpierw obszar, aby móc przyjmować '
                                         'do niego przedmioty.', self)
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
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
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
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
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
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
            self.unblurwindow()
        else:
            self.blurwindow()
            orchbarcode, orchok = InputDialog.komunikat('barcode', 'Naklej kod kreskowy na plakietkę uczestnika, '
                                                                   'a następnie go zeskanuj:', self)
            if orchok:
                orchstatus, orchstatustxt = barcodevalcheck(orchbarcode, 'orch')
                if orchstatus == 0:
                    orchid = barcodetoid(orchbarcode, 'int')
                    if slotbaza.isorchexist(orchid):
                        logbaza.orchchange(self.username, 'Override Trial during first come in', orchid)
                        Dialog.komunikat('error',
                                         'Ten przedmiot jest już przyjęty na stan magazynu! '
                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                         self)
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
                                                                                self)
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
                                        Dialog.komunikat('ok', 'Poprawnie przyjęto przedmiot do SLOT Orkiestry', self)
                                        self.unblurwindow()
                                        self.updateorchcounters()
                                    else:
                                        logbaza.orchchange(self.username, 'Differential durgin first come in', orchid)
                                        Dialog.komunikat('error',
                                                         'Kod naklejony na plakietkę i na przedmiot Różnią się! Jeśli '
                                                         'nie wiesz dlaczego, wezwij szefa ekipy!',
                                                         self)
                                        self.unblurwindow()
                                        self.updateorchcounters()
                                else:
                                    Dialog.komunikat('warn', orchitemstatustxt, self)
                                    Dialog.komunikat('warn',
                                                     'Nie wczytano kodu z przedmiotu! Wpis w bazie został utworzony, '
                                                     'ale przedmiot nie został przyjety na magazyn!',
                                                     self)
                                    self.unblurwindow()
                                    self.updateorchcounters()
                            else:
                                Dialog.komunikat('warn',
                                                 'Nie wczytano kodu z przedmiotu! Wpis w bazie został utworzony, '
                                                 'ale przedmiot nie został przyjety na magazyn!',
                                                 self)
                                self.unblurwindow()
                                self.updateorchcounters()
                        else:
                            Dialog.komunikat('warn',
                                             'Przerwano proces edycji obszaru! Wpis w bazie został utworzony, '
                                             'ale żadne zmiany nie zostały zapisane.',
                                             self)
                            self.unblurwindow()
                            self.updateorchcounters()
                else:
                    Dialog.komunikat('warn', orchstatustxt, self)
                    self.unblurwindow()
                    self.updateorchcounters()
            else:
                Dialog.komunikat('warn', 'Przerwano proces edycji obszaru! Żadne zmiany nie zostały zapisane.', self)
                self.unblurwindow()
                self.updateorchcounters()

    # SLOT Orkiestra - przyjęcie przedmiotu
    def orchcomein(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
            self.unblurwindow()
        else:
            self.blurwindow()
            orchbarcode, orchok = InputDialog.komunikat('barcode', 'Wczytaj kod kreskowy z plakietki uczestnika:', self)
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
                                                 'który już jest przyjęty na stan magazynu!'
                                                 'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                 self)
                                self.unblurwindow()
                            else:
                                orchitembarcode, orchitemok = InputDialog.komunikat('barcode',
                                                                                    'Wczytaj kod kreskowy z naklejki na '
                                                                                    'przedmiocie',
                                                                                    self)
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
                                                             self)
                                            self.unblurwindow()
                                            self.updateorchcounters()
                                        else:
                                            logbaza.orchchange(self.username, 'Differential during come in', orchid)
                                            Dialog.komunikat('error',
                                                             'Kod naklejony na plakietkę i na przedmiot Różnią się! Jeśli '
                                                             'nie wiesz dlaczego, wezwij szefa ekipy!',
                                                             self)
                                            self.unblurwindow()
                                            self.updateorchcounters()
                                    else:
                                        Dialog.komunikat('warn', orchitemstatustxt, self)
                                        Dialog.komunikat('warn',
                                                         'Nie wczytano kodu z przedmiotu! '
                                                         'Przedmiot nie został przyjety na magazyn!',
                                                         self)
                                        self.unblurwindow()
                                        self.updateorchcounters()
                                else:
                                    Dialog.komunikat('warn',
                                                     'Nie wczytano kodu z przedmiotu! '
                                                     'Przedmiot nie został przyjety na magazyn!',
                                                     self)
                                    self.unblurwindow()
                                    self.updateorchcounters()
                        else:
                            Dialog.komunikat('warn',
                                             'Przerwano proces przyjmowania przedmiotu! '
                                             'Przedmiot nie został przyjety na magazyn!',
                                             self)
                            self.unblurwindow()
                            self.updateorchcounters()
                    else:
                        logbaza.orchchange(self.user, 'Failed Come In Critical', orchid)
                        Dialog.komunikat('error',
                                         'Ten przedmiot nie znajduje się w bazie! '
                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                         self)
                        self.unblurwindow()
                else:
                    Dialog.komunikat('warn', orchstatustxt, self)
                    self.unblurwindow()
                    self.updateorchcounters()
            else:
                Dialog.komunikat('warn',
                                 'Przerwano proces przyjmowania przedmiotu! Przedmiot nie został przyjęty na maagazyn.',
                                 self)
                self.unblurwindow()
                self.updateorchcounters()

    # SLOT Orkiestra - wydanie przedmiotu
    def orchcomeout(self):
        if not (self.loginstatus or self.loginbypass):
            self.blurwindow()
            Dialog.komunikat('warn', 'Musisz być zalogowany aby korzystać z programu!')
            self.unblurwindow()
        else:
            self.blurwindow()
            orchbarcode, orchok = InputDialog.komunikat('barcode', 'Wczytaj kod kreskowy z plakietki uczestnika:', self)
            if orchok:
                orchstatus, orchstatustxt = barcodevalcheck(orchbarcode, 'orch')
                if orchstatus == 0:
                    orchid = barcodetoid(orchbarcode, 'int')
                    if slotbaza.isorchexist(orchid):
                        orchitem = slotbaza.loadorch(orchid)
                        nowyorchitem, ok = OrchEditDialog.comeout(orchitem, self)
                        if ok:
                            if not (nowyorchitem['itemstate']):
                                logbaza.orchchange(self.user, 'Override Trial during come out', orchid)
                                Dialog.komunikat('error',
                                                 'Próbujesz wydać przedmiot, '
                                                 'który już jest wydany z magazynu!'
                                                 'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                                 self)
                                self.unblurwindow()
                            else:
                                orchitembarcode, orchitemok = InputDialog.komunikat('barcode',
                                                                                    'Wczytaj kod kreskowy z naklejki na '
                                                                                    'przedmiocie',
                                                                                    self)
                                if orchitemok:
                                    orchitemstatus, orchitemstatustxt = barcodevalcheck(orchitembarcode, 'orch')
                                    if orchitemstatus == 0:
                                        orchitemid = barcodetoid(orchitembarcode, 'int')
                                        if orchid == orchitemid:
                                            nowyorchitem['itemstate'] = False
                                            nowyorchitem['dateoflastoutcome'] = datetime.datetime.now()
                                            nowyorchitem['useroflastoutcome'] = self.username
                                            slotbaza.saveorch(nowyorchitem)
                                            logbaza.orchchange(self.user, 'Come Out', orchid)
                                            Dialog.komunikat('ok', 'Poprawnie wydano przedmiot ze SLOT Orkiestry', self)
                                            self.unblurwindow()
                                            self.updateorchcounters()
                                        else:
                                            logbaza.orchchange(self.username, 'Differential during come out', orchid)
                                            Dialog.komunikat('error',
                                                             'Kod naklejony na plakietkę i na przedmiot Różnią się! Jeśli '
                                                             'nie wiesz dlaczego, wezwij szefa ekipy!',
                                                             self)
                                            self.unblurwindow()
                                            self.updateorchcounters()
                                    else:
                                        Dialog.komunikat('warn', orchitemstatustxt, self)
                                        Dialog.komunikat('warn',
                                                         'Nie wczytano kodu z przedmiotu! '
                                                         'Przedmiot nie został wydany z magazynu!',
                                                         self)
                                        self.unblurwindow()
                                        self.updateorchcounters()
                                else:
                                    Dialog.komunikat('warn',
                                                     'Nie wczytano kodu z przedmiotu! '
                                                     'Przedmiot nie został wydany z magazynu!',
                                                     self)
                                    self.unblurwindow()
                                    self.updateorchcounters()
                        else:
                            Dialog.komunikat('warn',
                                             'Przerwano proces wydawania przedmiotu! '
                                             'Przedmiot nie został wydany z magazynu!',
                                             self)
                            self.unblurwindow()
                            self.updateorchcounters()
                    else:
                        logbaza.orchchange(self.user, 'Failed Come Out Critical', orchid)
                        Dialog.komunikat('error',
                                         'Ten przedmiot nie znajduje się w bazie! '
                                         'Jeśli nie wiesz dlaczego, wezwij szefa ekipy!',
                                         self)
                        self.unblurwindow()
                else:
                    Dialog.komunikat('warn', orchstatustxt, self)
                    self.unblurwindow()
                    self.updateorchcounters()
            else:
                Dialog.komunikat('warn',
                                 'Przerwano proces wydawania przedmiotu! Przedmiot nie został wydany z magazynu!',
                                 self)
                self.unblurwindow()
                self.updateorchcounters()

    # Funkcja rysująca obszary, po wcześniejszym wyczyszczeniu sceny
    def rysujobszary(self):
        self.wyczyscscene()
        obszary = slotbaza.getareageometries()  # Wczytanie geometrii obszarów

        # Wybór czcionki
        font = QFont()
        font.setPixelSize(18)
        font.setBold(True)

        for obszar in obszary:
            grupa = QGraphicsItemGroup()  # Tworzy grupę

            # Stworzenie prostokąta
            prosto = QGraphicsRectItem(QRectF(obszar['posx'], obszar['posy'], obszar['sizex'], obszar['sizey']))
            gradient = QLinearGradient(QPoint(obszar['posx'], obszar['posy']),
                                       QPoint(obszar['posx'], obszar['posy'] + obszar['sizey']))
            gradient.setColorAt(0, QColor('#220087FF'))
            gradient.setColorAt(1, QColor('#440048FF'))
            prosto.setBrush(gradient)

            # Stworzenie etykiety
            etykieta = QGraphicsTextItem(str(obszar['areaid']))
            etykieta.setDefaultTextColor(Qt.white)
            etykieta.setFont(font)
            etykieta_br = etykieta.boundingRect()
            etykieta.setPos(obszar['posx'] + obszar['sizex'] / 2 - etykieta_br.width() / 2,
                            obszar['posy'] + obszar['sizey'] / 2 - etykieta_br.height() / 2)

            # Dodanie prostokąta i etykiety do grupy
            grupa.addToGroup(prosto)
            grupa.addToGroup(etykieta)

            grupa.setFlag(QGraphicsItem.ItemIsMovable, True)  # Ustawienie grupy jako możliwej do przesunięcia
            self.scena.addItem(grupa)  # dodanie grupy do sceny

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
