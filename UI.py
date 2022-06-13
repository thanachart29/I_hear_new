from cmath import e
import sys
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
        self.color = Color()

        #---------------------------------------------------------------------------------------------------#

        self.bigTopic = Text(self, 0, "ระบบคัดแยกคุณภาพผลทุเรียน", 125, 78)
        self.bigTopic.setFontSize(21) 
        self.bigTopic.setSize(460, 50)
        self.bigTopic.setStyle("color: {}; background-color: white; font-weight: bold;".format(self.color.darkGrey))

        self.ByTopic = Text(self, 0, "BY BLUEBLINK @FIBO KMUTT", 600, 100)
        self.ByTopic.setFontSize(7) 
        self.ByTopic.setSize(185, 18)
        self.ByTopic.setStyle("color: grey; background-color: white; font-weight: bold;") 

        self.PicTopic = Text(self, 0, "PICTURE", 160, 210)
        self.PicTopic.setFontSize(18) 
        self.PicTopic.setSize(131, 46)
        self.PicTopic.setStyle("color: {}; background-color: white; font-weight: bold;".format(self.color.darkGreen)) 

        self.DetailTopic = Text(self, 0, "DETAILS", 670, 210)
        self.DetailTopic.setFontSize(18) 
        self.DetailTopic.setSize(131, 46)
        self.DetailTopic.setStyle("color: {}; background-color: white; font-weight: bold;".format(self.color.darkGreen)) 

        self.WeightTopic = Text(self, 0, "น้ำหนักผลทุเรียน", 610, 300)
        self.WeightTopic.setFontSize(13) 
        self.WeightTopic.setSize(150, 30)
        self.WeightTopic.setStyle("color: {}; background-color: white; font-weight: light;".format(self.color.darkGreen)) 
        
        self.AmountTopic = Text(self, 0, "จำนวนพู", 795, 300)
        self.AmountTopic.setFontSize(13) 
        self.AmountTopic.setSize(150, 30)
        self.AmountTopic.setStyle("color: {}; background-color: white; font-weight: light;".format(self.color.darkGreen)) 

        self.PercentTopic = Text(self, 0, "เปอร์เซ็นต์น้ำหนักแห้ง", 970, 300)
        self.PercentTopic.setFontSize(13) 
        self.PercentTopic.setSize(210, 30)
        self.PercentTopic.setStyle("color: {}; background-color: white; font-weight: light;".format(self.color.darkGreen)) 

        self.WeightTopic1 = Text(self, 0, "กิโลกรัม", 605, 510)
        self.WeightTopic1.setFontSize(13) 
        self.WeightTopic1.setSize(150, 30)
        self.WeightTopic1.setStyle("color: {}; background-color: white; font-weight: light;".format(self.color.darkGreen)) 

        self.AmountTopic1 = Text(self, 0, "พู", 792, 510)
        self.AmountTopic1.setFontSize(13) 
        self.AmountTopic1.setSize(150, 30)
        self.AmountTopic1.setStyle("color: {}; background-color: white; font-weight: light;".format(self.color.darkGreen)) 
        
        self.PercentTopic1 = Text(self, 0, "เปอร์เซ็นต์", 990, 510)
        self.PercentTopic1.setFontSize(13) 
        self.PercentTopic1.setSize(150, 30)
        self.PercentTopic1.setStyle("color: {} ; background-color: white; font-weight: light;".format(self.color.darkGreen)) 

        #---------------------------------------------------------------------------------------------------#
        

        #---------------------------------------------------------------------------------------------------#

        self.show()

        #---------------------------------------------------------------------------------------------------#
        
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


        painter1 = QPainter(self)
        painter1.setPen(QPen(Qt.white))
        painter1.setBrush(QBrush(QColor(82, 137, 1, 170), Qt.SolidPattern))
        # For PicTitle
        painter1.drawRoundedRect(125, 225, 15, 15, 2.1, 2.1)
        # For DetailTitle
        painter1.drawRoundedRect(640, 225, 15, 15, 2.1, 2.1)


        painter2 = QPainter(self)
        painter2.setPen(QColor(150, 150, 150))
        painter2.setBrush(QBrush(QColor(150, 150, 150), Qt.SolidPattern))
        # For Grade
        painter2.drawRoundedRect(571, 586, 640, 110, 0, 0)
    
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    DurianUI = Window()
    sys.exit(app.exec_())