# -*- coding: utf-8 -*-

import time
from PyQt5.QtCore import QRect, Qt, QSize, QMetaObject, QPropertyAnimation, QEasingCurve, QPoint, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QIcon, QPainter
from PyQt5.QtWidgets import QMainWindow, QFrame, QWidget, QPushButton, \
    QVBoxLayout, QHBoxLayout, QLabel, QGraphicsView, QGraphicsScene, QDialog, QLineEdit, \
    QGridLayout, QSizePolicy, QSpacerItem, QLayout, QGraphicsBlurEffect, QRubberBand, QPlainTextEdit, QListWidget, \
    QTableView


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
                 "QPushButton#btn_itemcounter\n" \
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
                 "QPushButton:checked#btn_orchestra\n" \
                 "{background-color: #558400FF}\n" \
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
                 "{background-color: #AAC60018}\n " \
                 "QLineEdit\n" \
                 "{background-color: #22FFFFFF; color: white; selection-background-color: darkgray; " \
                 "border-style: none; border-color: #FFFFFF; border-width: 1px; border-radius: 5px;}" \
                 "QPlainTextEdit\n" \
                 "{background-color: #22FFFFFF; color: white; selection-background-color: darkgray; " \
                 "border-style: none; border-color: #FFFFFF; border-width: 1px; border-radius: 5px;}" \
                 "QListWidget\n" \
                 "{background-color: #00000000; color: white; selection-color: white; " \
                 "border-style: none; border-color: #AA000000; border-width: 0px; border-radius: 5px;}\n" \
                 "QListWidget::item:hover\n" \
                 "{background: #22FFFFFF}\n" \
                 "QListWidget::item:selected\n" \
                 "{background: #66FFFFFF}\n" \
                 "\n" \
                 "QTableView\n" \
                 "{color: white; selection-background-color: #55000000; gridline-color: #55000000}" \
                 "QTableCornerButton::section\n" \
                 "{background-color: #55000000; color: white; border: 1px solid #55000000}" \
                 "QHeaderView::section" \
                 "{background-color: #55000000; color: white; border: 1px solid #55000000}\n" \
                 "QHeaderView::section:checked" \
                 "{background-color: #AA000000; color: white; border: 1px solid #55000000}\n" \
                 "QHeaderView::section" \
                 "{background-color: #55000000; color: white; border: 1px solid #55000000}\n"
    return stylesheet


class _QGraphicsScene(QGraphicsScene):
    rectChanged = pyqtSignal(QRect)

    def __init__(self, parent):
        super(_QGraphicsScene, self).__init__(parent)


