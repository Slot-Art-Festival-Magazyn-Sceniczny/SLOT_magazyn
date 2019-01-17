# -*- coding: utf-8 -*-

from PyQt5.QtCore import QRect, Qt, QSize, QMetaObject
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QWidget, QGroupBox, QStatusBar, QPushButton, \
    QVBoxLayout, QHBoxLayout, QLabel, QAction, QMenu, QMenuBar, QGraphicsView, QGraphicsScene, QDialog, QLineEdit, \
    QGridLayout, QSizePolicy, QSpacerItem, QLayout


def mainstylesheet():
    stylesheet = "QDialog\n" \
                 "{background-color: white}\n" \
                 "\n" \
                 "QFrame#login_line\n" \
                 "{color: #88FFFFFF}\n" \
                 "\n" \
                 "\n" \
                 "QWidget#centralwidget\n" \
                 "{background-color: " \
                 "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #B721FF, stop:1 #21D4FD);}\n" \
                 "\n" \
                 "QGraphicsView\n" \
                 "{background-color: #44FFFFFF}\n" \
                 "\n" \
                 "QFrame#frm_leftside\n" \
                 "{background-color: #44FFFFFF}\n" \
                 "\n" \
                 "QFrame#frm_login\n" \
                 "{background-color: #44FFFFFF}\n" \
                 "\n" \
                 "QPushButton\n" \
                 "{background-color: #00FFFFFF; color: #FFFFFFFF; " \
                 "border-style: none; border-color: #AA000000; border-width: 0px; border-radius: 0px;}\n" \
                 "\n" \
                 "QPushButton:hover\n" \
                 "{background-color: #55000000; color: #FFFFFFFF}\n" \
                 "\n" \
                 "QPushButton:pressed\n" \
                 "{background-color: #AA000000}\n" \
                 "\n" \
                 "QPushButton#btn_listofareas\n" \
                 "{Text-align:left; padding-left: 30px;}\n" \
                 "\n" \
                 "QPushButton#btn_addarea\n" \
                 "{Text-align:left; padding-left: 30px;}\n" \
                 "\n" \
                 "QPushButton#btn_editarea\n" \
                 "{Text-align:left; padding-left: 30px;}\n" \
                 "\n" \
                 "QPushButton#btn_finditem\n" \
                 "{Text-align:left; padding-left: 30px;}\n" \
                 "\n" \
                 "QPushButton#btn_lookinside\n" \
                 "{Text-align:left; padding-left: 30px;}\n" \
                 "\n" \
                 "QPushButton#btn_comein\n" \
                 "{Text-align:left; padding-left: 30px;}\n" \
                 "\n" \
                 "QPushButton#btn_comeout\n" \
                 "{Text-align:left; padding-left: 30px;}\n" \
                 "\n" \
                 "QPushButton#btn_orchestra\n" \
                 "{Text-align:left; padding-left: 30px;}\n" \
                 "\n" \
                 "QPushButton#btn_exit\n" \
                 "{Text-align:left; padding-left: 30px;}\n" \
                 "\n" \
                 "QPushButton:hover#btn_finditem\n" \
                 "{background-color: #550065FF}\n" \
                 "\n" \
                 "QPushButton:hover#btn_comein\n" \
                 "{background-color: #5500AE37}\n" \
                 "\n" \
                 "QPushButton:hover#btn_comeout\n" \
                 "{background-color: #55C60018}\n" \
                 "\n" \
                 "QPushButton:hover#btn_lookinside\n" \
                 "{background-color: #55FF9D00}\n" \
                 "\n" \
                 "QPushButton:hover#btn_orchestra\n" \
                 "{background-color: #558400FF}\n" \
                 "\n" \
                 "QPushButton:pressed#btn_finditem\n" \
                 "{background-color: #AA0065FF}\n" \
                 "\n" \
                 "QPushButton:pressed#btn_comein\n" \
                 "{background-color: #AA00AE37}\n" \
                 "\n" \
                 "QPushButton:pressed#btn_comeout\n" \
                 "{background-color: #AAC60018}\n" \
                 "\n" \
                 "QPushButton:pressed#btn_lookinside\n" \
                 "{background-color: #AAFF9D00}\n" \
                 "\n" \
                 "QPushButton:pressed#btn_orchestra\n" \
                 "{background-color: #AA8400FF}\n" \
                 "\n" \
                 "QPushButton#btn_exit\n" \
                 "{background-color: #55C60018}\n" \
                 "\n" \
                 "QPushButton:hover#btn_exit\n" \
                 "{background-color: #AAC60018}\n" \
                 "\n" \
                 "QPushButton:pressed#btn_exit\n" \
                 "{background-color: #FFC60018}"
    return stylesheet


