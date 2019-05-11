import datetime

from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtCore import Qt
from peewee import *

db_filename = 'test.db'

baza = SqliteDatabase(db_filename)
qbaza = QSqlDatabase("QSQLITE")
qbaza.setDatabaseName(db_filename)

if qbaza.open():
    print('Udalo sie połączyć z bazą')
else:
    print('Nie udało sie połączyć z bazą')


class ModelBazy(Model):
    class Meta:
        database = baza


class Area(ModelBazy):
    areaid = IntegerField(unique=True, primary_key=True)
    areabarcode = CharField(unique=True)
    areaname = CharField(default='')
    posx = FloatField(default=0)
    posy = FloatField(default=0)
    sizex = FloatField(default=0)
    sizey = FloatField(default=0)
    userofcreation = CharField(default='')
    dateofcreation = DateTimeField(default=0)
    person1 = CharField(default='')
    person2 = CharField(default='')
    person3 = CharField(default='')
    tel1 = CharField(default='')
    tel2 = CharField(default='')
    tel3 = CharField(default='')
    comments = TextField(default='')


class Item(ModelBazy):
    itemid = IntegerField(unique=True, primary_key=True)
    itembarcode = CharField(unique=True)
    itemname = CharField(default='')
    itemstate = BooleanField(default=True)
    dateoffirstincome = DateTimeField(default='')
    useroffirstincome = CharField(default='')
    dateoflastincome = DateTimeField(default='')
    useroflastincome = CharField(default='')
    dateoflastoutcome = DateTimeField(default='')
    useroflastoutcome = CharField(default='')
    itemcomments = TextField(default='')
    areaass = ForeignKeyField(Area, backref='itemsinside')


class User(ModelBazy):
    usertype = CharField(default='user')
    firstname = CharField(default='')
    secondname = CharField(default='')
    shortname = CharField(default='')
    login = CharField(unique=True)
    password = CharField()
    joindate = DateTimeField()
    lastlogindate = DateTimeField(default='')
    lastlogoutdate = DateTimeField(default='')


class Orchestra(ModelBazy):
    orchestraid = IntegerField(unique=True, primary_key=True)
    orchestrabarcode = CharField(unique=True)
    firstname = CharField(default='')
    secondname = CharField(default='')
    itemname = CharField(default='')
    itemcomments = TextField(default='')
    itemstate = BooleanField(default=False)
    dateofcreation = DateTimeField(default='')
    userofcreation = CharField(default='')
    dateoffirstincome = DateTimeField(default='')
    useroffirstincome = CharField(default='')
    dateoflastincome = DateTimeField(default='')
    useroflastincome = CharField(default='')
    dateoflastoutcome = DateTimeField(default='')
    useroflastoutcome = CharField(default='')


# Stworzenie tabel - wykonywac tylko raz!!!
def openconnection():
    baza.connect()


# Otwarcie połączenia z bazą
def closeconnection():
    baza.close()


# Stworzenie tablic
def createtables():
    openconnection()
    baza.create_tables([Area, Item, User, Orchestra])
    closeconnection()


# Sprawdzenie czy obszar o podanym ID istnieje
def isareaexist(areaid):
    try:
        Area.get_by_id(areaid)
        return True
    except:
        return False


# Sprawdzenie czy przedmiot o podanym ID istnieje
def isitemexist(itemid):
    try:
        Item.get_by_id(itemid)
        return True
    except:
        return False


def isorchexist(orchid):
    try:
        Orchestra.get_by_id(orchid)
        return True
    except:
        return False


# Stworenie obszaru
def createarea(areaid, areabarcode, areaname, posx, posy, sizex, sizey, user):
    if isareaexist(areaid):
        pass
    else:
        Area.create(areaid=areaid, areabarcode=areabarcode, areaname=areaname, posx=posx, posy=posy, sizex=sizex,
                    sizey=sizey,
                    dateofcreation=datetime.datetime.now(), userofcreation=user)