class _QGraphicsView(QGraphicsView):
    rectChanged = pyqtSignal(QRect)

    def __init__(self, parent):
        super(_QGraphicsView, self).__init__(parent)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._zoom = 0
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.setMouseTracking(True)
        self.origin = QPoint()
        self.changeRubberBand = False
        # self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setInteractive(False)  # Wyłączenie funkcji interaktywnych - np. przesuwania obszarów
        self.mode = 'normal'  # deklaracja normalnego trybu pracy

    # Przełączenie na tryb rysowania nowego obszaru
    def addareamode(self):
        self.setInteractive(False)
        self.mode = 'addarea'

    # Przełączenie na tryb normalny
    def normalmode(self):
        self.mode = 'normal'

    # obsługa przybliżania i oddalania - funkcja eksperymentalna
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

    # Rozpoczęcie rysowania nowego obszaru
    def mousePressEvent(self, event):
        if self.mode == 'addarea':
            self.origin = event.pos()
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()
            self.changeRubberBand = True
            QGraphicsView.mousePressEvent(self, event)
        else:
            super(_QGraphicsView, self).mousePressEvent(event)

    # Rysowanie obszaru
    def mouseMoveEvent(self, event):
        if self.mode == 'addarea':
            if self.changeRubberBand:
                self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
            QGraphicsView.mouseMoveEvent(self, event)
        else:
            super(_QGraphicsView, self).mouseMoveEvent(event)

    # Zakończenie rysowania obszaru
    def mouseReleaseEvent(self, event):
        if self.mode == 'addarea':
            self.changeRubberBand = False
            self.rectChanged.emit(self.rubberBand.geometry())  # Nadanie sygnału wyzwalającego koniec rysowania
            # self.rubberBand.hide()
            QGraphicsView.mouseReleaseEvent(self, event)
        else:
            super(_QGraphicsView, self).mouseReleaseEvent(event)


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
        try:
            self.blur.blurRadius() == 0
        except:
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
            self.disablebuttons()

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
        self.enablebuttons()

    def disablebuttons(self):
        self.btn_login.setEnabled(False)
        self.btn_logout.setEnabled(False)
        self.btn_listofareas.setEnabled(False)
        self.btn_itemcounter.setEnabled(False)
        self.btn_addarea.setEnabled(False)
        self.btn_editarea.setEnabled(False)
        self.btn_finditem.setEnabled(False)
        self.btn_comein.setEnabled(False)
        self.btn_comeout.setEnabled(False)
        self.btn_lookinside.setEnabled(False)
        self.btn_orchestra.setEnabled(False)
        self.btn_exit.setEnabled(False)

    def enablebuttons(self):
        time.sleep(0.1)
        self.btn_login.setEnabled(True)
        self.btn_logout.setEnabled(True)
        self.btn_listofareas.setEnabled(True)
        self.btn_itemcounter.setEnabled(True)
        self.btn_addarea.setEnabled(True)
        self.btn_editarea.setEnabled(True)
        self.btn_finditem.setEnabled(True)
        self.btn_comein.setEnabled(True)
        self.btn_comeout.setEnabled(True)
        self.btn_lookinside.setEnabled(True)
        self.btn_orchestra.setEnabled(True)
        self.btn_exit.setEnabled(True)

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
        self.frm_loginbuttons.setFrameShape(QFrame.NoFrame)
        self.frm_loginbuttons.setFrameShadow(QFrame.Plain)
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
        spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Maximum)
        spacerItem2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)
        spacerItem3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)
        spacerItem4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)
        spacerItem5 = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
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
        icon0 = QIcon()
        icon0.addPixmap(QPixmap("images/buttons/btn_itemcounter_hover.png"), QIcon.Normal, QIcon.Off)
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

        self.btn_itemcounter = QPushButton(self.frm_buttons)
        self.btn_itemcounter.setMinimumSize(QSize(0, 50))
        self.btn_itemcounter.setFont(font)
        self.btn_itemcounter.setAutoFillBackground(False)
        self.btn_itemcounter.setStyleSheet("")
        self.btn_itemcounter.setIcon(icon0)
        self.btn_itemcounter.setIconSize(QSize(24, 24))
        self.btn_itemcounter.setFlat(False)
        self.btn_itemcounter.setObjectName("btn_itemcounter")
        self.lt_buttons.addWidget(self.btn_itemcounter)

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
        self.btn_orchestra.setCheckable(True)
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
        self.btn_itemcounter.setText("ZAPEŁNIENIE")
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
        self.scena = _QGraphicsScene(self)
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
        self.fr_top.setFrameShape(QFrame.NoFrame)
        self.fr_top.setFrameShadow(QFrame.Plain)
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


