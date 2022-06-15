import sys
import math
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from Element import *


State = 2 
# State 0 : ระบบหยุดการทำงาน
# State 1 : ระบบกำลังประมวลผล
# State 2 : ระบบทำงานเสร็จสมบูรณ์

# Parameter 
WeightValue  = "15"         # น้ำหนักของทุเรียน
AmountValue  = "2"          # จำนวนพู
PercentValue = "50"         # เปอร์เซ็นต์น้ำหนักแห้ง
GradeValue   = "A"          # เกรดของทุเรียน
PicAngle1    = 'pics/Durian1.jpg'
PicAngle2    = 'pics/Durian2.jpg'

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setGeometry(450, 200, 960, 540)
        self.setStyleSheet("background-color: #DBDBDB;")
        self.setFixedSize(1280, 800)
        self.setWindowTitle("ระบบคัดแยกคุณภาพผลทุเรียนอัตโนมัติ")
        self.setWindowIcon(QtGui.QIcon("icons/durian.png"))
        self.color = Color()

        #---------------------------------------------------------------------------------------------------#

        self.bigTopic = Text(self, 0, "ระบบคัดแยกคุณภาพผลทุเรียน", 125, 78)
        self.bigTopic.setFontSize(21) 
        self.bigTopic.setSize(460, 50)
        self.bigTopic.setStyle("color: {}; background-color: white; font-weight: bold;".format(self.color.darkGray))

        self.ByTopic = Text(self, 0, "BY BLUEBLINK @FIBO KMUTT", 600, 100)
        self.ByTopic.setFontSize(7) 
        self.ByTopic.setSize(185, 18)
        self.ByTopic.setStyle("color: gray; background-color: None; font-weight: bold;") 

        self.PicTopic = Text(self, 0, "PICTURE", 160, 210)
        self.PicTopic.setFontSize(18) 
        self.PicTopic.setSize(131, 46)
        self.PicTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 

        self.DetailTopic = Text(self, 0, "DETAILS", 670, 210)
        self.DetailTopic.setFontSize(18) 
        self.DetailTopic.setSize(131, 46)
        self.DetailTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 

        self.WeightTopic = Text(self, 0, "น้ำหนักผลทุเรียน", 610, 300)
        self.WeightTopic.setFontSize(13) 
        self.WeightTopic.setSize(150, 30)
        self.WeightTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 

        self.WeightTopic1 = Text(self, 0, "กิโลกรัม", 605, 500)
        self.WeightTopic1.setFontSize(13) 
        self.WeightTopic1.setSize(150, 30)
        self.WeightTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 
        
        self.AmountTopic = Text(self, 0, "จำนวนพู", 795, 300)
        self.AmountTopic.setFontSize(13) 
        self.AmountTopic.setSize(150, 30)
        self.AmountTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 

        self.AmountTopic1 = Text(self, 0, "พู", 792, 500)
        self.AmountTopic1.setFontSize(13) 
        self.AmountTopic1.setSize(150, 30)
        self.AmountTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 

        self.PercentTopic = Text(self, 0, "เปอร์เซ็นต์น้ำหนักแห้ง", 973, 300)
        self.PercentTopic.setFontSize(13) 
        self.PercentTopic.setSize(210, 30)
        self.PercentTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 
        
        self.PercentTopic1 = Text(self, 0, "เปอร์เซ็นต์", 990, 500)
        self.PercentTopic1.setFontSize(13) 
        self.PercentTopic1.setSize(150, 30)
        self.PercentTopic1.setStyle("color: {} ; background-color: None; font-weight: light;".format(self.color.darkGreen)) 

        self.GradeTopic = Text(self, 0, "เกรดทุเรียน", 635, 607)
        self.GradeTopic.setFontSize(18) 
        self.GradeTopic.setSize(200, 60)
        self.GradeTopic.setStyle("color: white ; background-color: None; font-weight: Bold;") 

        self.GradeTopic1 = Text(self, 0, "GRADE", 838, 612)
        self.GradeTopic1.setFontSize(28) 
        self.GradeTopic1.setSize(200, 50)
        self.GradeTopic1.setStyle("color: white ; background-color: None; font-weight: Bold;") 

        #---------------------------------------------------------------------------------------------------#
        
        # ระบบหยุดทำงานรอคำสั่งจากเครื่อง
        if (State == 0):
            self.WeightVa = Text(self, 0, "0", 604, 365)
            self.WeightVa.setFontSize(40) 
            self.WeightVa.setSize(150, 100)
            self.WeightVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.blackGreen)) 

            self.AmountVa = Text(self, 0, "0", 793, 365)
            self.AmountVa.setFontSize(40) 
            self.AmountVa.setSize(150, 100)
            self.AmountVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.blackGreen)) 

            self.PercentVa = Text(self, 0, "0", 988, 365)
            self.PercentVa.setFontSize(40) 
            self.PercentVa.setSize(150, 100)
            self.PercentVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.blackGreen)) 

            self.GradeVa = Text(self, 0, "-", 988, 585)
            self.GradeVa.setFontSize(40) 
            self.GradeVa.setSize(150, 100)
            self.GradeVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.white)) 

            self.StateVa = Text(self, 0, "ระบบหยุดการทำงาน", 885, 55)
            self.StateVa.setFontSize(13) 
            self.StateVa.setSize(300, 100)
            self.StateVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkRed)) 
        

        # ระบบกำลังประมวลผลข้อมูล
        if (State == 1):
            self.WeightVa = Text(self, 0, "0", 604, 365)
            self.WeightVa.setFontSize(40) 
            self.WeightVa.setSize(150, 100)
            self.WeightVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.blackGreen)) 

            self.AmountVa = Text(self, 0, "0", 793, 365)
            self.AmountVa.setFontSize(40) 
            self.AmountVa.setSize(150, 100)
            self.AmountVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.blackGreen)) 

            self.PercentVa = Text(self, 0, "0", 988, 365)
            self.PercentVa.setFontSize(40) 
            self.PercentVa.setSize(150, 100)
            self.PercentVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.blackGreen)) 

            self.GradeVa = Text(self, 0, "-", 988, 585)
            self.GradeVa.setFontSize(40) 
            self.GradeVa.setSize(150, 100)
            self.GradeVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.white)) 

            self.StateVa = Text(self, 0, "ระบบกำลังประมวลผล", 885, 55)
            self.StateVa.setFontSize(13) 
            self.StateVa.setSize(300, 100)
            self.StateVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkYellow)) 


        # ระบบทำงานเสร็จสมบูรณ์ แสดงข้อมูลที่เกี่ยวข้อง
        if (State == 2):
            self.WeightVa = Text(self, 0, WeightValue, 604, 365)
            self.WeightVa.setFontSize(40) 
            self.WeightVa.setSize(150, 100)
            self.WeightVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.blackGreen)) 

            self.AmountVa = Text(self, 0, AmountValue, 793, 365)
            self.AmountVa.setFontSize(40) 
            self.AmountVa.setSize(150, 100)
            self.AmountVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.blackGreen)) 

            self.PercentVa = Text(self, 0, PercentValue, 990, 365)
            self.PercentVa.setFontSize(40) 
            self.PercentVa.setSize(150, 100)
            self.PercentVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.blackGreen)) 

            self.GradeVa = Text(self, 0, GradeValue, 990, 587)
            self.GradeVa.setFontSize(38) 
            self.GradeVa.setSize(150, 100)
            self.GradeVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.white)) 

            self.StateVa = Text(self, 0, "ระบบทำงานเสร็จสมบูรณ์", 885, 55)
            self.StateVa.setFontSize(13) 
            self.StateVa.setSize(300, 100)
            self.StateVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            self.Pic1 = Text(self, 0, "ภาพมุมที่ 1", 42, 640)
            self.Pic1.setFontSize(10) 
            self.Pic1.setSize(300, 100)
            self.Pic1.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            self.Pic2 = Text(self, 0, "ภาพมุมที่ 2", 272, 640)
            self.Pic2.setFontSize(10) 
            self.Pic2.setSize(300, 100)
            self.Pic2.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            high_rez = QtCore.QSize(216, 384)
            self.label = QLabel(self)
            self.pixmap1 = QPixmap(PicAngle1)
            self.pixmap1 = self.pixmap1.scaled(high_rez)
            self.label.setPixmap(self.pixmap1)
            self.label.resize(self.pixmap1.width(), self.pixmap1.height())
            self.label.move(86, 270)

            self.label = QLabel(self)
            self.pixmap2 = QPixmap(PicAngle2)
            self.pixmap2 = self.pixmap2.scaled(high_rez)
            self.label.setPixmap(self.pixmap2)
            self.label.resize(self.pixmap2.width(), self.pixmap2.height())
            self.label.move(317, 270)

        #---------------------------------------------------------------------------------------------------#

        self.setting = Button(self, 20, "SETTING CRITERIA", 992, 745)
        self.setting.setFontSize(12) 
        self.setting.setSize(220, 40)
        self.setting.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))
        self.setting.Icon(QtGui.QIcon("icons/settings.png"))
        self.show()


    #---------------------------------------------------------------------------------------------------------------------------#
        
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        # For title
        painter.drawRoundedRect(67, 56, 1142, 92, 20.0, 20.0)
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
        painter2.drawRoundedRect(571, 581, 640, 110, 0, 0)


        painter3 = QPainter(self)
        painter3.setPen(QPen(QColor(140, 160, 50, 100), 2.5))
        painter3.setBrush(QBrush(QColor(140, 160, 50, 100)))
        # For line
        painter3.drawLine(795, 290, 795, 550)
        # For line
        painter3.drawLine(945, 290, 945, 550)


        if (State == 0):
            painter4 = QPainter(self)
            painter4.setPen(QPen(QColor(211, 47, 47, 25)))
            painter4.setBrush(QBrush(QColor(211, 47, 47, 25), Qt.SolidPattern))
            # For status
            painter4.drawRoundedRect(840, 74, 350, 60, 20.0, 20.0)

            painter5 = QPainter(self)
            painter5.setPen(QPen(QColor(211, 47, 47)))
            painter5.setBrush(QBrush(QColor(211, 47, 47), Qt.SolidPattern))
            # For title
            painter5.drawEllipse(870, 91, 28, 28)

        if (State == 1):
            painter4 = QPainter(self)
            painter4.setPen(QPen(QColor(255, 210, 85, 25)))
            painter4.setBrush(QBrush(QColor(255, 210, 85, 25), Qt.SolidPattern))
            # For status
            painter4.drawRoundedRect(840, 74, 350, 60, 20.0, 20.0)

            painter5 = QPainter(self)
            painter5.setPen(QPen(QColor(255, 210, 85)))
            painter5.setBrush(QBrush(QColor(255, 210, 85), Qt.SolidPattern))
            # For title
            painter5.drawEllipse(870, 91, 28, 28)

        if (State == 2):
            painter4 = QPainter(self)
            painter4.setPen(QPen(QColor(163, 195, 48, 25)))
            painter4.setBrush(QBrush(QColor(163, 195, 48, 25), Qt.SolidPattern))
            # For status
            painter4.drawRoundedRect(840, 74, 350, 60, 20.0, 20.0)

            painter5 = QPainter(self)
            painter5.setPen(QPen(QColor(82, 137, 1)))
            painter5.setBrush(QBrush(QColor(82, 137, 1), Qt.SolidPattern))
            # For title
            painter5.drawEllipse(870, 91, 28, 28)

   #---------------------------------------------------------------------------------------------------------------------------#


   #---------------------------------------------------------------------------------------------------------------------------# 
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    DurianUI = Window()
    sys.exit(app.exec_())