# Wczytanie danych obszaru
def loadarea(areaid):
    if isareaexist(areaid):
        area = Area.get_by_id(areaid)
        areadict = {}
        areadict['areaid'] = area.areaid
        areadict['areabarcode'] = area.areabarcode
        areadict['areaname'] = area.areaname
        areadict['posx'] = area.posx
        areadict['posy'] = area.posy
        areadict['sizex'] = area.sizex
        areadict['sizey'] = area.sizey
        areadict['userofcreation'] = area.userofcreation
        areadict['dateofcreation'] = area.dateofcreation
        areadict['person1'] = area.person1
        areadict['person2'] = area.person2
        areadict['person3'] = area.person3
        areadict['tel1'] = area.tel1
        areadict['tel2'] = area.tel2
        areadict['tel3'] = area.tel3
        areadict['comments'] = area.comments
        return areadict
    else:
        pass


# Zapisanie danych obszaru
def savearea(areadict):
    if isareaexist(areadict['areaid']):
        area = Area.get_by_id(areadict['areaid'])
        area.areaid = areadict['areaid']
        area.areabarcode = areadict['areabarcode']
        area.areaname = areadict['areaname']
        area.posx = areadict['posx']
        area.posy = areadict['posy']
        area.sizex = areadict['sizex']
        area.sizey = areadict['sizey']
        area.userofcreation = areadict['userofcreation']
        area.dateofcreation = areadict['dateofcreation']
        area.person1 = areadict['person1']
        area.person2 = areadict['person2']
        area.person3 = areadict['person3']
        area.tel1 = areadict['tel1']
        area.tel2 = areadict['tel2']
        area.tel3 = areadict['tel3']
        area.comments = areadict['comments']
        area.save()
    else:
        pass


# Wczytanie geometrii obszarów
def getareageometries():
    areadict = {}
    areadictlist = []
    for area in Area.select():
        areadict['areaid'] = area.areaid
        areadict['areaname'] = area.areaname
        areadict['posx'] = area.posx
        areadict['posy'] = area.posy
        areadict['sizex'] = area.sizex
        areadict['sizey'] = area.sizey
        areadictlist.append(areadict)
        areadict = {}
    return areadictlist


# Stworzenie przedmiotu
def createitem(itemid, itembarcode, itemname, areaass):
    if isitemexist(itemid):
        pass
    else:
        if isareaexist(areaass):
            Item.create(itemid=itemid, itembarcode=itembarcode, itemname=itemname, areaass=areaass)
        else:
            pass


# Wczytanie danych przedmiotu
def loaditem(itemid):
    if isitemexist(itemid):
        item = Item.get_by_id(itemid)
        itemdict = {}
        itemdict['itemid'] = item.itemid
        itemdict['itembarcode'] = item.itembarcode
        itemdict['itemname'] = item.itemname
        itemdict['itemstate'] = item.itemstate
        itemdict['dateoffirstincome'] = item.dateoffirstincome
        itemdict['useroffirstincome'] = item.useroffirstincome
        itemdict['dateoflastincome'] = item.dateoflastincome
        itemdict['useroflastincome'] = item.useroflastincome
        itemdict['dateoflastoutcome'] = item.dateoflastoutcome
        itemdict['useroflastoutcome'] = item.useroflastoutcome
        itemdict['itemcomments'] = item.itemcomments
        itemdict['areaass'] = item.areaass
        return itemdict
    else:
        pass


# zapisanie danych przedmiotu
def saveitem(itemdict):
    if isitemexist(itemdict['itemid']):
        item = Item.get_by_id(itemdict['itemid'])
        item.itemid = itemdict['itemid']
        item.itembarcode = itemdict['itembarcode']
        item.itemname = itemdict['itemname']
        item.itemstate = itemdict['itemstate']
        item.dateoffirstincome = itemdict['dateoffirstincome']
        item.useroffirstincome = itemdict['useroffirstincome']
        item.dateoflastincome = itemdict['dateoflastincome']
        item.useroflastincome = itemdict['useroflastincome']
        item.dateoflastoutcome = itemdict['dateoflastoutcome']
        item.useroflastoutcome = itemdict['useroflastoutcome']
        item.itemcomments = itemdict['itemcomments']
        item.areaass = itemdict['areaass']
        item.save()
    else:
        pass


