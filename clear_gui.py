# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clear_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1013, 963)
        MainWindow.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 500))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("QDialog\n"
"{background-color: white}\n"
"\n"
"Line\n"
"{color: #88FFFFFF}\n"
"\n"
"\n"
"QWidget#centralwidget\n"
"{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #B721FF, stop:1 #21D4FD);}\n"
"\n"
"QGraphicsView\n"
"{background-color: #44FFFFFF}\n"
"\n"
"QFrame#frm_leftside\n"
"{background-color: #44FFFFFF}\n"
"\n"
"QFrame#frm_login\n"
"{background-color: #44FFFFFF}\n"
"\n"
"QPushButton\n"
"{background-color: #00FFFFFF; color: #FFFFFFFF; border-style: none; border-color: #AA000000; border-width: 0px; border-radius: 0px;}\n"
"\n"
"QPushButton:hover\n"
"{background-color: #55000000; color: #FFFFFFFF}\n"
"\n"
"QPushButton:pressed\n"
"{background-color: #AA000000}\n"
"\n"
"QPushButton#btn_listofareas\n"
"{Text-align:left; padding-left: 30px;}\n"
"\n"
"QPushButton#btn_addarea\n"
"{Text-align:left; padding-left: 30px;}\n"
"\n"
"QPushButton#btn_editarea\n"
"{Text-align:left; padding-left: 30px;}\n"
"\n"
"QPushButton#btn_finditem\n"
"{Text-align:left; padding-left: 30px;}\n"
"\n"
"QPushButton#btn_lookinside\n"
"{Text-align:left; padding-left: 30px;}\n"
"\n"
"QPushButton#btn_comein\n"
"{Text-align:left; padding-left: 30px;}\n"
"\n"
"QPushButton#btn_comeout\n"
"{Text-align:left; padding-left: 30px;}\n"
"\n"
"QPushButton#btn_orchestra\n"
"{Text-align:left; padding-left: 30px;}\n"
"\n"
"QPushButton#btn_exit\n"
"{Text-align:left; padding-left: 30px;}\n"
"\n"
"QPushButton:hover#btn_finditem\n"
"{background-color: #550065FF}\n"
"\n"
"QPushButton:hover#btn_comein\n"
"{background-color: #5500AE37}\n"
"\n"
"QPushButton:hover#btn_comeout\n"
"{background-color: #55C60018}\n"
"\n"
"QPushButton:hover#btn_lookinside\n"
"{background-color: #55FF9D00}\n"
"\n"
"QPushButton:hover#btn_orchestra\n"
"{background-color: #558400FF}\n"
"\n"
"QPushButton:pressed#btn_finditem\n"
"{background-color: #AA0065FF}\n"
"\n"
"QPushButton:pressed#btn_comein\n"
"{background-color: #AA00AE37}\n"
"\n"
"QPushButton:pressed#btn_comeout\n"
"{background-color: #AAC60018}\n"
"\n"
"QPushButton:pressed#btn_lookinside\n"
"{background-color: #AAFF9D00}\n"
"\n"
"QPushButton:pressed#btn_orchestra\n"
"{background-color: #AA8400FF}\n"
"\n"
"QPushButton#btn_exit\n"
"{background-color: #55C60018}\n"
"\n"
"QPushButton:hover#btn_exit\n"
"{background-color: #AAC60018}\n"
"\n"
"QPushButton:pressed#btn_exit\n"
"{background-color: #FFC60018}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lt_central = QtWidgets.QHBoxLayout()
        self.lt_central.setSpacing(0)
        self.lt_central.setObjectName("lt_central")
        self.frm_leftside = QtWidgets.QFrame(self.centralwidget)
        self.frm_leftside.setMinimumSize(QtCore.QSize(260, 0))
        self.frm_leftside.setMaximumSize(QtCore.QSize(260, 16777215))
        self.frm_leftside.setStyleSheet("")
        self.frm_leftside.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_leftside.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frm_leftside.setLineWidth(0)
        self.frm_leftside.setObjectName("frm_leftside")
        self.lt_leftside = QtWidgets.QVBoxLayout(self.frm_leftside)
        self.lt_leftside.setContentsMargins(0, 0, 0, 0)
        self.lt_leftside.setSpacing(6)
        self.lt_leftside.setObjectName("lt_leftside")
        self.frm_logo = QtWidgets.QFrame(self.frm_leftside)
        self.frm_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frm_logo.setLineWidth(0)
        self.frm_logo.setObjectName("frm_logo")
        self.lt_logo = QtWidgets.QGridLayout(self.frm_logo)
        self.lt_logo.setContentsMargins(0, 0, 0, 0)
        self.lt_logo.setSpacing(0)
        self.lt_logo.setObjectName("lt_logo")
        self.label_2 = QtWidgets.QLabel(self.frm_logo)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/images/LOGO.png"))
        self.label_2.setObjectName("label_2")
        self.lt_logo.addWidget(self.label_2, 0, 0, 1, 1)
        self.lt_leftside.addWidget(self.frm_logo)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.lt_leftside.addItem(spacerItem)
        self.frm_login = QtWidgets.QFrame(self.frm_leftside)
        self.frm_login.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_login.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frm_login.setLineWidth(0)
        self.frm_login.setObjectName("frm_login")
        self.lt_login = QtWidgets.QVBoxLayout(self.frm_login)
        self.lt_login.setContentsMargins(0, 0, 0, 6)
        self.lt_login.setSpacing(6)
        self.lt_login.setObjectName("lt_login")
        self.frm_loginbuttons = QtWidgets.QFrame(self.frm_login)
        self.frm_loginbuttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_loginbuttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_loginbuttons.setObjectName("frm_loginbuttons")
        self.lt_loginbuttons = QtWidgets.QHBoxLayout(self.frm_loginbuttons)
        self.lt_loginbuttons.setContentsMargins(0, 0, 0, 0)
        self.lt_loginbuttons.setSpacing(0)
        self.lt_loginbuttons.setObjectName("lt_loginbuttons")
        self.btn_login = QtWidgets.QPushButton(self.frm_loginbuttons)
        self.btn_login.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setFlat(False)
        self.btn_login.setObjectName("btn_login")
        self.lt_loginbuttons.addWidget(self.btn_login)
        self.login_line = QtWidgets.QFrame(self.frm_loginbuttons)
        self.login_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.login_line.setObjectName("login_line")
        self.lt_loginbuttons.addWidget(self.login_line)
        self.btn_logout = QtWidgets.QPushButton(self.frm_loginbuttons)
        self.btn_logout.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setFlat(False)
        self.btn_logout.setObjectName("btn_logout")
        self.lt_loginbuttons.addWidget(self.btn_logout)
        self.lt_login.addWidget(self.frm_loginbuttons)
        self.loginstatus = QtWidgets.QLabel(self.frm_login)
        self.loginstatus.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.loginstatus.setFont(font)
        self.loginstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.loginstatus.setObjectName("loginstatus")
        self.lt_login.addWidget(self.loginstatus)
        self.lt_leftside.addWidget(self.frm_login)
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.lt_leftside.addItem(spacerItem1)
        self.frm_buttons = QtWidgets.QFrame(self.frm_leftside)
        self.frm_buttons.setStyleSheet("")
        self.frm_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_buttons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frm_buttons.setLineWidth(0)
        self.frm_buttons.setObjectName("frm_buttons")
        self.lt_buttons = QtWidgets.QVBoxLayout(self.frm_buttons)
        self.lt_buttons.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.lt_buttons.setContentsMargins(0, 0, 0, 0)
        self.lt_buttons.setSpacing(0)
        self.lt_buttons.setObjectName("lt_buttons")
        self.btn_listofareas = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_listofareas.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_listofareas.setFont(font)
        self.btn_listofareas.setAutoFillBackground(False)
        self.btn_listofareas.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/buttons/btn_listofareas_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_listofareas.setIcon(icon)
        self.btn_listofareas.setIconSize(QtCore.QSize(24, 24))
        self.btn_listofareas.setFlat(False)
        self.btn_listofareas.setObjectName("btn_listofareas")
        self.lt_buttons.addWidget(self.btn_listofareas)
        self.btn_addarea = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_addarea.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_addarea.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/buttons/btn_addarea_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_addarea.setIcon(icon1)
        self.btn_addarea.setIconSize(QtCore.QSize(24, 24))
        self.btn_addarea.setFlat(False)
        self.btn_addarea.setObjectName("btn_addarea")
        self.lt_buttons.addWidget(self.btn_addarea)
        self.btn_editarea = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_editarea.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_editarea.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/buttons/btn_editarea_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editarea.setIcon(icon2)
        self.btn_editarea.setIconSize(QtCore.QSize(24, 24))
        self.btn_editarea.setAutoRepeat(False)
        self.btn_editarea.setFlat(False)
        self.btn_editarea.setObjectName("btn_editarea")
        self.lt_buttons.addWidget(self.btn_editarea)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.lt_buttons.addItem(spacerItem2)
        self.btn_finditem = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_finditem.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_finditem.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/buttons/btn_finditem_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_finditem.setIcon(icon3)
        self.btn_finditem.setIconSize(QtCore.QSize(24, 24))
        self.btn_finditem.setFlat(False)
        self.btn_finditem.setObjectName("btn_finditem")
        self.lt_buttons.addWidget(self.btn_finditem)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.lt_buttons.addItem(spacerItem3)
        self.btn_lookinside = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_lookinside.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_lookinside.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/buttons/btn_lookinside_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_lookinside.setIcon(icon4)
        self.btn_lookinside.setIconSize(QtCore.QSize(24, 24))
        self.btn_lookinside.setFlat(False)
        self.btn_lookinside.setObjectName("btn_lookinside")
        self.lt_buttons.addWidget(self.btn_lookinside)
        self.btn_comein = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_comein.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_comein.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/buttons/btn_comein_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_comein.setIcon(icon5)
        self.btn_comein.setIconSize(QtCore.QSize(24, 24))
        self.btn_comein.setFlat(False)
        self.btn_comein.setObjectName("btn_comein")
        self.lt_buttons.addWidget(self.btn_comein)
        self.btn_comeout = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_comeout.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_comeout.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/buttons/btn_comeout_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_comeout.setIcon(icon6)
        self.btn_comeout.setIconSize(QtCore.QSize(24, 24))
        self.btn_comeout.setFlat(False)
        self.btn_comeout.setObjectName("btn_comeout")
        self.lt_buttons.addWidget(self.btn_comeout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.lt_buttons.addItem(spacerItem4)
        self.btn_orchestra = QtWidgets.QPushButton(self.frm_buttons)
        self.btn_orchestra.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_orchestra.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/buttons/btn_orchestra_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_orchestra.setIcon(icon7)
        self.btn_orchestra.setIconSize(QtCore.QSize(24, 24))
        self.btn_orchestra.setFlat(False)
        self.btn_orchestra.setObjectName("btn_orchestra")
        self.lt_buttons.addWidget(self.btn_orchestra)
        self.lt_leftside.addWidget(self.frm_buttons)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.lt_leftside.addItem(spacerItem5)
        self.btn_exit = QtWidgets.QPushButton(self.frm_leftside)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_exit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/images/buttons/btn_exit_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon8)
        self.btn_exit.setIconSize(QtCore.QSize(24, 24))
        self.btn_exit.setObjectName("btn_exit")
        self.lt_leftside.addWidget(self.btn_exit)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.lt_leftside.addItem(spacerItem6)
        self.frm_logo.raise_()
        self.frm_login.raise_()
        self.frm_buttons.raise_()
        self.btn_exit.raise_()
        self.lt_central.addWidget(self.frm_leftside)
        self.frm_rightside = QtWidgets.QFrame(self.centralwidget)
        self.frm_rightside.setMinimumSize(QtCore.QSize(400, 0))
        self.frm_rightside.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frm_rightside.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_rightside.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frm_rightside.setLineWidth(0)
        self.frm_rightside.setObjectName("frm_rightside")
        self.lt_rightside = QtWidgets.QVBoxLayout(self.frm_rightside)
        self.lt_rightside.setContentsMargins(20, 20, 20, 0)
        self.lt_rightside.setSpacing(6)
        self.lt_rightside.setObjectName("lt_rightside")
        self.frm_top = QtWidgets.QFrame(self.frm_rightside)
        self.frm_top.setMinimumSize(QtCore.QSize(0, 0))
        self.frm_top.setStyleSheet("")
        self.frm_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frm_top.setLineWidth(0)
        self.frm_top.setObjectName("frm_top")
        self.lt_rightside.addWidget(self.frm_top)
        self.gr_v = QtWidgets.QGraphicsView(self.frm_rightside)
        self.gr_v.setMinimumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.gr_v.setFont(font)
        self.gr_v.setAutoFillBackground(False)
        self.gr_v.setStyleSheet("")
        self.gr_v.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gr_v.setFrameShadow(QtWidgets.QFrame.Plain)
        self.gr_v.setLineWidth(0)
        self.gr_v.setObjectName("gr_v")
        self.lt_rightside.addWidget(self.gr_v)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.lt_rightside.addItem(spacerItem7)
        self.lt_central.addWidget(self.frm_rightside)
        self.gridLayout.addLayout(self.lt_central, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_login.setText(_translate("MainWindow", "ZALOGUJ"))
        self.btn_logout.setText(_translate("MainWindow", "WYLOGUJ"))
        self.loginstatus.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Niezalogowany</span></p></body></html>"))
        self.btn_listofareas.setText(_translate("MainWindow", "LISTA OBSZARÓW"))
        self.btn_addarea.setText(_translate("MainWindow", "DODAJ OBSZAR"))
        self.btn_editarea.setText(_translate("MainWindow", "EDYTUJ OBSZAR"))
        self.btn_finditem.setText(_translate("MainWindow", "WYSZUKAJ PRZEDMIOT"))
        self.btn_lookinside.setText(_translate("MainWindow", "ZAJRZYJ DO ŚRODKA"))
        self.btn_comein.setText(_translate("MainWindow", "PRZYJMIJ PRZEDMIOT"))
        self.btn_comeout.setText(_translate("MainWindow", "WYDAJ PRZEDMIOT"))
        self.btn_orchestra.setText(_translate("MainWindow", "SLOT ORKIESTRA"))
        self.btn_exit.setText(_translate("MainWindow", "WYJŚCIE"))

import gui_res_rc
