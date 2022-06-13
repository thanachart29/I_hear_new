from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont, QFontDatabase
from PyQt5.QtCore import Qt
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setGeometry(450, 200, 960, 540)
        self.setStyleSheet("background-color: #DBDBDB;")
        self.setFixedSize(1280, 800)
        self.setWindowTitle("ระบบคัดแยกคุณภาพผลทุเรียนอัตโนมัติ")
        self.setWindowIcon(QtGui.QIcon("pic/durian.png"))
        self.show()
        
    
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        # For title
        painter.drawRoundedRect(67, 56, 776, 92, 20.0, 20.0)
        # For status
        painter.drawRoundedRect(860, 56, 351, 92, 20.0, 20.0)
        # For picture
        painter.drawRoundedRect(69, 181, 480, 550, 7.0, 7.0)
        # For details
        painter.drawRoundedRect(571, 181, 640, 550, 7.0, 7.0)

    def addText(self):
        font = QFont()
        font.setFamily('Tahoma')
        mainText = QLabel('ระบบคัดแยกผลทุเรียนอัตโนมัติ',window)
        mainText.setFont(font)
        mainText.move(129, 83)
        
if __name__ == '__main__':
    # create pyQt5 app
    app = QApplication(sys.argv)

    # create the instance of window
    window = Window()
    window.show()

    # start the app
    sys.exit(app.exec_())