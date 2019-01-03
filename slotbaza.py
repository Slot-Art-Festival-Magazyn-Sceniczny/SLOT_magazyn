import os
import datetime
from peewee import *

db_filename = 'test.db'

baza = SqliteDatabase(db_filename)


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
    usertype = CharField()
    firstname = CharField()
    secondname = CharField()
    shortname = CharField()
    login = CharField(unique=True)
    password = CharField()
    joindate = DateTimeField()
    lastlogindate = DateTimeField()
    lastlogoutdate = DateTimeField()


class Orchestra(ModelBazy):
    orchestraID = IntegerField(unique=True)
    orchestrabarcode = CharField(unique=True)
    firstname = CharField()
    secondname = CharField()
    itemname = CharField()
    itemstate = BooleanField()


# Stworzenie tabel - wykonywac tylko raz!!!
def openconnection():
    baza.connect()


# Otwarcie połączenia z bazą
def closeconnection():
    baza.close()


# Zamkniecie połączenia z bazą
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


# Stworenie obszaru
def createarea(areaid, areabarcode, posx, posy, sizex, sizey, user):
    if isareaexist(areaid):
        pass
    else:
        Area.create(areaid=areaid, areabarcode=areabarcode, posx=posx, posy=posy, sizex=sizex, sizey=sizey,
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
        iremdict = {}
        iremdict['itemid'] = item.itemid
        iremdict['itembarcode'] = item.itembarcode
        iremdict['itemname'] = item.itemname
        iremdict['itemstate'] = item.itemstate
        iremdict['dateoffirstincome'] = item.dateoffirstincome
        iremdict['useroffirstincome'] = item.useroffirstincome
        iremdict['dateoflastincome'] = item.dateoflastincome
        iremdict['useroflastincome'] = item.useroflastincome
        iremdict['dateoflastoutcome'] = item.dateoflastoutcome
        iremdict['useroflastoutcome'] = item.useroflastoutcome
        iremdict['itemcomments'] = item.itemcomments
        iremdict['areaass'] = item.areaass
        return iremdict
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