class Ui_MainWindow(QMainWindow):
    def setupUI(self):
        self.setmainwindow()
        self.assigncentralwidget()
        self.setframes()
        self.setlayouts()
        self.setwidgets()
        self.settext()
        self.setcentralwidget()

        QMetaObject.connectSlotsByName(self)
        self.setWindowTitle("Magazyn Sceniczny")

        self.showFullScreen()

    def setmainwindow(self):
        self.setWindowModality(Qt.NonModal)
        self.resize(1013, 963)
        self.setMinimumSize(QSize(900, 650))
        self.setWindowOpacity(1.0)
        self.setStyleSheet("")

    def assigncentralwidget(self):
        self.centralwidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(900, 500))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(mainstylesheet())
        self.centralwidget.setObjectName("centralwidget")

    def setframes(self):
        self.frm_leftside = QFrame(self.centralwidget)
        self.frm_leftside.setMinimumSize(QSize(260, 0))
        self.frm_leftside.setMaximumSize(QSize(260, 16777215))
        self.frm_leftside.setStyleSheet("")
        self.frm_leftside.setFrameShape(QFrame.NoFrame)
        self.frm_leftside.setFrameShadow(QFrame.Plain)
        self.frm_leftside.setLineWidth(0)
        self.frm_leftside.setObjectName("frm_leftside")

        self.frm_logo = QFrame(self.frm_leftside)
        self.frm_logo.setFrameShape(QFrame.NoFrame)
        self.frm_logo.setFrameShadow(QFrame.Plain)
        self.frm_logo.setLineWidth(0)
        self.frm_logo.setObjectName("frm_logo")

        self.frm_login = QFrame(self.frm_leftside)
        self.frm_login.setFrameShape(QFrame.NoFrame)
        self.frm_login.setFrameShadow(QFrame.Plain)
        self.frm_login.setLineWidth(0)
        self.frm_login.setObjectName("frm_login")

        self.frm_loginbuttons = QFrame(self.frm_login)
        self.frm_loginbuttons.setFrameShape(QFrame.StyledPanel)
        self.frm_loginbuttons.setFrameShadow(QFrame.Raised)
        self.frm_loginbuttons.setObjectName("frm_loginbuttons")

        self.login_line = QFrame(self.frm_loginbuttons)
        self.login_line.setFrameShadow(QFrame.Plain)
        self.login_line.setFrameShape(QFrame.VLine)
        self.login_line.setObjectName("login_line")

        self.frm_buttons = QFrame(self.frm_leftside)
        self.frm_buttons.setStyleSheet("")
        self.frm_buttons.setFrameShape(QFrame.NoFrame)
        self.frm_buttons.setFrameShadow(QFrame.Plain)
        self.frm_buttons.setLineWidth(0)
        self.frm_buttons.setObjectName("frm_buttons")

        self.frm_rightside = QFrame(self.centralwidget)
        self.frm_rightside.setMinimumSize(QSize(400, 0))
        self.frm_rightside.setMaximumSize(QSize(16777215, 16777215))
        self.frm_rightside.setFrameShape(QFrame.NoFrame)
        self.frm_rightside.setFrameShadow(QFrame.Plain)
        self.frm_rightside.setLineWidth(0)
        self.frm_rightside.setObjectName("frm_rightside")

        self.frm_top = QFrame(self.frm_rightside)
        self.frm_top.setMinimumSize(QSize(0, 0))
        self.frm_top.setStyleSheet("")
        self.frm_top.setFrameShape(QFrame.NoFrame)
        self.frm_top.setFrameShadow(QFrame.Plain)
        self.frm_top.setLineWidth(0)
        self.frm_top.setObjectName("frm_top")

    def setlayouts(self):
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.lt_central = QHBoxLayout()
        self.lt_central.setSpacing(0)
        self.lt_central.setObjectName("lt_central")

        self.lt_leftside = QVBoxLayout(self.frm_leftside)
        self.lt_leftside.setContentsMargins(0, 0, 0, 0)
        self.lt_leftside.setSpacing(6)
        self.lt_leftside.setObjectName("lt_leftside")

        self.lt_logo = QGridLayout(self.frm_logo)
        self.lt_logo.setContentsMargins(0, 0, 0, 0)
        self.lt_logo.setSpacing(0)
        self.lt_logo.setObjectName("lt_logo")

        self.lt_login = QVBoxLayout(self.frm_login)
        self.lt_login.setContentsMargins(0, 0, 0, 6)
        self.lt_login.setSpacing(6)
        self.lt_login.setObjectName("lt_login")

        self.lt_loginbuttons = QHBoxLayout(self.frm_loginbuttons)
        self.lt_loginbuttons.setContentsMargins(0, 0, 0, 0)
        self.lt_loginbuttons.setSpacing(0)
        self.lt_loginbuttons.setObjectName("lt_loginbuttons")

        self.lt_buttons = QVBoxLayout(self.frm_buttons)
        self.lt_buttons.setSizeConstraint(QLayout.SetNoConstraint)
        self.lt_buttons.setContentsMargins(0, 0, 0, 0)
        self.lt_buttons.setSpacing(0)
        self.lt_buttons.setObjectName("lt_buttons")

        self.lt_rightside = QVBoxLayout(self.frm_rightside)
        self.lt_rightside.setContentsMargins(20, 20, 20, 0)
        self.lt_rightside.setSpacing(6)
        self.lt_rightside.setObjectName("lt_rightside")

    def setwidgets(self):
        spacerItem = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)
        spacerItem1 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Maximum)
        spacerItem2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)
        spacerItem3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)
        spacerItem4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)
        spacerItem5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        spacerItem6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        spacerItem7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        font2 = QFont()
        font2.setFamily("Arial")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)

        icon = QIcon()
        icon.addPixmap(QPixmap("images/buttons/btn_listofareas_hover.png"), QIcon.Normal, QIcon.Off)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("images/buttons/btn_addarea_hover.png"), QIcon.Normal, QIcon.Off)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("images/buttons/btn_editarea_hover.png"), QIcon.Normal, QIcon.Off)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("images/buttons/btn_finditem_hover.png"), QIcon.Normal, QIcon.Off)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("images/buttons/btn_lookinside_hover.png"), QIcon.Normal, QIcon.Off)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap("images/buttons/btn_comein_hover.png"), QIcon.Normal, QIcon.Off)
        icon6 = QIcon()
        icon6.addPixmap(QPixmap("images/buttons/btn_comeout_hover.png"), QIcon.Normal, QIcon.Off)
        icon7 = QIcon()
        icon7.addPixmap(QPixmap("images/buttons/btn_orchestra_hover.png"), QIcon.Normal, QIcon.Off)
        icon8 = QIcon()
        icon8.addPixmap(QPixmap("images/buttons/btn_exit_hover.png"), QIcon.Normal, QIcon.Off)

        self.label_2 = QLabel(self.frm_logo)
        self.label_2.setText("")
        self.label_2.setPixmap(QPixmap("images/LOGO.png"))
        self.label_2.setObjectName("label_2")

        self.lt_logo.addWidget(self.label_2, 0, 0, 1, 1)
        self.lt_leftside.addWidget(self.frm_logo)
        self.lt_leftside.addItem(spacerItem)

        self.btn_login = QPushButton(self.frm_loginbuttons)
        self.btn_login.setMinimumSize(QSize(0, 50))
        self.btn_login.setFont(font)
        self.btn_login.setFlat(False)
        self.btn_login.setObjectName("btn_login")

        self.btn_logout = QPushButton(self.frm_loginbuttons)
        self.btn_logout.setMinimumSize(QSize(0, 50))
        self.btn_logout.setFont(font)
        self.btn_logout.setFlat(False)
        self.btn_logout.setObjectName("btn_logout")

        self.lt_loginbuttons.addWidget(self.btn_login)
        self.lt_loginbuttons.addWidget(self.login_line)
        self.lt_loginbuttons.addWidget(self.btn_logout)

        self.lt_login.addWidget(self.frm_loginbuttons)
        self.logstatus = QLabel(self.frm_login)
        self.logstatus.setMinimumSize(QSize(0, 13))
        self.logstatus.setFont(font2)
        self.logstatus.setAlignment(Qt.AlignCenter)
        self.logstatus.setObjectName("logstatus")
        self.lt_login.addWidget(self.logstatus)
        self.lt_leftside.addWidget(self.frm_login)

        self.lt_leftside.addItem(spacerItem1)

        self.btn_listofareas = QPushButton(self.frm_buttons)
        self.btn_listofareas.setMinimumSize(QSize(0, 50))
        self.btn_listofareas.setFont(font)
        self.btn_listofareas.setAutoFillBackground(False)
        self.btn_listofareas.setStyleSheet("")
        self.btn_listofareas.setIcon(icon)
        self.btn_listofareas.setIconSize(QSize(24, 24))
        self.btn_listofareas.setFlat(False)
        self.btn_listofareas.setObjectName("btn_listofareas")
        self.lt_buttons.addWidget(self.btn_listofareas)

        self.btn_addarea = QPushButton(self.frm_buttons)
        self.btn_addarea.setMinimumSize(QSize(0, 50))
        self.btn_addarea.setFont(font)
        self.btn_addarea.setIcon(icon1)
        self.btn_addarea.setIconSize(QSize(24, 24))
        self.btn_addarea.setFlat(False)
        self.btn_addarea.setObjectName("btn_addarea")
        self.lt_buttons.addWidget(self.btn_addarea)

        self.btn_editarea = QPushButton(self.frm_buttons)
        self.btn_editarea.setMinimumSize(QSize(0, 50))
        self.btn_editarea.setFont(font)
        self.btn_editarea.setIcon(icon2)
        self.btn_editarea.setIconSize(QSize(24, 24))
        self.btn_editarea.setAutoRepeat(False)
        self.btn_editarea.setFlat(False)
        self.btn_editarea.setObjectName("btn_editarea")
        self.lt_buttons.addWidget(self.btn_editarea)

        self.lt_buttons.addItem(spacerItem2)

        self.btn_finditem = QPushButton(self.frm_buttons)
        self.btn_finditem.setMinimumSize(QSize(0, 50))
        self.btn_finditem.setFont(font)
        self.btn_finditem.setIcon(icon3)
        self.btn_finditem.setIconSize(QSize(24, 24))
        self.btn_finditem.setFlat(False)
        self.btn_finditem.setObjectName("btn_finditem")
        self.lt_buttons.addWidget(self.btn_finditem)

        self.lt_buttons.addItem(spacerItem3)

        self.btn_lookinside = QPushButton(self.frm_buttons)
        self.btn_lookinside.setMinimumSize(QSize(0, 50))
        self.btn_lookinside.setFont(font)
        self.btn_lookinside.setIcon(icon4)
        self.btn_lookinside.setIconSize(QSize(24, 24))
        self.btn_lookinside.setFlat(False)
        self.btn_lookinside.setObjectName("btn_lookinside")
        self.lt_buttons.addWidget(self.btn_lookinside)

        self.btn_comein = QPushButton(self.frm_buttons)
        self.btn_comein.setMinimumSize(QSize(0, 50))
        self.btn_comein.setFont(font)
        self.btn_comein.setIcon(icon5)
        self.btn_comein.setIconSize(QSize(24, 24))
        self.btn_comein.setFlat(False)
        self.btn_comein.setObjectName("btn_comein")
        self.lt_buttons.addWidget(self.btn_comein)

        self.btn_comeout = QPushButton(self.frm_buttons)
        self.btn_comeout.setMinimumSize(QSize(0, 50))
        self.btn_comeout.setFont(font)
        self.btn_comeout.setIcon(icon6)
        self.btn_comeout.setIconSize(QSize(24, 24))
        self.btn_comeout.setFlat(False)
        self.btn_comeout.setObjectName("btn_comeout")
        self.lt_buttons.addWidget(self.btn_comeout)

        self.lt_buttons.addItem(spacerItem4)

        self.btn_orchestra = QPushButton(self.frm_buttons)
        self.btn_orchestra.setMinimumSize(QSize(0, 50))
        self.btn_orchestra.setFont(font)
        self.btn_orchestra.setIcon(icon7)
        self.btn_orchestra.setIconSize(QSize(24, 24))
        self.btn_orchestra.setFlat(False)
        self.btn_orchestra.setObjectName("btn_orchestra")
        self.lt_buttons.addWidget(self.btn_orchestra)

        self.lt_leftside.addWidget(self.frm_buttons)
        self.lt_leftside.addItem(spacerItem5)

        self.btn_exit = QPushButton(self.frm_leftside)
        self.btn_exit.setMinimumSize(QSize(0, 50))
        self.btn_exit.setMaximumSize(QSize(16777215, 50))
        self.btn_exit.setFont(font)
        self.btn_exit.setIcon(icon8)
        self.btn_exit.setIconSize(QSize(24, 24))
        self.btn_exit.setObjectName("btn_exit")

        self.lt_leftside.addWidget(self.btn_exit)

        self.lt_leftside.addItem(spacerItem6)

        # self.frm_logo.raise_()
        # self.frm_login.raise_()
        # self.frm_buttons.raise_()
        # self.btn_exit.raise_()

        self.lt_central.addWidget(self.frm_leftside)
        self.lt_rightside.addWidget(self.frm_top)

        self.gr_v = QGraphicsView(self.frm_rightside)
        self.gr_v.setMinimumSize(QSize(600, 400))
        self.gr_v.setFont(font)
        self.gr_v.setAutoFillBackground(False)
        self.gr_v.setStyleSheet("")
        self.gr_v.setFrameShape(QFrame.NoFrame)
        self.gr_v.setFrameShadow(QFrame.Plain)
        self.gr_v.setLineWidth(0)
        self.gr_v.setObjectName("gr_v")
        self.lt_rightside.addWidget(self.gr_v)

        self.lt_rightside.addItem(spacerItem7)

    def settext(self):
        self.btn_login.setText("ZALOGUJ")
        self.btn_logout.setText("WYLOGUJ")
        self.logstatus.setText("<FONT COLOR=\'#AA2222\'> Niezalogowany")
        self.btn_listofareas.setText("LISTA OBSZARÓW")
        self.btn_addarea.setText("DODAJ OBSZAR")
        self.btn_editarea.setText("EDYTUJ OBSZAR")
        self.btn_finditem.setText("WYSZUKAJ PRZEDMIOT")
        self.btn_lookinside.setText("ZAJRZYJ DO ŚRODKA")
        self.btn_comein.setText("PRZYJMIJ PRZEDMIOT")
        self.btn_comeout.setText("WYDAJ PRZEDMIOT")
        self.btn_orchestra.setText("SLOT ORKIESTRA")
        self.btn_exit.setText("WYJŚCIE")

    def setcentralwidget(self):
        self.lt_central.addWidget(self.frm_rightside)
        self.gridLayout.addLayout(self.lt_central, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
