import sys
from tokenize import Whitespace
from webbrowser import BackgroundBrowser
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Element import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setGeometry(450, 200, 960, 540)
        self.setStyleSheet("background-color: #DBDBDB;")
        self.setFixedSize(1280, 800)
        self.setWindowTitle("ระบบคัดแยกคุณภาพผลทุเรียนอัตโนมัติ")
        self.setWindowIcon(QtGui.QIcon("pics/durian.png"))

        #---------------------------------------------------------------------------------------------------#

        self.bigTopic = Text(self, 0, "ระบบคัดแยกคุณภาพผลทุเรียน", 125, 78)
        self.bigTopic.setFontSize(21) 
        self.bigTopic.setSize(460, 50)
        self.bigTopic.setStyle("color: rgb(43, 43, 43); background-color: white; font-weight: bold;")

        self.ByTopic = Text(self, 0, "BY BLUEBLINK @FIBO KMUTT", 600, 100)
        self.ByTopic.setFontSize(7) 
        self.ByTopic.setSize(185, 18)
        self.ByTopic.setStyle("color: grey; background-color: white; font-weight: bold;") 

        self.PicTopic = Text(self, 0, "PICTURE", 160, 210)
        self.PicTopic.setFontSize(18) 
        self.PicTopic.setSize(131, 46)
        self.PicTopic.setStyle("color: rgb(56, 70, 9); background-color: white; font-weight: bold;") 

        self.DetailTopic = Text(self, 0, "DETAILS", 670, 210)
        self.DetailTopic.setFontSize(18) 
        self.DetailTopic.setSize(131, 46)
        self.DetailTopic.setStyle("color: rgb(56, 70, 9); background-color: white; font-weight: bold;") 

        self.WeightTopic = Text(self, 0, "น้ำหนักผลทุเรียน", 610, 300)
        self.WeightTopic.setFontSize(13) 
        self.WeightTopic.setSize(150, 30)
        self.WeightTopic.setStyle("color: rgb(56, 70, 9); background-color: white; font-weight: light;") 
        
        self.AmountTopic = Text(self, 0, "จำนวนพู", 795, 300)
        self.AmountTopic.setFontSize(13) 
        self.AmountTopic.setSize(150, 30)
        self.AmountTopic.setStyle("color: rgb(56, 70, 9); background-color: white; font-weight: light;") 

        self.PercentTopic = Text(self, 0, "เปอร์เซ็นต์น้ำหนักแห้ง", 970, 300)
        self.PercentTopic.setFontSize(13) 
        self.PercentTopic.setSize(210, 30)
        self.PercentTopic.setStyle("color: rgb(56, 70, 9); background-color: white; font-weight: light;") 

        self.WeightTopic1 = Text(self, 0, "กิโลกรัม", 610, 500)
        self.WeightTopic1.setFontSize(13) 
        self.WeightTopic1.setSize(150, 30)
        self.WeightTopic1.setStyle("color: rgb(56, 70, 9); background-color: white; font-weight: light;") 

        self.AmountTopic1 = Text(self, 0, "พู", 790, 500)
        self.AmountTopic1.setFontSize(13) 
        self.AmountTopic1.setSize(150, 30)
        self.AmountTopic1.setStyle("color: rgb(56, 70, 9); background-color: white; font-weight: light;") 
        
        self.PercentTopic1 = Text(self, 0, "เปอร์เซ็นต์", 990, 500)
        self.PercentTopic1.setFontSize(13) 
        self.PercentTopic1.setSize(150, 30)
        self.PercentTopic1.setStyle("color: rgb(56, 70, 9); background-color: white; font-weight: light;") 

        #---------------------------------------------------------------------------------------------------#
        
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    DurianUI = Window()
    sys.exit(app.exec_())