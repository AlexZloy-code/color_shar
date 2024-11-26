import sys

from random import randint
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import QtCore


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.printy)

    def printy(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            size = randint(20, 80)
            qp.setPen(QColor('#FFFF00'))
            qp.drawEllipse(QtCore.QPointF(randint(80, 120), randint(80, 120)), size, size)
            qp.drawEllipse(QtCore.QPointF(randint(200, 280), randint(200, 280)), size, size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())