# wczytanie listy wszystkich obszarów
def loadallareas():
    areadict = {}
    areadictlist = []
    for area in Area.select():
        areadict['areaid'] = area.areaid
        areadict['areabarcode'] = area.areabarcode
        areadict['areaname'] = area.areaname
        areadict['posx'] = area.posx
        areadict['posy'] = area.posy
        areadict['sizex'] = area.sizex
        areadict['sizey'] = area.sizey
        areadict['userofcreation'] = area.userofcreation
        areadict['dateofcreation'] = area.dateofcreation
        areadict['person1'] = area.person1
        areadict['person2'] = area.person2
        areadict['person3'] = area.person3
        areadict['tel1'] = area.tel1
        areadict['tel2'] = area.tel2
        areadict['tel3'] = area.tel3
        areadict['comments'] = area.comments
        areadictlist.append(areadict)
        areadict = {}
    return areadictlist


# wczytanie listy wszystkich przedmiotów
def loadallitems():
    itemdict = {}
    itemdictlist = []
    for item in Item.select():
        itemdict['itemid'] = item.itemid
        itemdict['itembarcode'] = item.itembarcode
        itemdict['itemname'] = item.itemname
        itemdict['itemstate'] = item.itemstate
        itemdict['dateoffirstincome'] = item.dateoffirstincome
        itemdict['useroffirstincome'] = item.useroffirstincome
        itemdict['dateoflastincome'] = item.dateoflastincome
        itemdict['useroflastincome'] = item.useroflastincome
        itemdict['dateoflastoutcome'] = item.dateoflastoutcome
        itemdict['useroflastoutcome'] = item.useroflastoutcome
        itemdict['itemcomments'] = item.itemcomments
        itemdict['areaass'] = item.areaass
        itemdictlist.append(itemdict)
        itemdict = {}
    return itemdictlist


# wczytanie listy przedmiotow z danego obszaru
def loaditemsinarea(areaid):
    itemdict = {}
    itemdictlist = []
    for item in Item.select().where(Item.areaass == areaid):
        itemdict['itemid'] = item.itemid
        itemdict['itembarcode'] = item.itembarcode
        itemdict['itemname'] = item.itemname
        itemdict['itemstate'] = item.itemstate
        itemdict['dateoffirstincome'] = item.dateoffirstincome
        itemdict['useroffirstincome'] = item.useroffirstincome
        itemdict['dateoflastincome'] = item.dateoflastincome
        itemdict['useroflastincome'] = item.useroflastincome
        itemdict['dateoflastoutcome'] = item.dateoflastoutcome
        itemdict['useroflastoutcome'] = item.useroflastoutcome
        itemdict['itemcomments'] = item.itemcomments
        itemdict['areaass'] = item.areaass
        itemdictlist.append(itemdict)
        itemdict = {}
    return itemdictlist


def createorch(orchid, orchbarcode, user):
    if isorchexist(orchid):
        pass
    else:
        Orchestra.create(orchestraid=orchid, orchestrabarcode=orchbarcode, userofcreation=user,
                         dateofcreation=datetime.datetime.now())


def loadorch(orchid):
    if isorchexist(orchid):
        orch = Orchestra.get_by_id(orchid)
        orchdict = {}
        orchdict['orchid'] = orch.orchestraid
        orchdict['orchbarcode'] = orch.orchestrabarcode
        orchdict['firstname'] = orch.firstname
        orchdict['lastname'] = orch.secondname
        orchdict['itemname'] = orch.itemname
        orchdict['itemcomments'] = orch.itemcomments
        orchdict['itemstate'] = orch.itemstate
        orchdict['dateofcreation'] = orch.dateofcreation
        orchdict['userofcreation'] = orch.userofcreation
        orchdict['dateoffirstincome'] = orch.dateoffirstincome
        orchdict['useroffirstincome'] = orch.useroffirstincome
        orchdict['dateoflastincome'] = orch.dateoflastincome
        orchdict['useroflastincome'] = orch.useroflastincome
        orchdict['dateoflastoutcome'] = orch.dateoflastoutcome
        orchdict['useroflastoutcome'] = orch.useroflastoutcome
        return orchdict
    else:
        pass


