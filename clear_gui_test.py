import hashlib
import sys
import datetime

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont, QLinearGradient, QColor, QPolygonF, QBrush, QPen
from PyQt5.QtWidgets import QApplication

import slotbaza
from clear_gui import Ui_MainWindow


class Magazyn(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()


if __name__ == '__main__':
    app = QApplication([])
    magazyn = Magazyn()
    sys.exit(app.exec_())
