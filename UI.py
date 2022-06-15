import sys
import math
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from Element import *

State = 0
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

class mainWindow(QDialog):
    def __init__(self):
        super().__init__()
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

        #---------------------------------------------------------------------------------------------------#

        # ระบบหยุดทำงานรอคำสั่งจากเครื่อง
        if (State == 0):
            self.PicTopic = Text(self, 0, "PICTURE", 160, 210)
            self.PicTopic.setFontSize(18) 
            self.PicTopic.setSize(131, 46)
            self.PicTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.blackGreen)) 

            self.DetailTopic = Text(self, 0, "DETAILS", 670, 210)
            self.DetailTopic.setFontSize(18) 
            self.DetailTopic.setSize(131, 46)
            self.DetailTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.blackGreen)) 

            self.WeightTopic = Text(self, 0, "น้ำหนักผลทุเรียน", 610, 300)
            self.WeightTopic.setFontSize(13) 
            self.WeightTopic.setSize(150, 30)
            self.WeightTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 

            self.WeightTopic1 = Text(self, 0, "กิโลกรัม", 605, 500)
            self.WeightTopic1.setFontSize(13) 
            self.WeightTopic1.setSize(150, 30)
            self.WeightTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 
            
            self.AmountTopic = Text(self, 0, "จำนวนพู", 795, 300)
            self.AmountTopic.setFontSize(13) 
            self.AmountTopic.setSize(150, 30)
            self.AmountTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 

            self.AmountTopic1 = Text(self, 0, "พู", 792, 500)
            self.AmountTopic1.setFontSize(13) 
            self.AmountTopic1.setSize(150, 30)
            self.AmountTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 

            self.PercentTopic = Text(self, 0, "เปอร์เซ็นต์น้ำหนักแห้ง", 973, 300)
            self.PercentTopic.setFontSize(13) 
            self.PercentTopic.setSize(210, 30)
            self.PercentTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 
            
            self.PercentTopic1 = Text(self, 0, "เปอร์เซ็นต์", 990, 500)
            self.PercentTopic1.setFontSize(13) 
            self.PercentTopic1.setSize(150, 30)
            self.PercentTopic1.setStyle("color: {} ; background-color: None; font-weight: light;".format(self.color.green)) 

            self.GradeTopic = Text(self, 0, "เกรดทุเรียน", 635, 607)
            self.GradeTopic.setFontSize(18) 
            self.GradeTopic.setSize(200, 60)
            self.GradeTopic.setStyle("color: white ; background-color: None; font-weight: Bold;") 

            self.GradeTopic1 = Text(self, 0, "GRADE", 838, 612)
            self.GradeTopic1.setFontSize(28) 
            self.GradeTopic1.setSize(200, 50)
            self.GradeTopic1.setStyle("color: white ; background-color: None; font-weight: Bold;")

            self.WeightVa = Text(self, 0, "0", 604, 365)
            self.WeightVa.setFontSize(40) 
            self.WeightVa.setSize(150, 100)
            self.WeightVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            self.AmountVa = Text(self, 0, "0", 793, 365)
            self.AmountVa.setFontSize(40) 
            self.AmountVa.setSize(150, 100)
            self.AmountVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            self.PercentVa = Text(self, 0, "0", 988, 365)
            self.PercentVa.setFontSize(40) 
            self.PercentVa.setSize(150, 100)
            self.PercentVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            self.GradeVa = Text(self, 0, "-", 988, 585)
            self.GradeVa.setFontSize(40) 
            self.GradeVa.setSize(150, 100)
            self.GradeVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.white)) 

            self.StateVa = Text(self, 0, "ระบบหยุดการทำงาน", 885, 55)
            self.StateVa.setFontSize(13) 
            self.StateVa.setSize(300, 100)
            self.StateVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkRed)) 

            self.setting = Button(self, 20, "  SETTING CRITERIA", 973, 745, self.gotoSettingWindow)
            self.setting.setFontSize(12) 
            self.setting.setSize(240, 40)
            self.setting.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))
            self.setting.Icon(QtGui.QIcon("icons/settings.png"))
        

        # ระบบกำลังประมวลผลข้อมูล
        if (State == 1):
            self.PicTopic = Text(self, 0, "PICTURE", 160, 210)
            self.PicTopic.setFontSize(18) 
            self.PicTopic.setSize(131, 46)
            self.PicTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.blackGreen)) 

            self.DetailTopic = Text(self, 0, "DETAILS", 670, 210)
            self.DetailTopic.setFontSize(18) 
            self.DetailTopic.setSize(131, 46)
            self.DetailTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.blackGreen)) 

            self.WeightTopic = Text(self, 0, "น้ำหนักผลทุเรียน", 610, 300)
            self.WeightTopic.setFontSize(13) 
            self.WeightTopic.setSize(150, 30)
            self.WeightTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 

            self.WeightTopic1 = Text(self, 0, "กิโลกรัม", 605, 500)
            self.WeightTopic1.setFontSize(13) 
            self.WeightTopic1.setSize(150, 30)
            self.WeightTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 
            
            self.AmountTopic = Text(self, 0, "จำนวนพู", 795, 300)
            self.AmountTopic.setFontSize(13) 
            self.AmountTopic.setSize(150, 30)
            self.AmountTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 

            self.AmountTopic1 = Text(self, 0, "พู", 792, 500)
            self.AmountTopic1.setFontSize(13) 
            self.AmountTopic1.setSize(150, 30)
            self.AmountTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 

            self.PercentTopic = Text(self, 0, "เปอร์เซ็นต์น้ำหนักแห้ง", 973, 300)
            self.PercentTopic.setFontSize(13) 
            self.PercentTopic.setSize(210, 30)
            self.PercentTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 
            
            self.PercentTopic1 = Text(self, 0, "เปอร์เซ็นต์", 990, 500)
            self.PercentTopic1.setFontSize(13) 
            self.PercentTopic1.setSize(150, 30)
            self.PercentTopic1.setStyle("color: {} ; background-color: None; font-weight: light;".format(self.color.green)) 

            self.GradeTopic = Text(self, 0, "เกรดทุเรียน", 635, 607)
            self.GradeTopic.setFontSize(18) 
            self.GradeTopic.setSize(200, 60)
            self.GradeTopic.setStyle("color: white ; background-color: None; font-weight: Bold;") 

            self.GradeTopic1 = Text(self, 0, "GRADE", 838, 612)
            self.GradeTopic1.setFontSize(28) 
            self.GradeTopic1.setSize(200, 50)
            self.GradeTopic1.setStyle("color: white ; background-color: None; font-weight: Bold;")

            self.WeightVa = Text(self, 0, "0", 604, 365)
            self.WeightVa.setFontSize(40) 
            self.WeightVa.setSize(150, 100)
            self.WeightVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            self.AmountVa = Text(self, 0, "0", 793, 365)
            self.AmountVa.setFontSize(40) 
            self.AmountVa.setSize(150, 100)
            self.AmountVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            self.PercentVa = Text(self, 0, "0", 988, 365)
            self.PercentVa.setFontSize(40) 
            self.PercentVa.setSize(150, 100)
            self.PercentVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

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
            self.PicTopic = Text(self, 0, "PICTURE", 160, 210)
            self.PicTopic.setFontSize(18) 
            self.PicTopic.setSize(131, 46)
            self.PicTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.blackGreen)) 

            self.DetailTopic = Text(self, 0, "DETAILS", 670, 210)
            self.DetailTopic.setFontSize(18) 
            self.DetailTopic.setSize(131, 46)
            self.DetailTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.blackGreen)) 

            self.WeightTopic = Text(self, 0, "น้ำหนักผลทุเรียน", 610, 300)
            self.WeightTopic.setFontSize(13) 
            self.WeightTopic.setSize(150, 30)
            self.WeightTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 

            self.WeightTopic1 = Text(self, 0, "กิโลกรัม", 605, 500)
            self.WeightTopic1.setFontSize(13) 
            self.WeightTopic1.setSize(150, 30)
            self.WeightTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 
            
            self.AmountTopic = Text(self, 0, "จำนวนพู", 795, 300)
            self.AmountTopic.setFontSize(13) 
            self.AmountTopic.setSize(150, 30)
            self.AmountTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 

            self.AmountTopic1 = Text(self, 0, "พู", 792, 500)
            self.AmountTopic1.setFontSize(13) 
            self.AmountTopic1.setSize(150, 30)
            self.AmountTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 

            self.PercentTopic = Text(self, 0, "เปอร์เซ็นต์น้ำหนักแห้ง", 973, 300)
            self.PercentTopic.setFontSize(13) 
            self.PercentTopic.setSize(210, 30)
            self.PercentTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.green)) 
            
            self.PercentTopic1 = Text(self, 0, "เปอร์เซ็นต์", 990, 500)
            self.PercentTopic1.setFontSize(13) 
            self.PercentTopic1.setSize(150, 30)
            self.PercentTopic1.setStyle("color: {} ; background-color: None; font-weight: light;".format(self.color.green)) 

            self.GradeTopic = Text(self, 0, "เกรดทุเรียน", 635, 607)
            self.GradeTopic.setFontSize(18) 
            self.GradeTopic.setSize(200, 60)
            self.GradeTopic.setStyle("color: white ; background-color: None; font-weight: Bold;") 

            self.GradeTopic1 = Text(self, 0, "GRADE", 838, 612)
            self.GradeTopic1.setFontSize(28) 
            self.GradeTopic1.setSize(200, 50)
            self.GradeTopic1.setStyle("color: white ; background-color: None; font-weight: Bold;")

            self.WeightVa = Text(self, 0, WeightValue, 604, 365)
            self.WeightVa.setFontSize(40) 
            self.WeightVa.setSize(150, 100)
            self.WeightVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            self.AmountVa = Text(self, 0, AmountValue, 793, 365)
            self.AmountVa.setFontSize(40) 
            self.AmountVa.setSize(150, 100)
            self.AmountVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

            self.PercentVa = Text(self, 0, PercentValue, 990, 365)
            self.PercentVa.setFontSize(40) 
            self.PercentVa.setSize(150, 100)
            self.PercentVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 

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

            self.setting = Button(self, 20, "  SETTING CRITERIA", 973, 745, self.gotoSettingWindow)
            self.setting.setFontSize(12) 
            self.setting.setSize(240, 40)
            self.setting.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))
            self.setting.Icon(QtGui.QIcon("icons/settings.png"))

    #---------------------------------------------------------------------------------------------------------------------------#

    def gotoSettingWindow(self):
        SettingWindow = settingWindow()
        widget.addWidget(SettingWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

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
        painter1.setBrush(QBrush(QColor(82, 94, 77), Qt.SolidPattern))
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

        #---------------------------------------------------------------------------------------------------#

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

        #---------------------------------------------------------------------------------------------------#

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

        #---------------------------------------------------------------------------------------------------#

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
   
class settingWindow(QDialog):
    def __init__(self):
        super().__init__()
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

        #---------------------------------------------------------------------------------------------------#

        self.settingTopic = Text(self, 0, "SETTING CRITERIA", 45, 210)
        self.settingTopic.setFontSize(18) 
        self.settingTopic.setSize(500, 46)
        self.settingTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.blackGreen)) 

        self.gradeTopic = Text(self, 0, "Select Grade", 130, 270)
        self.gradeTopic.setFontSize(13) 
        self.gradeTopic.setSize(150, 40)
        self.gradeTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))

        self.criteriaTopic = Text(self, 0, "Details for Criteria", 133, 330)
        self.criteriaTopic.setFontSize(13) 
        self.criteriaTopic.setSize(200, 40)
        self.criteriaTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))

        self.weightCriTopic = Text(self, 0, "น้ำหนักของทุเรียน", 125, 390)
        self.weightCriTopic.setFontSize(13) 
        self.weightCriTopic.setSize(250, 40)
        self.weightCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.weightCriTopic1 = Text(self, 0, "กิโลกรัม      ถึง", 504, 390)
        self.weightCriTopic1.setFontSize(13) 
        self.weightCriTopic1.setSize(250, 40)
        self.weightCriTopic1.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))
        
        self.weightCriTopic2 = Text(self, 0, "กิโลกรัม", 800, 390)
        self.weightCriTopic2.setFontSize(13) 
        self.weightCriTopic2.setSize(250, 40)
        self.weightCriTopic2.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.notSelect1 = Text(self, 0, "Not Select", 1000, 390)
        self.notSelect1.setFontSize(12) 
        self.notSelect1.setSize(250, 40)
        self.notSelect1.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.green))

        self.percentCriTopic = Text(self, 0, "เปอร์เซ็นต์น้ำหนักแห้ง", 143, 450)
        self.percentCriTopic.setFontSize(13) 
        self.percentCriTopic.setSize(250, 40)
        self.percentCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.percentCriTopic1 = Text(self, 0, "เปอร์เซ็นต์   ถึง", 503, 450)
        self.percentCriTopic1.setFontSize(13) 
        self.percentCriTopic1.setSize(250, 40)
        self.percentCriTopic1.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.percentCriTopic2 = Text(self, 0, "เปอร์เซ็นต์", 810, 450)
        self.percentCriTopic2.setFontSize(13) 
        self.percentCriTopic2.setSize(250, 40)
        self.percentCriTopic2.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.notSelect2 = Text(self, 0, "Not Select", 1000, 450)
        self.notSelect2.setFontSize(12) 
        self.notSelect2.setSize(250, 40)
        self.notSelect2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.green))

        self.amountCriTopic = Text(self, 0, "จำนวนพู", 84, 510)
        self.amountCriTopic.setFontSize(13) 
        self.amountCriTopic.setSize(250, 40)
        self.amountCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.notSelect3 = Text(self, 0, "Not Select", 1000, 510)
        self.notSelect3.setFontSize(12) 
        self.notSelect3.setSize(250, 40)
        self.notSelect3.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.green))

        self.badCriTopic = Text(self, 0, "จำนวนตำหนิ (รอยด่าง) ", 154, 570)
        self.badCriTopic.setFontSize(13) 
        self.badCriTopic.setSize(250, 40)
        self.badCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.notSelect4 = Text(self, 0, "Not Select", 1000, 570)
        self.notSelect4.setFontSize(12) 
        self.notSelect4.setSize(250, 40)
        self.notSelect4.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.green))

        self.shapeCriTopic = Text(self, 0, "รูปร่างของทุเรียน", 124, 630)
        self.shapeCriTopic.setFontSize(13) 
        self.shapeCriTopic.setSize(250, 40)
        self.shapeCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.notSelect5 = Text(self, 0, "Not Select", 1000, 630)
        self.notSelect5.setFontSize(12) 
        self.notSelect5.setSize(250, 40)
        self.notSelect5.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.green))

        #---------------------------------------------------------------------------------------------------#

        self.backToMain = Button(self, 20, "  BACK", 1013, 745, self.gotoMainWindow)
        self.backToMain.setFontSize(12) 
        self.backToMain.setSize(200, 40)
        self.backToMain.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))
        self.backToMain.Icon(QtGui.QIcon("icons/back.png"))

        self.save = Button(self, 20, "SAVE", 520, 685, self.saveCriteria)
        self.save.setFontSize(11) 
        self.save.setSize(120, 35)
        self.save.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.white, self.color.darkGreen))

        self.cancel = Button(self, 20, "CANCEL", 680, 685, self.cancelCriteria)
        self.cancel.setFontSize(11) 
        self.cancel.setSize(120, 35)
        self.cancel.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.white, self.color.darkGreen))

    #---------------------------------------------------------------------------------------------------------------------------#

    def gotoMainWindow(self):
        MainWindow    = mainWindow()
        widget.addWidget(MainWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #---------------------------------------------------------------------------------------------------------------------------#

    def saveCriteria(self):
        print("Save Value")
    
    #---------------------------------------------------------------------------------------------------------------------------#

    def cancelCriteria(self):
        print("Cancel Value")

    #---------------------------------------------------------------------------------------------------------------------------#
        
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        # For title
        painter.drawRoundedRect(67, 56, 776, 92, 20.0, 20.0)
        # For setting
        painter.drawRoundedRect(69, 181, 1142, 550, 7.0, 7.0)

        painter1 = QPainter(self)
        painter1.setPen(QPen(Qt.white))
        painter1.setBrush(QBrush(QColor(82, 94, 77), Qt.SolidPattern))
        # For PicTitle
        painter1.drawRoundedRect(125, 225, 15, 15, 2.1, 2.1)

        painter2 = QPainter(self)
        painter2.setPen(QPen(Qt.white))
        painter2.setBrush(QBrush(QColor(163, 184, 154, 100), Qt.SolidPattern))
        painter2.drawRoundedRect(135, 405, 12, 12, 2, 2)
        painter2.drawRoundedRect(135, 465, 12, 12, 2, 2)
        painter2.drawRoundedRect(135, 525, 12, 12, 2, 2)
        painter2.drawRoundedRect(135, 585, 12, 12, 2, 2)
        painter2.drawRoundedRect(135, 645, 12, 12, 2, 2)

#---------------------------------------------------------------------------------------------------------------------------#

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    MainWindow    = mainWindow()
    widget.addWidget(MainWindow)
    widget.setFixedSize(1280, 800)
    widget.show()
    sys.exit(app.exec_())