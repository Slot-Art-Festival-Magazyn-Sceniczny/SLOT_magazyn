from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QWidget, QGroupBox, QStatusBar, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QAction, QMenu, QMenuBar, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import QRect, Qt, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QBrush, QPolygonF, QPen
import sys, random


class UI_widget(QMainWindow):

    def setupUI(self):
        '''initiates application UI'''
        self.resize(1200, 900)
        self.setFixedSize(self.size())
        self.center()
        self.setWindowTitle('Magazyn Sceniczny')
        self.setStyleSheet("background-color: #555555; color: white\n")
        self.centralwidget = QWidget(self)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(0,21,1200,859)
        self.setframes()
        self.setmenus()
        self.setlogo()
        self.setgroupboxes()
        self.setbuttons()
        self.setloginstatus()
        self.setscena()
        self.setviewer()
        self.show()
        # self.showFullScreen()

    def setframes(self):
        self.frame_logo=QFrame(self.centralwidget)
        self.frame_logo.setGeometry(QRect(0, 0, 250, 150))
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")

        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setGeometry(QRect(0, 150, 241, 691))
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")

        self.frame_north = QFrame(self.centralwidget)
        self.frame_north.setGeometry(QRect(250, 0, 930, 50))
        self.frame_north.setFrameShape(QFrame.StyledPanel)
        self.frame_north.setFrameShadow(QFrame.Raised)
        self.frame_north.setObjectName("frame_north")

        self.frame_drawer = QFrame(self.centralwidget)
        self.frame_drawer.setGeometry(QRect(250, 50, 930, 800))
        self.frame_drawer.setFrameShape(QFrame.StyledPanel)
        self.frame_drawer.setFrameShadow(QFrame.Raised)
        self.frame_drawer.setObjectName("frame_drawer")

    def setgroupboxes(self):
        self.logging = QGroupBox(self.frame_menu)
        self.logging.setGeometry(QRect(10, 10, 221, 121))
        font = QFont()
        font.setPointSize(14)
        self.logging.setFont(font)
        self.logging.setStyleSheet("")
        self.logging.setAlignment(Qt.AlignCenter)
        self.logging.setFlat(False)
        self.logging.setCheckable(False)
        self.logging.setObjectName("logging")
        self.logging.setTitle('Logowanie')


        self.areaoperations = QGroupBox(self.frame_menu)
        self.areaoperations.setGeometry(QRect(10, 135, 221, 171))
        font = QFont()
        font.setPointSize(14)
        self.areaoperations.setFont(font)
        self.areaoperations.setAlignment(Qt.AlignCenter)
        self.areaoperations.setFlat(False)
        self.areaoperations.setCheckable(False)
        self.areaoperations.setObjectName("areaoperations")
        self.areaoperations.setTitle('Obszary')

        self.searching = QGroupBox(self.frame_menu)
        self.searching.setGeometry(QRect(10, 310, 221, 91))
        font = QFont()
        font.setPointSize(14)
        self.searching.setFont(font)
        self.searching.setAlignment(Qt.AlignCenter)
        self.searching.setFlat(False)
        self.searching.setCheckable(False)
        self.searching.setObjectName("searching")
        self.searching.setTitle('Wyszukiwanie')

        self.itemoperations = QGroupBox(self.frame_menu)
        self.itemoperations.setGeometry(QRect(10, 405, 221, 171))
        font = QFont()
        font.setPointSize(14)
        self.itemoperations.setFont(font)
        self.itemoperations.setAutoFillBackground(False)
        self.itemoperations.setStyleSheet("")
        self.itemoperations.setAlignment(Qt.AlignCenter)
        self.itemoperations.setFlat(False)
        self.itemoperations.setCheckable(False)
        self.itemoperations.setObjectName("itemoperations")
        self.itemoperations.setTitle('Obsługa klienta')

        self.other_modules = QGroupBox(self.frame_menu)
        self.other_modules.setGeometry(QRect(10, 580, 221, 91))
        font = QFont()
        font.setPointSize(14)
        self.other_modules.setFont(font)
        self.other_modules.setAutoFillBackground(False)
        self.other_modules.setStyleSheet("")
        self.other_modules.setAlignment(Qt.AlignCenter)
        self.other_modules.setFlat(False)
        self.other_modules.setCheckable(False)
        self.other_modules.setObjectName("other_modules")
        self.other_modules.setTitle('Inne moduły')

    def setbuttons(self):
        self.verticalLayout = QVBoxLayout(self.areaoperations)
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayout_3 = QVBoxLayout(self.searching)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayout_2 = QVBoxLayout(self.itemoperations)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout_4 = QVBoxLayout(self.other_modules)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.btn_login = QPushButton(self.logging)
        self.btn_login.setGeometry(QRect(10, 40, 91, 41))
        self.btn_login.setStyleSheet(self.button_stylesheet(''))
        self.btn_login.setObjectName("btn_login")
        self.btn_login.setText('Zaloguj')

        self.btn_logout = QPushButton(self.logging)
        self.btn_logout.setGeometry(QRect(120, 40, 91, 41))
        self.btn_logout.setStyleSheet(self.button_stylesheet(''))
        self.btn_logout.setObjectName("btn_logout")
        self.btn_logout.setText('Wyloguj')

        self.btn_listofareas = QPushButton(self.areaoperations)
        self.btn_listofareas.setMinimumSize(QSize(0, 40))
        self.btn_listofareas.setStyleSheet(self.button_stylesheet(''))
        self.btn_listofareas.setObjectName("btn_listofareas")
        self.btn_listofareas.setText('Lista obszarów')
        self.verticalLayout.addWidget(self.btn_listofareas)

        self.btn_areaedit = QPushButton(self.areaoperations)
        self.btn_areaedit.setMinimumSize(QSize(0, 40))
        self.btn_areaedit.setStyleSheet(self.button_stylesheet(''))
        self.btn_areaedit.setObjectName("btn_areaedit")
        self.btn_areaedit.setText('Edytuj obszar')
        self.verticalLayout.addWidget(self.btn_areaedit)

        self.btn_addarea = QPushButton(self.areaoperations)
        self.btn_addarea.setMinimumSize(QSize(0, 40))
        self.btn_addarea.setStyleSheet(self.button_stylesheet(''))
        self.btn_addarea.setObjectName("btn_addarea")
        self.btn_addarea.setText('Dodaj obszar')
        self.verticalLayout.addWidget(self.btn_addarea)

        self.btn_searchitem = QPushButton(self.searching)
        self.btn_searchitem.setMinimumSize(QSize(0, 40))
        self.btn_searchitem.setStyleSheet(self.button_stylesheet('blue'))
        self.btn_searchitem.setObjectName("btn_searchitem")
        self.btn_searchitem.setText('Wyszukaj przedmiot')
        self.verticalLayout_3.addWidget(self.btn_searchitem)

        self.btn_takealookinside = QPushButton(self.itemoperations)
        self.btn_takealookinside.setMinimumSize(QSize(0, 40))
        self.btn_takealookinside.setStyleSheet(self.button_stylesheet('yellow'))
        self.btn_takealookinside.setObjectName("btn_takealookinside")
        self.btn_takealookinside.setText('Zajrzyj do środka')
        self.verticalLayout_2.addWidget(self.btn_takealookinside)

        self.btn_comein = QPushButton(self.itemoperations)
        self.btn_comein.setMinimumSize(QSize(0, 40))
        self.btn_comein.setStyleSheet(self.button_stylesheet('green'))
        self.btn_comein.setObjectName("btn_comein")
        self.btn_comein.setText('Przyjmij przedmiot')
        self.verticalLayout_2.addWidget(self.btn_comein)

        self.btn_comeout = QPushButton(self.itemoperations)
        self.btn_comeout.setMinimumSize(QSize(0, 40))
        self.btn_comeout.setStyleSheet(self.button_stylesheet('red'))
        self.btn_comeout.setObjectName("btn_comoeout")
        self.btn_comeout.setText('Wydaj przedmiot')
        self.verticalLayout_2.addWidget(self.btn_comeout)

        self.btn_orchestra = QPushButton(self.other_modules)
        self.btn_orchestra.setMinimumSize(QSize(0, 40))
        self.btn_orchestra.setStyleSheet(self.button_stylesheet('violet'))
        self.btn_orchestra.setObjectName("btn_orchestra")
        self.btn_orchestra.setText('SLOT Orkiestra')
        self.verticalLayout_4.addWidget(self.btn_orchestra)

    def setloginstatus(self):
        self.logstatus = QLabel(self.logging)
        self.logstatus.setGeometry(QRect(10, 90, 201, 20))
        self.logstatus.setTextFormat(Qt.RichText)
        self.logstatus.setScaledContents(False)
        self.logstatus.setAlignment(Qt.AlignCenter)
        self.logstatus.setObjectName("logstatus")

    def button_stylesheet(self, color):
        if color=='red':
            stylesheet = "QPushButton {\n"\
                            "Font: Bold 10pt Arial ; color: white; \n"\
                            "border-style: solid; border-color: #222222; border-width: 1px; border-radius: 12px; \n"\
                            "background-color: qlineargradient(\n"\
                            "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #AD2D2D, stop:1 #842222)}\n"\
                            "QPushButton:hover { \n"\
                            "background-color: qlineargradient(\n"\
                            "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #BF3737, stop:1 #AD2D2D)}\n"\
                            "QPushButton:pressed { \n"\
                            "background-color: qlineargradient(\n"\
                            "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #842222, stop:1 #AD2D2D)}"
        elif color == 'yellow':
            stylesheet = "QPushButton {\n" \
                           "Font: Bold 10pt Arial ; color: white; \n" \
                           "border-style: solid; border-color: #222222; border-width: 1px; border-radius: 12px; \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #D39A37, stop:1 #A1752A)}\n" \
                           "QPushButton:hover { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #DDB043, stop:1 #D39A37)}\n" \
                           "QPushButton:pressed { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #A1752A, stop:1 #D39A37)}"
        elif color == 'green':
            stylesheet = "QPushButton {\n" \
                           "Font: Bold 10pt Arial ; color: white; \n" \
                           "border-style: solid; border-color: #222222; border-width: 1px; border-radius: 12px; \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2A8E25, stop:1 #206C1C)}\n" \
                           "QPushButton:hover { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #33A72D, stop:1 #2A8E25)}\n" \
                           "QPushButton:pressed { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #206C1C, stop:1 #2A8E25)}"
        elif color == 'blue':
            stylesheet = "QPushButton {\n" \
                           "Font: Bold 10pt Arial ; color: white; \n" \
                           "border-style: solid; border-color: #222222; border-width: 1px; border-radius: 12px; \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #355ACC, stop:1 #28449C)}\n" \
                           "QPushButton:hover { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #416ED7, stop:1 #355ACC)}\n" \
                           "QPushButton:pressed { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #28449C, stop:1 #355ACC)}"
        elif color == 'violet':
            stylesheet = "QPushButton {\n" \
                           "Font: Bold 10pt Arial ; color: white; \n" \
                           "border-style: solid; border-color: #222222; border-width: 1px; border-radius: 12px; \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #8931BC, stop:1 #68258F)}\n" \
                           "QPushButton:hover { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #A33CCB, stop:1 #8931BC)}\n" \
                           "QPushButton:pressed { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #68258F, stop:1 #8931BC)}"
        else:
            stylesheet = "QPushButton {\n" \
                           "Font: Bold 10pt Arial ; color: white; \n" \
                           "border-style: solid; border-color: #222222; border-width: 1px; border-radius: 12px; \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #444444, stop:1 #343434)}\n" \
                           "QPushButton:hover { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #535353, stop:1 #444444)}\n" \
                           "QPushButton:pressed { \n" \
                           "background-color: qlineargradient(\n" \
                           "spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #343434, stop:1 #444444)}"
        return stylesheet

    def setlogo(self):
        label=QLabel(self.frame_logo)
        pixmap=QPixmap('images/LOGO.png')
        label.setPixmap(pixmap)
        pass

    def setmenus(self):
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 1200, 21))
        self.menubar.setStyleSheet("QMenuBar::item:selected{background-color: #888888}")
        self.menubar.setObjectName("menubar")
        self.menuPlik = QMenu(self.menubar)
        self.menuPlik.setStyleSheet("QMenu:selected{background-color: #888888}\n"
                                    "")
        self.menuPlik.setObjectName("menuPlik")
        self.menuLogowanie = QMenu(self.menubar)
        self.menuLogowanie.setStyleSheet("QMenu:selected{background-color: #888888}\n"
                                         "")
        self.menuLogowanie.setObjectName("menuLogowanie")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("background-color: #AA5555; color: white\n")
        self.setStatusBar(self.statusbar)
        self.actionWczytaj = QAction(self)
        self.actionWczytaj.setObjectName("actionWczytaj")
        self.actionZapisz = QAction(self)
        self.actionZapisz.setObjectName("actionZapisz")
        self.actionWyj_cie = QAction(self)
        self.actionWyj_cie.setObjectName("actionWyj_cie")
        self.actionZaloguj = QAction(self)
        self.actionZaloguj.setObjectName("actionZaloguj")
        self.actionWyloguj = QAction(self)
        self.actionWyloguj.setObjectName("actionWyloguj")
        self.actionLista_u_ytkownik_w = QAction(self)
        self.actionLista_u_ytkownik_w.setObjectName("actionLista_u_ytkownik_w")
        self.menuPlik.addAction(self.actionWczytaj)
        self.menuPlik.addAction(self.actionZapisz)
        self.menuPlik.addAction(self.actionWyj_cie)
        self.menuLogowanie.addAction(self.actionZaloguj)
        self.menuLogowanie.addAction(self.actionWyloguj)
        self.menuLogowanie.addAction(self.actionLista_u_ytkownik_w)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuLogowanie.menuAction())

        self.menuPlik.setTitle("Plik")
        self.menuLogowanie.setTitle("Logowanie")
        self.actionWczytaj.setText("Wczytaj")
        self.actionZapisz.setText("Zapisz")
        self.actionWyj_cie.setText("Wyjście")
        self.actionZaloguj.setText("Zaloguj")
        self.actionWyloguj.setText("Wyloguj")
        self.actionLista_u_ytkownik_w.setText("Lista użytkowników")

    def setscena(self):
        self.scena=QGraphicsScene()
        self.scena.setSceneRect(0,0,1000,950)

    def setviewer(self):
        self.viewer=QGraphicsView(self.frame_drawer)
        self.viewer.setGeometry(0,0,910,772)
        self.viewer.setScene(self.scena)
        scale=0.75
        self.viewer.scale(scale,scale)
        self.viewer.setFrameShape(QFrame.StyledPanel)
        self.viewer.setFrameShadow(QFrame.Raised)


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