class OrchestraModule(QWidget):
    def __init__(self, parent=None):
        super(OrchestraModule, self).__init__(parent)
        self.setwindow()
        self.setcentralwidget()
        self.setframes()
        self.setlayouts()
        self.setbuttons()
        self.setlabels()
        self.setlineedits()

        self.lt_central.addWidget(self.fr_top)
        self.lt_central.addWidget(self.line)
        self.lt_central.addWidget(self.fr_mid)
        self.lt_central.addWidget(self.fr_bottom)
        self.lt_module.addWidget(self.centralwidget, 0, 0, 1, 1)

    def setwindow(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(5)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(100, 200))
        self.setMaximumSize(QSize(200, 400))
        self.setSizeIncrement(QSize(0, 0))
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFFFFF, stop:1 #AAAAAA)")
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowTitle('SLOT Orkiestra')
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setAttribute(Qt.WA_NoSystemBackground, True)

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
        self.fr_top.setFrameShape(QFrame.NoFrame)
        self.fr_top.setFrameShadow(QFrame.Plain)
        self.fr_top.setLineWidth(0)
        self.fr_top.setObjectName("fr_top")

        self.line = QFrame(self.centralwidget)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setObjectName("line")

        self.fr_mid = QFrame(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.fr_mid.setSizePolicy(sizePolicy)
        self.fr_mid.setFrameShape(QFrame.NoFrame)
        self.fr_mid.setFrameShadow(QFrame.Plain)
        self.fr_mid.setLineWidth(0)
        self.fr_mid.setObjectName("fr_mid")

        self.fr_bottom = QFrame(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.fr_bottom.setSizePolicy(sizePolicy)
        self.fr_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_bottom.setFrameShadow(QFrame.Plain)
        self.fr_bottom.setLineWidth(0)
        self.fr_bottom.setObjectName("fr_bottom")

    def setlayouts(self):
        self.lt_module = QGridLayout(self)
        self.lt_module.setObjectName("lt_module")
        self.lt_module.setContentsMargins(0, 0, 0, 0)

        self.lt_central = QVBoxLayout(self.centralwidget)
        self.lt_central.setContentsMargins(0, 0, 0, 0)
        self.lt_central.setSpacing(0)
        self.lt_central.setObjectName("lt_central")

        self.lt_top = QGridLayout(self.fr_top)
        self.lt_top.setObjectName("lt_top")
        self.lt_top.setContentsMargins(6, 6, 6, 6)
        self.lt_top.setSpacing(6)

        self.lt_mid = QVBoxLayout(self.fr_mid)
        self.lt_mid.setContentsMargins(0, 0, 0, 0)
        self.lt_mid.setSpacing(0)
        self.lt_mid.setObjectName("lt_mid")

        self.lt_bottom = QGridLayout(self)

    def setbuttons(self):
        self.btn_orchtable = QPushButton(self.fr_mid)
        self.btn_orchtable.setText('Lista przedmiotów')
        self.btn_orchtable.setMinimumWidth(100)
        self.btn_orchtable.setMinimumHeight(50)
        self.lt_mid.addWidget(self.btn_orchtable)

        self.btn_orchfirstcomein = QPushButton(self.fr_mid)
        self.btn_orchfirstcomein.setText('Przyjmij po raz pierwszy')
        self.btn_orchfirstcomein.setMinimumWidth(100)
        self.btn_orchfirstcomein.setMinimumHeight(50)
        self.lt_mid.addWidget(self.btn_orchfirstcomein)

        self.btn_orchcomein = QPushButton(self.fr_mid)
        self.btn_orchcomein.setText('Przyjmij przedmiot')
        self.btn_orchcomein.setMinimumWidth(100)
        self.btn_orchcomein.setMinimumHeight(50)
        self.lt_mid.addWidget(self.btn_orchcomein)

        self.btn_orchcomeout = QPushButton(self.fr_mid)
        self.btn_orchcomeout.setText('Wydaj przedmiot')
        self.btn_orchcomeout.setMinimumWidth(100)
        self.btn_orchcomeout.setMinimumHeight(50)
        self.lt_mid.addWidget(self.btn_orchcomeout)

    def setlabels(self):

        self.lbl_items = QLabel(self.fr_top)
        self.lbl_items.setText("Przedmioty")
        self.lbl_items.setAlignment(Qt.AlignCenter)
        self.lt_top.addWidget(self.lbl_items, 0, 0, 1, 2)

        self.lbl_overall = QLabel(self.fr_top)
        self.lbl_overall.setText('Łącznie:')
        self.lbl_overall.setAlignment(Qt.AlignRight)
        self.lt_top.addWidget(self.lbl_overall, 1, 0, 1, 1)

        self.lbl_onmagazine = QLabel(self.fr_top)
        self.lbl_onmagazine.setText('Na magazynie: ')
        self.lbl_onmagazine.setAlignment(Qt.AlignRight)
        self.lt_top.addWidget(self.lbl_onmagazine, 2, 0, 1, 1)

        self.lbl_outmagazine = QLabel(self.fr_top)
        self.lbl_outmagazine.setText('Poza magazynem: ')
        self.lbl_outmagazine.setAlignment(Qt.AlignRight)
        self.lt_top.addWidget(self.lbl_outmagazine, 3, 0, 1, 1)

    def setlineedits(self):
        self.le_overall = QLineEdit(self.fr_top)
        self.le_overall.setText('0')
        self.le_overall.setReadOnly(True)
        self.lt_top.addWidget(self.le_overall, 1, 1, 1, 1)

        self.le_onmagazine = QLineEdit(self.fr_top)
        self.le_onmagazine.setText('0')
        self.le_onmagazine.setReadOnly(True)
        self.lt_top.addWidget(self.le_onmagazine, 2, 1, 1, 1)

        self.le_outmagazine = QLineEdit(self.fr_top)
        self.le_outmagazine.setText('0')
        self.le_outmagazine.setReadOnly(True)
        self.lt_top.addWidget(self.le_outmagazine, 3, 1, 1, 1)

    def toggleshow(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()

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
        self.enablebuttons()

    def disablebuttons(self):
        pass

    def enablebuttons(self):
        time.sleep(0.1)
        pass


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


class AreaEditDialog(QDialog):
    def __init__(self, obszar, parent=None):
        super(AreaEditDialog, self).__init__(parent)
        self.obszar = obszar
        self.setwindow()
        self.setcentralwidget()
        self.setframes()
        self.setlayouts()
        self.setbuttons()
        self.setlabels()
        self.setedits()
        self.filledits()

        self.line = QFrame(self.centralwidget)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setObjectName("line")

        self.setmainlabel()

        self.addwidgets()

        self.buttonok.clicked.connect(self.accept)
        self.buttoncancel.clicked.connect(self.reject)

    def setwindow(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(5)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(300, 400))
        self.setMaximumSize(QSize(300, 400))
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
        self.fr_top.setFrameShape(QFrame.NoFrame)
        self.fr_top.setFrameShadow(QFrame.Plain)
        self.fr_top.setLineWidth(0)
        self.fr_top.setObjectName("fr_top")

        self.fr_label = QFrame(self.fr_top)
        self.fr_label.setMaximumSize(QSize(16777215, 50))
        self.fr_label.setFrameShape(QFrame.NoFrame)
        self.fr_label.setFrameShadow(QFrame.Plain)
        self.fr_label.setLineWidth(0)
        self.fr_label.setObjectName("fr_label")

        self.fr_content = QFrame(self.fr_top)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.fr_content.setSizePolicy(sizePolicy)
        self.fr_content.setFrameShape(QFrame.NoFrame)
        self.fr_content.setFrameShadow(QFrame.Plain)
        self.fr_content.setLineWidth(0)
        self.fr_content.setObjectName("fr_content")

        self.fr_bottom = QFrame(self.centralwidget)
        self.fr_bottom.setMaximumSize(QSize(16777215, 50))
        self.fr_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_bottom.setFrameShadow(QFrame.Plain)
        self.fr_bottom.setLineWidth(0)
        self.fr_bottom.setObjectName("fr_bottom")

    def setlayouts(self):
        self.lt_dialog = QGridLayout(self)
        self.lt_dialog.setObjectName("lt_dialog")
        self.lt_dialog.setContentsMargins(0, 0, 0, 0)
        self.lt_central = QVBoxLayout(self.centralwidget)
        self.lt_central.setContentsMargins(0, 0, 0, 0)
        self.lt_central.setSpacing(0)
        self.lt_central.setObjectName("lt_central")

        self.lt_bottom = QHBoxLayout(self.fr_bottom)
        self.lt_bottom.setContentsMargins(0, 0, 0, 0)
        self.lt_bottom.setSpacing(0)
        self.lt_bottom.setObjectName("lt_bottom")

        self.lt_top = QVBoxLayout(self.fr_top)
        self.lt_top.setContentsMargins(0, 20, 0, 10)
        self.lt_top.setSpacing(20)
        self.lt_top.setObjectName("lt_top")

        self.lt_label = QGridLayout(self.fr_label)
        self.lt_label.setObjectName("lt_label")
        self.lt_label.setContentsMargins(0, 0, 0, 0)

        self.lt_content = QGridLayout(self.fr_content)
        self.lt_content.setObjectName("lt_content")
        self.lt_content.setContentsMargins(20, 0, 20, 0)
        self.lt_content.setSpacing(9)

    def setbuttons(self):
        self.buttonok = QPushButton(self.fr_bottom)
        self.buttonok.setText('Zapisz zmiany')
        self.buttonok.setFocus()
        self.buttonok.setMinimumWidth(100)
        self.buttonok.setMinimumHeight(50)
        self.buttonok.setObjectName('buttonok')
        self.buttoncancel = QPushButton(self.fr_bottom)
        self.buttoncancel.setText('Anuluj')
        self.buttoncancel.setMinimumWidth(100)
        self.buttoncancel.setMinimumHeight(50)
        self.buttoncancel.setObjectName('buttoncancel')

    def setlabels(self):
        self.label_areaname = QLabel(self.fr_content)
        self.label_person1 = QLabel(self.fr_content)
        self.label_person2 = QLabel(self.fr_content)
        self.label_person3 = QLabel(self.fr_content)
        self.label_tel1 = QLabel(self.fr_content)
        self.label_tel2 = QLabel(self.fr_content)
        self.label_tel3 = QLabel(self.fr_content)
        self.label_comments = QLabel(self.fr_content)

        self.label_areaname.setText('Nazwa obszaru')
        self.label_person1.setText('Osoba kontaktowa')
        self.label_person2.setText('Osoba kontaktowa')
        self.label_person3.setText('Osoba kontaktowa')
        self.label_tel1.setText('Telefon')
        self.label_tel2.setText('Telefon')
        self.label_tel3.setText('Telefon')
        self.label_comments.setText('Uwagi')

        self.label_areaname.setAlignment(Qt.AlignRight)
        self.label_person1.setAlignment(Qt.AlignRight)
        self.label_person2.setAlignment(Qt.AlignRight)
        self.label_person3.setAlignment(Qt.AlignRight)
        self.label_tel1.setAlignment(Qt.AlignRight)
        self.label_tel2.setAlignment(Qt.AlignRight)
        self.label_tel3.setAlignment(Qt.AlignRight)
        self.label_comments.setAlignment(Qt.AlignRight)

    def setedits(self):
        self.edit_areaname = QLineEdit(self.fr_content)
        self.edit_person1 = QLineEdit(self.fr_content)
        self.edit_person2 = QLineEdit(self.fr_content)
        self.edit_person3 = QLineEdit(self.fr_content)
        self.edit_tel1 = QLineEdit(self.fr_content)
        self.edit_tel2 = QLineEdit(self.fr_content)
        self.edit_tel3 = QLineEdit(self.fr_content)
        self.edit_comments = QPlainTextEdit(self.fr_content)
        self.edit_comments.setMaximumHeight(50)
        self.edit_comments.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def setmainlabel(self):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.mainlabel = QLabel(self.fr_label)
        mainlabel = str(self.obszar['areaid']) + ' - ' + str(self.obszar['areaname'])
        self.mainlabel.setText(mainlabel)
        self.mainlabel.setFont(font)
        self.mainlabel.setAlignment(Qt.AlignCenter)

    def addwidgets(self):
        self.lt_bottom.addWidget(self.buttonok)
        self.lt_bottom.addWidget(self.buttoncancel)

        self.lt_label.addWidget(self.mainlabel, 0, 0, 1, 1)

        self.lt_content.addWidget(self.label_areaname, 0, 0, 1, 1)
        self.lt_content.addWidget(self.label_person1, 1, 0, 1, 1)
        self.lt_content.addWidget(self.label_person2, 2, 0, 1, 1)
        self.lt_content.addWidget(self.label_person3, 3, 0, 1, 1)
        self.lt_content.addWidget(self.label_tel1, 4, 0, 1, 1)
        self.lt_content.addWidget(self.label_tel2, 5, 0, 1, 1)
        self.lt_content.addWidget(self.label_tel3, 6, 0, 1, 1)
        self.lt_content.addWidget(self.label_comments, 7, 0, 1, 1)

        self.lt_content.addWidget(self.edit_areaname, 0, 1, 1, 1)
        self.lt_content.addWidget(self.edit_person1, 1, 1, 1, 1)
        self.lt_content.addWidget(self.edit_person2, 2, 1, 1, 1)
        self.lt_content.addWidget(self.edit_person3, 3, 1, 1, 1)
        self.lt_content.addWidget(self.edit_tel1, 4, 1, 1, 1)
        self.lt_content.addWidget(self.edit_tel2, 5, 1, 1, 1)
        self.lt_content.addWidget(self.edit_tel3, 6, 1, 1, 1)
        self.lt_content.addWidget(self.edit_comments, 7, 1, 1, 1)

        self.lt_top.addWidget(self.fr_label)
        self.lt_top.addWidget(self.fr_content)
        self.lt_central.addWidget(self.fr_top)
        self.lt_central.addWidget(self.line)
        self.lt_central.addWidget(self.fr_bottom)
        self.lt_dialog.addWidget(self.centralwidget, 0, 0, 1, 1)

    def filledits(self):
        self.edit_areaname.setText(self.obszar['areaname'])
        self.edit_person1.setText(self.obszar['person1'])
        self.edit_person2.setText(self.obszar['person2'])
        self.edit_person3.setText(self.obszar['person3'])
        self.edit_tel1.setText(self.obszar['tel1'])
        self.edit_tel2.setText(self.obszar['tel2'])
        self.edit_tel3.setText(self.obszar['tel3'])
        self.edit_comments.setPlainText(self.obszar['comments'])

    def nowyobszar(self, obszar):
        obszar['areaname'] = self.edit_areaname.text().strip()
        obszar['person1'] = self.edit_person1.text().strip()
        obszar['person2'] = self.edit_person2.text().strip()
        obszar['person3'] = self.edit_person3.text().strip()
        obszar['tel1'] = self.edit_tel1.text().strip()
        obszar['tel2'] = self.edit_tel2.text().strip()
        obszar['tel3'] = self.edit_tel3.text().strip()
        obszar['comments'] = self.edit_comments.toPlainText().strip()
        return obszar

    # metoda statyczna, tworzy dialog i zwraca słownik z nowymi danymi obszaru
    @staticmethod
    def editarea(obszar, parent=None):
        dialog = AreaEditDialog(obszar, parent)
        ok = dialog.exec_()
        nowyobszar = dialog.nowyobszar(obszar)
        return nowyobszar, ok == QDialog.Accepted


class AreaListSmall(QDialog):
    def __init__(self, obszary, parent=None):
        super(AreaListSmall, self).__init__(parent)
        self.obszary = obszary

        self.setwindow()
        self.setcentralwidget()
        self.setframes()
        self.setlayouts()
        self.setbuttons()
        self.setmainlabel()
        self.setlist()

        self.line = QFrame(self.centralwidget)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setObjectName("line")

        self.addwidgets()

        self.buttonok.clicked.connect(self.accept)
        self.buttoncancel.clicked.connect(self.reject)

    def setwindow(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(5)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(300, 600))
        self.setMaximumSize(QSize(300, 600))
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
        self.fr_top.setFrameShape(QFrame.NoFrame)
        self.fr_top.setFrameShadow(QFrame.Plain)
        self.fr_top.setLineWidth(0)
        self.fr_top.setObjectName("fr_top")

        self.fr_label = QFrame(self.fr_top)
        self.fr_label.setMaximumSize(QSize(16777215, 50))
        self.fr_label.setFrameShape(QFrame.NoFrame)
        self.fr_label.setFrameShadow(QFrame.Plain)
        self.fr_label.setLineWidth(0)
        self.fr_label.setObjectName("fr_label")

        self.fr_content = QFrame(self.fr_top)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.fr_content.setSizePolicy(sizePolicy)
        self.fr_content.setFrameShape(QFrame.NoFrame)
        self.fr_content.setFrameShadow(QFrame.Plain)
        self.fr_content.setLineWidth(0)
        self.fr_content.setObjectName("fr_content")

        self.fr_bottom = QFrame(self.centralwidget)
        self.fr_bottom.setMaximumSize(QSize(16777215, 50))
        self.fr_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_bottom.setFrameShadow(QFrame.Plain)
        self.fr_bottom.setLineWidth(0)
        self.fr_bottom.setObjectName("fr_bottom")

    def setlayouts(self):
        self.lt_dialog = QGridLayout(self)
        self.lt_dialog.setObjectName("lt_dialog")
        self.lt_dialog.setContentsMargins(0, 0, 0, 0)
        self.lt_central = QVBoxLayout(self.centralwidget)
        self.lt_central.setContentsMargins(0, 0, 0, 0)
        self.lt_central.setSpacing(0)
        self.lt_central.setObjectName("lt_central")

        self.lt_bottom = QHBoxLayout(self.fr_bottom)
        self.lt_bottom.setContentsMargins(0, 0, 0, 0)
        self.lt_bottom.setSpacing(0)
        self.lt_bottom.setObjectName("lt_bottom")

        self.lt_top = QVBoxLayout(self.fr_top)
        self.lt_top.setContentsMargins(0, 20, 0, 10)
        self.lt_top.setSpacing(20)
        self.lt_top.setObjectName("lt_top")

        self.lt_label = QGridLayout(self.fr_label)
        self.lt_label.setObjectName("lt_label")
        self.lt_label.setContentsMargins(0, 0, 0, 0)

        self.lt_content = QGridLayout(self.fr_content)
        self.lt_content.setObjectName("lt_content")
        self.lt_content.setContentsMargins(20, 0, 20, 0)
        self.lt_content.setSpacing(9)

    def setbuttons(self):
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

    def setmainlabel(self):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.mainlabel = QLabel(self.fr_label)
        self.mainlabel.setText('Wybierz obszar, który chcesz edytować')
        self.mainlabel.setFont(font)
        self.mainlabel.setAlignment(Qt.AlignCenter)

    def setlist(self):
        lista = []
        self.lista = QListWidget(self.fr_content)
        for obszar in self.obszary:
            obszartekst = str(obszar['areaid']) + ' - ' + str(obszar['areaname'])
            lista.append(obszartekst)
        self.lista.addItems(lista)
        self.lista.setFrameShape(QFrame.NoFrame)
        self.lista.setFrameShadow(QFrame.Plain)
        self.lista.setLineWidth(0)
        self.lista.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def addwidgets(self):
        self.lt_bottom.addWidget(self.buttonok)
        self.lt_bottom.addWidget(self.buttoncancel)

        self.lt_label.addWidget(self.mainlabel, 0, 0, 1, 1)

        self.lt_content.addWidget(self.lista, 0, 0, 1, 1)

        self.lt_top.addWidget(self.fr_label)
        self.lt_top.addWidget(self.fr_content)
        self.lt_central.addWidget(self.fr_top)
        self.lt_central.addWidget(self.line)
        self.lt_central.addWidget(self.fr_bottom)

        self.lt_dialog.addWidget(self.centralwidget, 0, 0, 1, 1)

    def ktoryobszar(self, obszary):
        try:
            obiekt = self.lista.currentItem().text()
            obiektnum = obiekt[:obiekt.find(' ')]
            obiektnum = int(obiektnum)
        except:
            obiektnum = 0
        return obiektnum

    # metoda statyczna, tworzy dialog i wybrany ID, ok
    @staticmethod
    def showlist(obszary, parent=None):
        dialog = AreaListSmall(obszary, parent)
        ok = dialog.exec_()
        wybranyID = dialog.ktoryobszar(obszary)
        return wybranyID, ok == QDialog.Accepted


class AreaList(QDialog):
    def __init__(self, model, parent=None):
        super(AreaList, self).__init__(parent)
        self.model = model

        self.setwindow()
        self.setcentralwidget()
        self.setframes()
        self.setlayouts()
        self.setbuttons()
        self.settable()

        self.line = QFrame(self.centralwidget)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setObjectName("line")

        self.addwidgets()

        self.buttonok.clicked.connect(self.submitandaccept)
        self.buttoncancel.clicked.connect(self.revertaandreject)

    def submitandaccept(self):
        self.model.submitAll()
        self.accept()

    def revertaandreject(self):
        self.model.revertAll()
        self.reject()

    def setwindow(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(5)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(1200, 600))
        self.setMaximumSize(QSize(1200, 600))
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
        self.fr_top.setFrameShape(QFrame.NoFrame)
        self.fr_top.setFrameShadow(QFrame.Plain)
        self.fr_top.setLineWidth(0)
        self.fr_top.setObjectName("fr_top")

        self.fr_label = QFrame(self.fr_top)
        self.fr_label.setMaximumSize(QSize(16777215, 50))
        self.fr_label.setFrameShape(QFrame.NoFrame)
        self.fr_label.setFrameShadow(QFrame.Plain)
        self.fr_label.setLineWidth(0)
        self.fr_label.setObjectName("fr_label")

        self.fr_content = QFrame(self.fr_top)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.fr_content.setSizePolicy(sizePolicy)
        self.fr_content.setFrameShape(QFrame.NoFrame)
        self.fr_content.setFrameShadow(QFrame.Plain)
        self.fr_content.setLineWidth(0)
        self.fr_content.setObjectName("fr_content")

        self.fr_bottom = QFrame(self.centralwidget)
        self.fr_bottom.setMaximumSize(QSize(16777215, 50))
        self.fr_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_bottom.setFrameShadow(QFrame.Plain)
        self.fr_bottom.setLineWidth(0)
        self.fr_bottom.setObjectName("fr_bottom")

    def setlayouts(self):
        self.lt_dialog = QGridLayout(self)
        self.lt_dialog.setObjectName("lt_dialog")
        self.lt_dialog.setContentsMargins(0, 0, 0, 0)
        self.lt_central = QVBoxLayout(self.centralwidget)
        self.lt_central.setContentsMargins(0, 0, 0, 0)
        self.lt_central.setSpacing(0)
        self.lt_central.setObjectName("lt_central")

        self.lt_bottom = QHBoxLayout(self.fr_bottom)
        self.lt_bottom.setContentsMargins(0, 0, 0, 0)
        self.lt_bottom.setSpacing(0)
        self.lt_bottom.setObjectName("lt_bottom")

        self.lt_top = QVBoxLayout(self.fr_top)
        self.lt_top.setContentsMargins(0, 0, 0, 10)
        self.lt_top.setSpacing(20)
        self.lt_top.setObjectName("lt_top")

        self.lt_label = QGridLayout(self.fr_label)
        self.lt_label.setObjectName("lt_label")
        self.lt_label.setContentsMargins(0, 0, 0, 0)

        self.lt_content = QGridLayout(self.fr_content)
        self.lt_content.setObjectName("lt_content")
        self.lt_content.setContentsMargins(0, 0, 0, 0)
        self.lt_content.setSpacing(9)

    def setbuttons(self):
        self.buttonok = QPushButton(self.fr_bottom)
        self.buttonok.setText('Zapisz zmiany')
        self.buttonok.setFocus()
        self.buttonok.setMinimumWidth(100)
        self.buttonok.setMinimumHeight(50)
        self.buttonok.setObjectName('buttonok')
        self.buttoncancel = QPushButton(self.fr_bottom)
        self.buttoncancel.setText('Anuluj')
        self.buttoncancel.setMinimumWidth(100)
        self.buttoncancel.setMinimumHeight(50)
        self.buttoncancel.setObjectName('buttoncancel')

    def settable(self):
        self.table = QTableView(self.fr_content)
        self.table.setModel(self.model)
        self.table.hideColumn(3)
        self.table.hideColumn(4)
        self.table.hideColumn(5)
        self.table.hideColumn(6)

        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setFrameShadow(QFrame.Plain)
        self.table.setLineWidth(0)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def addwidgets(self):
        self.lt_bottom.addWidget(self.buttonok)
        self.lt_bottom.addWidget(self.buttoncancel)
        self.lt_content.addWidget(self.table, 0, 0, 1, 1)
        self.lt_top.addWidget(self.fr_content)
        self.lt_central.addWidget(self.fr_top)
        self.lt_central.addWidget(self.line)
        self.lt_central.addWidget(self.fr_bottom)
        self.lt_dialog.addWidget(self.centralwidget, 0, 0, 1, 1)

    # metoda statyczna, tworzy dialog i wybrany ID, ok
    @staticmethod
    def showtable(model, parent=None):
        dialog = AreaList(model, parent)
        ok = dialog.exec_()
        return ok == QDialog.Accepted


class ItemList(QDialog):
    def __init__(self, model, parent=None):
        super(AreaList, self).__init__(parent)
        self.model = model

        self.setwindow()
        self.setcentralwidget()
        self.setframes()
        self.setlayouts()
        self.setbuttons()
        self.settable()

        self.line = QFrame(self.centralwidget)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setObjectName("line")

        self.addwidgets()

        self.buttonok.clicked.connect(self.submitandaccept)
        self.buttoncancel.clicked.connect(self.revertaandreject)

    def submitandaccept(self):
        self.model.submitAll()
        self.accept()

    def revertaandreject(self):
        self.model.revertAll()
        self.reject()

    def setwindow(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(5)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(1200, 600))
        self.setMaximumSize(QSize(1200, 600))
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
        self.fr_top.setFrameShape(QFrame.NoFrame)
        self.fr_top.setFrameShadow(QFrame.Plain)
        self.fr_top.setLineWidth(0)
        self.fr_top.setObjectName("fr_top")

        self.fr_label = QFrame(self.fr_top)
        self.fr_label.setMaximumSize(QSize(16777215, 50))
        self.fr_label.setFrameShape(QFrame.NoFrame)
        self.fr_label.setFrameShadow(QFrame.Plain)
        self.fr_label.setLineWidth(0)
        self.fr_label.setObjectName("fr_label")

        self.fr_content = QFrame(self.fr_top)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.fr_content.setSizePolicy(sizePolicy)
        self.fr_content.setFrameShape(QFrame.NoFrame)
        self.fr_content.setFrameShadow(QFrame.Plain)
        self.fr_content.setLineWidth(0)
        self.fr_content.setObjectName("fr_content")

        self.fr_bottom = QFrame(self.centralwidget)
        self.fr_bottom.setMaximumSize(QSize(16777215, 50))
        self.fr_bottom.setFrameShape(QFrame.NoFrame)
        self.fr_bottom.setFrameShadow(QFrame.Plain)
        self.fr_bottom.setLineWidth(0)
        self.fr_bottom.setObjectName("fr_bottom")

    def setlayouts(self):
        self.lt_dialog = QGridLayout(self)
        self.lt_dialog.setObjectName("lt_dialog")
        self.lt_dialog.setContentsMargins(0, 0, 0, 0)
        self.lt_central = QVBoxLayout(self.centralwidget)
        self.lt_central.setContentsMargins(0, 0, 0, 0)
        self.lt_central.setSpacing(0)
        self.lt_central.setObjectName("lt_central")

        self.lt_bottom = QHBoxLayout(self.fr_bottom)
        self.lt_bottom.setContentsMargins(0, 0, 0, 0)
        self.lt_bottom.setSpacing(0)
        self.lt_bottom.setObjectName("lt_bottom")

        self.lt_top = QVBoxLayout(self.fr_top)
        self.lt_top.setContentsMargins(0, 0, 0, 10)
        self.lt_top.setSpacing(20)
        self.lt_top.setObjectName("lt_top")

        self.lt_label = QGridLayout(self.fr_label)
        self.lt_label.setObjectName("lt_label")
        self.lt_label.setContentsMargins(0, 0, 0, 0)

        self.lt_content = QGridLayout(self.fr_content)
        self.lt_content.setObjectName("lt_content")
        self.lt_content.setContentsMargins(0, 0, 0, 0)
        self.lt_content.setSpacing(9)

    def setbuttons(self):
        self.buttonok = QPushButton(self.fr_bottom)
        self.buttonok.setText('Zapisz zmiany')
        self.buttonok.setFocus()
        self.buttonok.setMinimumWidth(100)
        self.buttonok.setMinimumHeight(50)
        self.buttonok.setObjectName('buttonok')
        self.buttoncancel = QPushButton(self.fr_bottom)
        self.buttoncancel.setText('Anuluj')
        self.buttoncancel.setMinimumWidth(100)
        self.buttoncancel.setMinimumHeight(50)
        self.buttoncancel.setObjectName('buttoncancel')

    def settable(self):
        self.table = QTableView(self.fr_content)
        self.table.setModel(self.model)
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setFrameShadow(QFrame.Plain)
        self.table.setLineWidth(0)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def addwidgets(self):
        self.lt_bottom.addWidget(self.buttonok)
        self.lt_bottom.addWidget(self.buttoncancel)
        self.lt_content.addWidget(self.table, 0, 0, 1, 1)
        self.lt_top.addWidget(self.fr_content)
        self.lt_central.addWidget(self.fr_top)
        self.lt_central.addWidget(self.line)
        self.lt_central.addWidget(self.fr_bottom)
        self.lt_dialog.addWidget(self.centralwidget, 0, 0, 1, 1)

    # metoda statyczna, tworzy dialog i wybrany ID, ok
    @staticmethod
    def showtable(model, parent=None):
        dialog = AreaList(model, parent)
        ok = dialog.exec_()
        return ok == QDialog.Accepted