def saveorch(orchdict):
    if isorchexist(orchdict['orchid']):
        orch = Orchestra.get_by_id(orchdict['orchid'])
        orch.orchestraid = orchdict['orchid']
        orch.orchestrabarcode = orchdict['orchbarcode']
        orch.firstname = orchdict['firstname']
        orch.secondname = orchdict['lastname']
        orch.itemname = orchdict['itemname']
        orch.itemcomments = orchdict['itemcomments']
        orch.itemstate = orchdict['itemstate']
        orch.dateofcreation = orchdict['dateofcreation']
        orch.userofcreation = orchdict['userofcreation']
        orch.dateoffirstincome = orchdict['dateoffirstincome']
        orch.useroffirstincome = orchdict['useroffirstincome']
        orch.dateoflastincome = orchdict['dateoflastincome']
        orch.useroflastincome = orchdict['useroflastincome']
        orch.dateoflastoutcome = orchdict['dateoflastoutcome']
        orch.useroflastoutcome = orchdict['useroflastoutcome']
        orch.save()
    else:
        pass


def orchcountall():
    lista = Orchestra.select()
    dlugosc = len(lista)
    return (dlugosc)


def orchcountpresent():
    lista = Orchestra.select().where(Orchestra.itemstate == True)
    dlugosc = len(lista)
    return (dlugosc)


# stworzenie nowego użytkownika
def createuser(usertype, login, password):
    if isuserexist(login):
        pass
    else:
        User.create(usertype=usertype, login=login, password=password, joindate=datetime.datetime.now())


# wczytanie danych użytkownika
def loaduser(login):
    if isuserexist(login):
        user = User.get(User.login == login)
        userdict = {}
        userdict['usertype'] = user.usertype
        userdict['firstname'] = user.firstname
        userdict['secondname'] = user.secondname
        userdict['shortname'] = user.shortname
        userdict['login'] = user.login
        userdict['password'] = user.password
        userdict['joindate'] = user.joindate
        userdict['lastlogindate'] = user.lastlogindate
        userdict['lastlogoutdate'] = user.lastlogoutdate
        return userdict
    else:
        pass


# zapisanie danych uzytkownika
def saveuser(userdict):
    if isuserexist(userdict['login']):
        user = User.get(User.login == userdict['login'])
        user.usertype = userdict['usertype']
        user.firstname = userdict['firstname']
        user.secondname = userdict['secondname']
        user.shortname = userdict['shortname']
        user.login = userdict['login']
        user.password = userdict['password']
        user.joindate = userdict['joindate']
        user.lastlogindate = userdict['lastlogindate']
        user.lastlogoutdate = userdict['lastlogoutdate']
        user.save()
    else:
        pass


# sprawdzenie czy uzytkownik o podanym loginie istnieje w bazie
def isuserexist(login):
    try:
        User.get(User.login == login)
        return True
    except:
        return False


# funkcja weryfikująca logowanie użytkonika
def loginvalidate(login, password):
    if isuserexist(login):
        user = User.get(User.login == login)
        if user.password == password:
            status = {'login': True, 'usertype': user.usertype}
        else:
            status = {'login': False, 'usertype': None}
    else:
        status = {'login': False, 'usertype': None}
    return status


# pobranie listy uzytkownikow
def userlist():
    userdict = {}
    userdictlist = []
    for user in User.select():
        userdict['login'] = user.login
        userdict['firstname'] = user.firstname
        userdict['secondname'] = user.secondname
        userdict['shortname'] = user.shortname
        userdictlist.append(userdict)
        userdict = {}
    return userdictlist


# Klasa pomocnicza - wyłączona edycji niektórych kolumn
class AreaQSqlTableModel(QSqlTableModel):
    def __init__(self, parent=None, db=QSqlDatabase()):
        super(AreaQSqlTableModel, self).__init__(parent, db)

    def flags(self, index):
        if (index.column() == 0):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 1):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 7):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 8):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        else:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


