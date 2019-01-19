# -*- coding: utf-8 -*-

from PyQt5.QtCore import QRect, Qt, QSize, QMetaObject, QTimer, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QPixmap, QIcon, QPainter
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QWidget, QGroupBox, QStatusBar, QPushButton, \
    QVBoxLayout, QHBoxLayout, QLabel, QAction, QMenu, QMenuBar, QGraphicsView, QGraphicsScene, QDialog, QLineEdit, \
    QGridLayout, QSizePolicy, QSpacerItem, QLayout, QGraphicsBlurEffect


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
                 "{background-color: #22FFFFFF}\n" \
                 "\n" \
                 "QFrame#frm_leftside\n" \
                 "{background-color: #22FFFFFF}\n" \
                 "\n" \
                 "QFrame#frm_login\n" \
                 "{background-color: #22FFFFFF}\n" \
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


def dialogstylesheet():
    stylesheet = "QFrame#line\n" \
                 "{color: #88FFFFFF}\n" \
                 "\n" \
                 "QLabel\n" \
                 "{color: #FFFFFFFF}\n" \
                 "\n" \
                 "\n" \
                 "QWidget\n" \
                 "{background-color: #00AAAAAA}\n" \
                 "\n" \
                 "QWidget#centralwidget\n" \
                 "{background-color: #88000000}\n" \
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
                 "QPushButton:hover#buttonok\n" \
                 "{background-color: #AA00AE37}\n" \
                 "\n" \
                 "QPushButton:hover#buttoncancel\n" \
                 "{background-color: #AAC60018}"
    return stylesheet


class _QGraphicsView(QGraphicsView):
    def __init__(self, parent):
        super(_QGraphicsView, self).__init__(parent)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._zoom = 0

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            factor = 1.25
            self._zoom += 1
        else:
            factor = 0.8
            self._zoom -= 1

        if self._zoom > 0:
            self.scale(factor, factor)
        elif self._zoom == 0:
            pass
        else:
            self.scale(factor, factor)


class MainWindow(QMainWindow):
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

    def blurwindow(self):
        self.blur = QGraphicsBlurEffect()
        self.blur.setBlurHints(QGraphicsBlurEffect.PerformanceHint)
        self.setGraphicsEffect(self.blur)
        self.blur.setBlurRadius(0)
        self.anim = QPropertyAnimation(self.blur, b'blurRadius')
        self.anim.setDuration(1000)
        self.anim.setStartValue(self.blur.blurRadius())
        self.anim.setEndValue(10)
        self.anim.setEasingCurve(QEasingCurve.InQuad)
        self.anim.start()

    def unblurwindow(self):
        self.anim = QPropertyAnimation(self.blur, b'blurRadius')
        self.anim.setDuration(500)
        self.anim.setStartValue(self.blur.blurRadius())
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.OutQuad)
        self.anim.start()
        self.anim.finished.connect(self.deleteblur)

    def deleteblur(self):
        self.setGraphicsEffect(None)

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

        self.setscena()
        self.setviewer()

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

    def closeEvent(self, event):
        self.blurwindow()
        ok = QuestionDialog.pytanie('Czy na pewno chcesz zakończyć?', self)
        if ok:
            event.accept()
        else:
            event.ignore()
            self.unblurwindow()

    def setscena(self):
        self.scena = QGraphicsScene()
        self.scena.setSceneRect(0, 0, 1000, 950)

    def setviewer(self):
        self.viewer = _QGraphicsView(self.frm_rightside)
        self.viewer.setMinimumSize(QSize(600, 400))
        # self.viewer.setFont(font)
        self.viewer.setAutoFillBackground(False)
        self.viewer.setStyleSheet("")
        self.viewer.setFrameShape(QFrame.NoFrame)
        self.viewer.setFrameShadow(QFrame.Plain)
        self.viewer.setLineWidth(0)
        self.viewer.setObjectName("viewer")
        self.viewer.setScene(self.scena)
        self.viewer.setRenderHints(QPainter.Antialiasing)
        self.viewer.fitInView(self.scena.sceneRect(), Qt.KeepAspectRatio)
        # scale = 0.75
        # self.viewer.scale(scale, scale)
        self.lt_rightside.addWidget(self.viewer)


