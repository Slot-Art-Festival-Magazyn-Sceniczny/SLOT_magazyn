import datetime

from PyQt5.QtSql import QSqlDatabase
from peewee import *

db_filename = 'logger.db'

baza = SqliteDatabase(db_filename)
qbaza = QSqlDatabase("QSQLITE")
qbaza.setDatabaseName(db_filename)

if qbaza.open():
    print('Udalo sie połączyć z bazą loggera')
else:
    print('Nie udało sie połączyć z bazą loggera')


class ModelBazy(Model):
    class Meta:
        database = baza


class AreaLog(ModelBazy):
    date = DateTimeField(default=0)
    user = CharField(default='')
    areaid = IntegerField()
    change = CharField()
    staredane = CharField(default='')
    nowedane = CharField()


class ItemLog(ModelBazy):
    date = DateTimeField(default=0)
    user = CharField(default='')
    areaid = IntegerField()
    itemid = IntegerField()
    change = CharField()
    staredane = CharField(default='')
    nowedane = CharField()


class OrchLog(ModelBazy):
    date = DateTimeField(default=0)
    user = CharField(default='')
    orchid = IntegerField()
    change = CharField()
    staredane = CharField(default='')
    nowedane = CharField()


class UserLog(ModelBazy):
    date = DateTimeField(default=0)
    user = CharField(default='')
    userid = IntegerField()
    change = CharField()
    staredane = CharField(default='')
    nowedane = CharField()


# Otwarcie połączenia z bazą
def openconnection():
    baza.connect()


# Zamknięcie połączenia z bazą
def closeconnection():
    baza.close()


# Stworzenie tablic
def createtables():
    openconnection()
    baza.create_tables([AreaLog, ItemLog, OrchLog, UserLog])
    closeconnection()


def areachange(user, change, areaid, staredane='', nowedane=''):
    AreaLog.create(date=datetime.datetime.now(), user=user, areaid=areaid, change=change, staredane=staredane,
                   nowedane=nowedane)


def itemchange(user, change, areaid, itemid, staredane='', nowedane=''):
    ItemLog.create(date=datetime.datetime.now(), user=user, areaid=areaid, itemid=itemid, change=change,
                   staredane=staredane, nowedane=nowedane)


def orchchange(user, change, orchid, staredane='', nowedane=''):
    OrchLog.create(date=datetime.datetime.now(), user=user, orchid=orchid, change=change, staredane=staredane,
                   nowedane=nowedane)


def userchange(user, change, staredane='', nowedane=''):
    UserLog.create(date=datetime.datetime.now(), user=user, change=change, staredane=staredane, nowedane=nowedane)