class ItemQSqlTableModel(QSqlTableModel):
    def __init__(self, parent=None, db=QSqlDatabase()):
        super(ItemQSqlTableModel, self).__init__(parent, db)

    def flags(self, index):
        if (index.column() == 0):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 1):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 7):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 8):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 9):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 10):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 11):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 12):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 13):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        elif (index.column() == 15):
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
        else:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable


# funkcja zwracająca model tablicy 'area' zgodny z Qt
def getqareamodel():
    model = AreaQSqlTableModel(None, qbaza)
    model.setTable('area')
    model.setHeaderData(0, Qt.Horizontal, 'No')
    model.setHeaderData(1, Qt.Horizontal, 'Kod kreskowy')
    model.setHeaderData(2, Qt.Horizontal, 'Nazwa')
    model.setHeaderData(7, Qt.Horizontal, 'Kto stworzył')
    model.setHeaderData(8, Qt.Horizontal, 'Kiedy stworzony')
    model.setHeaderData(9, Qt.Horizontal, 'Osoba kontaktowa')
    model.setHeaderData(10, Qt.Horizontal, 'Osoba kontaktowa')
    model.setHeaderData(11, Qt.Horizontal, 'Osoba kontaktowa')
    model.setHeaderData(12, Qt.Horizontal, 'Telefon')
    model.setHeaderData(13, Qt.Horizontal, 'Telefon')
    model.setHeaderData(14, Qt.Horizontal, 'Telefon')
    model.setHeaderData(15, Qt.Horizontal, 'Uwagi')
    model.select()
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)

    return model


def getqitemmodel(areaid):
    model = ItemQSqlTableModel(None, qbaza)
    model.setTable('item')
    query = 'areaass_id = ' + str(areaid)
    model.setFilter(query)
    model.setHeaderData(0, Qt.Horizontal, 'No')
    model.setHeaderData(1, Qt.Horizontal, 'Kod kreskowy')
    model.setHeaderData(2, Qt.Horizontal, 'Nazwa')
    model.setHeaderData(3, Qt.Horizontal, 'Na magazynie?')
    model.setHeaderData(4, Qt.Horizontal, 'Kiedy stworzony')
    model.setHeaderData(5, Qt.Horizontal, 'Kto stworzył')
    model.setHeaderData(6, Qt.Horizontal, 'Ostatnio przyjęty')
    model.setHeaderData(7, Qt.Horizontal, 'Ostatnio przyjął')
    model.setHeaderData(8, Qt.Horizontal, 'Ostatnio wydany')
    model.setHeaderData(9, Qt.Horizontal, 'Ostatnio wydał')
    model.setHeaderData(10, Qt.Horizontal, 'Uwagi')
    model.setHeaderData(11, Qt.Horizontal, 'Obszar')
    model.select()
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)

    return model


def getqitemsmodel():
    model = ItemQSqlTableModel(None, qbaza)
    model.setTable('item')
    model.setHeaderData(0, Qt.Horizontal, 'No')
    model.setHeaderData(1, Qt.Horizontal, 'Kod kreskowy')
    model.setHeaderData(2, Qt.Horizontal, 'Nazwa')
    model.setHeaderData(7, Qt.Horizontal, 'Na magazynie?')
    model.setHeaderData(8, Qt.Horizontal, 'Kiedy stworzony')
    model.setHeaderData(9, Qt.Horizontal, 'Kto stworzył')
    model.setHeaderData(10, Qt.Horizontal, 'Ostatnio przyjęty')
    model.setHeaderData(11, Qt.Horizontal, 'Ostatnio przyjął')
    model.setHeaderData(12, Qt.Horizontal, 'Ostatnio wydany')
    model.setHeaderData(13, Qt.Horizontal, 'Ostatnio wydał')
    model.setHeaderData(14, Qt.Horizontal, 'Uwagi')
    model.setHeaderData(15, Qt.Horizontal, 'Obszar')
    model.select()
    model.setEditStrategy(QSqlTableModel.OnManualSubmit)

    return model