class SlotDialog(QDialog):

    def setall(self):
        self.setwindow()
        self.setcentralwidget()
        self.setframes()
        self.setlayouts()

        self.icon = QLabel(self.fr_icon)
        self.icon.setMaximumSize(QSize(48, 64))
        self.icon.setText("")
        self.icon.setPixmap(QPixmap("images/popups/ok.png"))
        self.icon.setObjectName("label")

        self.line = QFrame(self.centralwidget)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setObjectName("line")

        self.lt_icon.addWidget(self.icon, 0, 0, 1, 1)
        self.lt_top.addWidget(self.fr_icon)
        self.lt_top.addWidget(self.fr_content)
        self.lt_central.addWidget(self.fr_top)
        self.lt_central.addWidget(self.line)
        self.lt_central.addWidget(self.fr_bottom)
        self.lt_dialog.addWidget(self.centralwidget, 0, 0, 1, 1)

    def setwindow(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(5)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(300, 100))
        self.setMaximumSize(QSize(600, 200))
        self.setSizeIncrement(QSize(0, 0))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #B721FF, stop:1 #21D4FD)")
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, True)

    def setcentralwidget(self):
        self.centralwidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(dialogstylesheet())
        self.centralwidget.setObjectName("centralwidget")

    def setframes(self):
        self.fr_top = QFrame(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.fr_top.setSizePolicy(sizePolicy)
        self.fr_top.setFrameShape(QFrame.StyledPanel)
        self.fr_top.setFrameShadow(QFrame.Raised)
        self.fr_top.setLineWidth(0)
        self.fr_top.setObjectName("fr_top")

        self.fr_icon = QFrame(self.fr_top)
        self.fr_icon.setFrameShape(QFrame.NoFrame)
        self.fr_icon.setFrameShadow(QFrame.Plain)
        self.fr_icon.setLineWidth(0)
        self.fr_icon.setObjectName("fr_icon")

        self.fr_content = QFrame(self.fr_top)
        self.fr_content.setFrameShape(QFrame.NoFrame)
        self.fr_content.setFrameShadow(QFrame.Plain)
        self.fr_content.setLineWidth(0)
        self.fr_content.setObjectName("fr_content")
        self.fr_content.setSizePolicy(sizePolicy)

        self.fr_bottom = QFrame(self.centralwidget)
        self.fr_bottom.setMaximumSize(QSize(16777215, 50))
        self.fr_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_bottom.setFrameShadow(QFrame.Plain)
        self.fr_bottom.setLineWidth(0)
        self.fr_bottom.setObjectName("fr_bottom")

        # self.fr_top.setStyleSheet('background-color: yellow')
        # self.fr_icon.setStyleSheet('background-color: blue')
        # self.fr_content.setStyleSheet('background-color: red')
        # self.fr_bottom.setStyleSheet('background-color: green')

    def setlayouts(self):
        self.lt_dialog = QGridLayout(self)
        self.lt_dialog.setObjectName("lt_dialog")
        self.lt_dialog.setContentsMargins(0, 0, 0, 0)
        self.lt_central = QVBoxLayout(self.centralwidget)
        self.lt_central.setContentsMargins(0, 0, 0, 0)
        self.lt_central.setSpacing(0)
        self.lt_central.setObjectName("lt_central")

        self.lt_top = QHBoxLayout(self.fr_top)
        self.lt_top.setContentsMargins(9, 9, 9, 9)
        self.lt_top.setSpacing(9)
        self.lt_top.setObjectName("lt_top")

        self.lt_icon = QGridLayout(self.fr_icon)
        self.lt_icon.setContentsMargins(0, 0, 0, 0)
        self.lt_icon.setSpacing(0)
        self.lt_icon.setObjectName("lt_icon")

        self.lt_content = QGridLayout(self.fr_content)
        self.lt_content.setContentsMargins(9, 9, 9, 9)
        self.lt_content.setSpacing(0)
        self.lt_content.setObjectName("lt_content")

        self.lt_bottom = QHBoxLayout(self.fr_bottom)
        self.lt_bottom.setContentsMargins(0, 0, 0, 0)
        self.lt_bottom.setSpacing(0)
        self.lt_bottom.setObjectName("lt_bottom")


class Dialog(SlotDialog):
    def __init__(self, typ, tekst, parent=None):
        super(Dialog, self).__init__(parent)
        self.setall()

        # Dodanie przycisku

        self.przycisk = QPushButton(self.fr_bottom)
        self.przycisk.setText('OK')
        self.przycisk.setMinimumWidth(100)
        self.przycisk.setMinimumHeight(50)
        self.przycisk.clicked.connect(self.reject)
        self.lt_bottom.addWidget(self.przycisk)

        # Wstawienie grafiki
        if typ == 'ok':
            obrazek = QPixmap('images/popups/ok.png')
        elif typ == 'warn':
            obrazek = QPixmap('images/popups/warn.png')
        elif typ == 'error':
            obrazek = QPixmap('images/popups/error.png')
        elif typ == 'info':
            obrazek = QPixmap('images/popups/info.png')
        else:
            obrazek = QPixmap('images/popups/info.png')
        self.icon.setPixmap(obrazek)

        # Wstawienie etykiety
        self.txtlabel = QLabel(self.fr_content)
        self.txtlabel.setText(tekst)
        self.txtlabel.setWordWrap(True)
        self.lt_content.addWidget(self.txtlabel)

    @staticmethod
    def komunikat(typ, tekst, parent=None):
        # parent.blurwindow()
        dialog = Dialog(typ, tekst, parent)
        ok = dialog.exec_()
        # parent.unblurwindow()

class QuestionDialog(SlotDialog):
    def __init__(self, tekst, parent=None):
        super(QuestionDialog, self).__init__(parent)
        self.setall()
        obrazek = QPixmap('images/popups/question.png')
        self.icon.setPixmap(obrazek)

        self.buttonok = QPushButton(self.fr_bottom)
        self.buttonok.setText('OK')
        self.buttonok.setFocus()
        self.buttonok.setMinimumWidth(100)
        self.buttonok.setMinimumHeight(50)
        self.buttonok.setObjectName('buttonok')
        self.buttoncancel = QPushButton(self.fr_bottom)
        self.buttoncancel.setText('Anuluj')
        self.buttoncancel.setMinimumWidth(100)
        self.buttoncancel.setMinimumHeight(50)
        self.buttoncancel.setObjectName('buttoncancel')
        self.buttonok.clicked.connect(self.accept)
        self.buttoncancel.clicked.connect(self.reject)
        self.lt_bottom.addWidget(self.buttonok)
        self.lt_bottom.addWidget(self.buttoncancel)

        self.txtlabel = QLabel(self.fr_content)
        self.txtlabel.setText(tekst)
        self.txtlabel.setWordWrap(True)
        self.lt_content.addWidget(self.txtlabel)

    @staticmethod
    def pytanie(tekst, parent=None):
        # parent.blurwindow()
        dialog = QuestionDialog(tekst, parent)
        ok = dialog.exec_()
        # parent.unblurwindow()
        return ok == QDialog.Accepted


class InputDialog(SlotDialog):
    def __init__(self, typ, tekst, parent=None):
        super(InputDialog, self).__init__(parent)
        self.setall()

        if typ == 'txt':
            obrazek = QPixmap('images/popups/txt.png')
        elif typ == 'barcode':
            obrazek = QPixmap('images/popups/code.png')
        self.icon.setPixmap(obrazek)

        self.buttonok = QPushButton(self.fr_bottom)
        self.buttonok.setText('OK')
        self.buttonok.setFocus()
        self.buttonok.setMinimumWidth(100)
        self.buttonok.setMinimumHeight(50)
        self.buttonok.setObjectName('buttonok')
        self.buttonok.setDefault(True)
        self.buttoncancel = QPushButton(self.fr_bottom)
        self.buttoncancel.setText('Anuluj')
        self.buttoncancel.setMinimumWidth(100)
        self.buttoncancel.setMinimumHeight(50)
        self.buttoncancel.setObjectName('buttoncancel')
        self.buttonok.clicked.connect(self.accept)
        self.buttoncancel.clicked.connect(self.reject)

        self.lt_bottom.addWidget(self.buttonok)
        self.lt_bottom.addWidget(self.buttoncancel)

        self.text = QLabel(self.fr_content)
        self.text.setText(tekst)
        self.input = QLineEdit()
        self.input.setStyleSheet(
            'background-color: #22FFFFFF; color: white; border-style: none; border-color: #FFFFFF; border-width: 1px; border-radius: 5px;')

        self.lt_content.addWidget(self.text, 0, 0, 1, 1)
        self.lt_content.addWidget(self.input, 1, 0, 1, 1)

    def inputtext(self):
        return self.input.text()

    @staticmethod
    def komunikat(typ, tekst, parent=None):
        # parent.blurwindow()
        dialog = InputDialog(typ, tekst, parent)
        dialog.input.setFocus()
        ok = dialog.exec_()
        output = dialog.inputtext()
        # parent.unblurwindow()
        return output, ok == QDialog.Accepted


class LoginDialog(SlotDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setall()
        obrazek = QPixmap('images/popups/txt.png')
        self.icon.setPixmap(obrazek)

        self.buttonok = QPushButton(self.fr_bottom)
        self.buttonok.setText('OK')
        self.buttonok.setFocus()
        self.buttonok.setMinimumWidth(100)
        self.buttonok.setMinimumHeight(30)
        self.buttonok.setObjectName('buttonok')
        self.buttonok.setDefault(True)

        self.buttoncancel = QPushButton(self.fr_bottom)
        self.buttoncancel.setText('Anuluj')
        self.buttoncancel.setMinimumWidth(100)
        self.buttoncancel.setMinimumHeight(30)
        self.buttoncancel.setObjectName('buttoncancel')

        self.buttonok.clicked.connect(self.accept)
        self.buttoncancel.clicked.connect(self.reject)

        self.lt_bottom.addWidget(self.buttonok)
        self.lt_bottom.addWidget(self.buttoncancel)

        loginlbl = QLabel('Login')
        haslolbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.login.setStyleSheet('background-color: #22FFFFFF; color: white; border-style: none; border-radius: 5px;')
        self.haslo = QLineEdit()
        self.haslo.setStyleSheet('background-color: #22FFFFFF; color: white; border-style: none; border-radius: 5px;')
        self.haslo.setEchoMode(QLineEdit.Password)

        self.lt_content.setSpacing(6)
        self.lt_content.addWidget(loginlbl, 0, 0, 1, 1)
        self.lt_content.addWidget(haslolbl, 1, 0, 1, 1)
        self.lt_content.addWidget(self.login, 0, 1, 1, 1)
        self.lt_content.addWidget(self.haslo, 1, 1, 1, 1)

    def loginHaslo(self):
        return (self.login.text().strip(),
                self.haslo.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getloginhaslo(parent=None):
        # parent.blurwindow()
        dialog = LoginDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        # parent.unblurwindow()
        login, haslo = dialog.loginHaslo()
        return login, haslo, ok == QDialog.Accepted
