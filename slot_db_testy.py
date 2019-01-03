import os
import slotbaza
import json

#
# slotmagazyn_db_interface.Item.create(itemid=1,itembarcode='201920001',itemname='Obiekt',areaass=1,itemstate=1,dateoffirstincome='',dateoflastincome=datetime.datetime.now(),dateoflastoutcome=datetime.datetime.now())
# slotmagazyn_db_interface.Item.create(itemid=2,itembarcode='201920002',itemname='Gitara',areaass=1,itemstate=1,dateoffirstincome='',dateoflastincome=datetime.datetime.now(),dateoflastoutcome=datetime.datetime.now())
# slotmagazyn_db_interface.Item.create(itemid=3,itembarcode='201920003',itemname='Pianino',areaass=2,itemstate=1,dateoffirstincome='',dateoflastincome=datetime.datetime.now(),dateoflastoutcome=datetime.datetime.now())
#


for q in slotbaza.loaditemsinarea(3):
    print(q)

