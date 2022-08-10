from lib2to3.pgen2.pgen import ParserGenerator
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QComboBox, QHBoxLayout
from Element import *

#-----------------------------------------------------------------------------------------------------------#

     # State 0 : ระบบหยุดการทำงาน          >> เริ่มการทำงานของเครื่องใหม่ กด start เข้า state 1
     # State 1 : ระบบกำลังประมวลผล         >> เครื่องกำลังทำงาน กด emer or pause เข้่า state 2
     # State 2 : ระบบหยุุดการทำงานชั่วคราว    >> ปลด emer or resume เข้า state 1
     # State 3 : ระบบทำงานเสร็จสมบูรณ์       >> เครื่องทำงานเสร็จ กด finish เข้า state 0
process     = state('3') 

#-----------------------------------------------------------------------------------------------------------#

     # Parameter Input
WeightValue     = "1.5"                     
AmountValue     = "6"  
PerBadValue     = "0"                    
PerShapeValue   = "78"    
HardnessValue   = 1                                
PicAngle1       = 'pics/Durian1.jpg'
PicAngle2       = 'pics/Durian2.jpg'

#-----------------------------------------------------------------------------------------------------------#

     # Do not change!!! : setting parameter init

extraClass      = criteriaDurian('E', '0', '0', '0', '0', '0', '0', '0', '0', '0')
classI          = criteriaDurian('I', '0', '0', '0', '0', '0', '0', '0', '0', '0')
classII         = criteriaDurian('II', '0', '0', '0', '0', '0', '0', '0', '0', '0')

extraClassSave  = criteriaDurian('E', '1.5', '6', '     มากกว่าหรือเท่ากับ', '4', '0', '0', '91', '100', '1')
classISave      = criteriaDurian('I', '1.5', '6', '     มากกว่าหรือเท่ากับ', '3', '0', '10', '81', '90', '1')
classIISave     = criteriaDurian('II', '1.5', '6', '     มากกว่าหรือเท่ากับ', '2', '0', '10', '71', '80', '1')

#-----------------------------------------------------------------------------------------------------------#

extraClass.claDurian = 'E'
extraClass.weightInitDurian         = extraClassSave.weightInitDurian
extraClass.weightFinalDurian        = extraClassSave.weightFinalDurian
extraClass.perBadInitDurian         = extraClassSave.perBadInitDurian
extraClass.perBadFinalDurian        = extraClassSave.perBadFinalDurian
extraClass.perShapeInitDurian       = extraClassSave.perShapeInitDurian
extraClass.perShapeFinalDurian      = extraClassSave.perShapeFinalDurian
extraClass.amountDurian             = extraClassSave.amountDurian
extraClass.HTUAmountDurian          = extraClassSave.HTUAmountDurian

classI.claDurian = 'I'
classI.weightInitDurian             = classISave.weightInitDurian
classI.weightFinalDurian            = classISave.weightFinalDurian
classI.perBadInitDurian             = classISave.perBadInitDurian
classI.perBadFinalDurian            = classISave.perBadFinalDurian
classI.perShapeInitDurian           = classISave.perShapeInitDurian
classI.perShapeFinalDurian          = classISave.perShapeFinalDurian
classI.amountDurian                 = classISave.amountDurian
classI.HTUAmountDurian              = classISave.HTUAmountDurian

classII.claDurian = 'II'
classII.weightInitDurian            = classIISave.weightInitDurian
classII.weightFinalDurian           = classIISave.weightFinalDurian
classII.perBadInitDurian            = classIISave.perBadInitDurian
classII.perBadFinalDurian           = classIISave.perBadFinalDurian
classII.perShapeInitDurian          = classIISave.perShapeInitDurian
classII.perShapeFinalDurian         = classIISave.perShapeFinalDurian
classII.amountDurian                = classIISave.amountDurian
classII.HTUAmountDurian             = classIISave.HTUAmountDurian

#-----------------------------------------------------------------------------------------------------------#

ECheck      = criteriaCheck(1, 1, 1, 1)
ICheck      = criteriaCheck(1, 1, 1, 1)
IICheck     = criteriaCheck(1, 1, 1, 1)

ECheckSave  = criteriaCheck(1, 1, 1, 1)
ICheckSave  = criteriaCheck(1, 1, 1, 1)
IICheckSave = criteriaCheck(1, 1, 1, 1)

#-----------------------------------------------------------------------------------------------------------#


class mainWindow(QMainWindow):
    
    def Detail(self):
        self.color = Color()
        self.PicTopic = Text(self, 0, "PICTURE", 160, 210)
        self.PicTopic.setFontSize(18) 
        self.PicTopic.setSize(131, 46)
        self.PicTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.blackGreen)) 

        self.DetailTopic = Text(self, 0, "DETAILS", 670, 210)
        self.DetailTopic.setFontSize(18) 
        self.DetailTopic.setSize(131, 46)
        self.DetailTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.blackGreen)) 

        self.WeightTopic = Text(self, 0, "น้ำหนักผลทุเรียน", 630, 280)
        self.WeightTopic.setFontSize(11) 
        self.WeightTopic.setSize(150, 30)
        self.WeightTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 

        self.AmountTopic = Text(self, 0, "จำนวนพูสมบูรณ์", 630, 330)
        self.AmountTopic.setFontSize(11) 
        self.AmountTopic.setSize(150, 30)
        self.AmountTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))          

        self.PerBadTopic = Text(self, 0, "เปอร์เซ็นต์ตำหนิ", 630, 380)
        self.PerBadTopic.setFontSize(11) 
        self.PerBadTopic.setSize(150, 30)
        self.PerBadTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))     

        self.PerShapeTopic = Text(self, 0, "เปอร์เซ็นต์ความสมมาตร", 630, 430)
        self.PerShapeTopic.setFontSize(11) 
        self.PerShapeTopic.setSize(190, 30)
        self.PerShapeTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 

        self.HardnessTopic = Text(self, 0, "ลักษณะเนื้อทุเรียน", 630, 480)
        self.HardnessTopic.setFontSize(11) 
        self.HardnessTopic.setSize(190, 30)
        self.HardnessTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 

        self.CodeWeightTopic = Text(self, 0, "รหัสขนาด", 630, 530)
        self.CodeWeightTopic.setFontSize(11) 
        self.CodeWeightTopic.setSize(190, 30)
        self.CodeWeightTopic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 

        self.WeightTopic1 = Text(self, 0, "กิโลกรัม", 1060, 280)
        self.WeightTopic1.setFontSize(11) 
        self.WeightTopic1.setSize(150, 30)
        self.WeightTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen)) 

        self.AmountTopic1 = Text(self, 0, "พู", 1060, 330)
        self.AmountTopic1.setFontSize(11) 
        self.AmountTopic1.setSize(150, 30)
        self.AmountTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))          

        self.PerBadTopic1 = Text(self, 0, "เปอร์เซ็นต์", 1060, 380)
        self.PerBadTopic1.setFontSize(11) 
        self.PerBadTopic1.setSize(150, 30)
        self.PerBadTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))     

        self.PerShapeTopic1 = Text(self, 0, "เปอร์เซ็นต์", 1060, 430)
        self.PerShapeTopic1.setFontSize(11) 
        self.PerShapeTopic1.setSize(190, 30)
        self.PerShapeTopic1.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))

        self.Topic = Text(self, 0, "=", 870, 280)
        self.Topic.setFontSize(11) 
        self.Topic.setSize(190, 30)
        self.Topic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))      

        self.Topic = Text(self, 0, "=", 870, 330)
        self.Topic.setFontSize(11) 
        self.Topic.setSize(190, 30)
        self.Topic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))

        self.Topic = Text(self, 0, "=", 870, 380)
        self.Topic.setFontSize(11) 
        self.Topic.setSize(190, 30)
        self.Topic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))      

        self.Topic = Text(self, 0, "=", 870, 430)
        self.Topic.setFontSize(11) 
        self.Topic.setSize(190, 30)
        self.Topic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))

        self.Topic = Text(self, 0, "=", 870, 480)
        self.Topic.setFontSize(11) 
        self.Topic.setSize(190, 30)
        self.Topic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))

        self.Topic = Text(self, 0, "=", 870, 530)
        self.Topic.setFontSize(11) 
        self.Topic.setSize(190, 30)
        self.Topic.setStyle("color: {}; background-color: None; font-weight: light;".format(self.color.darkGreen))

        self.ClassTopic1 = Text(self, 0, "CLASS ทุเรียน", 650, 613)
        self.ClassTopic1.setFontSize(18) 
        self.ClassTopic1.setSize(200, 60)
        self.ClassTopic1.setStyle("color: white ; background-color: None; font-weight: Bold;")      
    
    #---------------------------------------------------------------------------------------------------------------------------#

    def NumberInDetail(self):
        self.color = Color() 

        self.WeightTopic2 = Text(self, 0, "0", 890, 280)
        self.WeightTopic2.setFontSize(13) 
        self.WeightTopic2.setSize(150, 30)
        self.WeightTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))
        self.WeightTopic2.setAlignment(Qt.AlignCenter) 

        self.AmountTopic2 = Text(self, 0, "0", 890, 330)
        self.AmountTopic2.setFontSize(13) 
        self.AmountTopic2.setSize(150, 30)
        self.AmountTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))  
        self.AmountTopic2.setAlignment(Qt.AlignCenter)         

        self.PerBadTopic2 = Text(self, 0, "0", 890, 380)
        self.PerBadTopic2.setFontSize(13) 
        self.PerBadTopic2.setSize(150, 30)
        self.PerBadTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))     
        self.PerBadTopic2.setAlignment(Qt.AlignCenter) 

        self.PerShapeTopic2 = Text(self, 0, "0", 890, 430)
        self.PerShapeTopic2.setFontSize(13) 
        self.PerShapeTopic2.setSize(150, 30)
        self.PerShapeTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
        self.PerShapeTopic2.setAlignment(Qt.AlignCenter) 

        self.HardnessTopic2 = Text(self, 0, "-", 890, 480)
        self.HardnessTopic2.setFontSize(13) 
        self.HardnessTopic2.setSize(150, 30)
        self.HardnessTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
        self.HardnessTopic2.setAlignment(Qt.AlignCenter) 

        self.CodeWeightTopic2 = Text(self, 0, "-", 890, 530)
        self.CodeWeightTopic2.setFontSize(13) 
        self.CodeWeightTopic2.setSize(150, 30)
        self.CodeWeightTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
        self.CodeWeightTopic2.setAlignment(Qt.AlignCenter) 

        self.ClassTopic2 = Text(self, 0, "-", 960, 605)
        self.ClassTopic2.setFontSize(24) 
        self.ClassTopic2.setSize(300, 60)
        self.ClassTopic2.setStyle("color: white ; background-color: None; font-weight: Bold;")   

    #---------------------------------------------------------------------------------------------------------------------------#

    def NumberInDetail1(self):
        self.color = Color() 

        self.WeightTopic2 = Text(self, 0, WeightValue, 890, 280)
        self.WeightTopic2.setFontSize(13) 
        self.WeightTopic2.setSize(150, 30)
        self.WeightTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))
        self.WeightTopic2.setAlignment(Qt.AlignCenter) 

        self.AmountTopic2 = Text(self, 0, AmountValue, 890, 330)
        self.AmountTopic2.setFontSize(13) 
        self.AmountTopic2.setSize(150, 30)
        self.AmountTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))  
        self.AmountTopic2.setAlignment(Qt.AlignCenter)         

        self.PerBadTopic2 = Text(self, 0, PerBadValue, 890, 380)
        self.PerBadTopic2.setFontSize(13) 
        self.PerBadTopic2.setSize(150, 30)
        self.PerBadTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))     
        self.PerBadTopic2.setAlignment(Qt.AlignCenter) 

        self.PerShapeTopic2 = Text(self, 0, PerShapeValue, 890, 430)
        self.PerShapeTopic2.setFontSize(13) 
        self.PerShapeTopic2.setSize(150, 30)
        self.PerShapeTopic2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
        self.PerShapeTopic2.setAlignment(Qt.AlignCenter) 

    #---------------------------------------------------------------------------------------------------------------------------#

    def outputOut(self):
        self.ClassTopic = Text(self, 0, "OUT", 900, 605)
        self.ClassTopic.setFontSize(24) 
        self.ClassTopic.setSize(300, 60)
        self.ClassTopic.setStyle("color: white ; background-color: None; font-weight: Bold;")   

    #---------------------------------------------------------------------------------------------------------------------------#

    def outputExtra(self):
        self.ClassTopic1 = Text(self, 0, "EXTRA CLASS", 860, 605)
        self.ClassTopic1.setFontSize(24) 
        self.ClassTopic1.setSize(300, 60)
        self.ClassTopic1.setStyle("color: white ; background-color: None; font-weight: Bold;") 
        self.ClassTopic1.setAlignment(Qt.AlignCenter)

    #---------------------------------------------------------------------------------------------------------------------------#

    def outputClassI(self):
        self.ClassTopic2 = Text(self, 0, "CLASS I", 900, 605)
        self.ClassTopic2.setFontSize(24) 
        self.ClassTopic2.setSize(300, 60)
        self.ClassTopic2.setStyle("color: white ; background-color: None; font-weight: Bold;")    

    #---------------------------------------------------------------------------------------------------------------------------#

    def outputClassII(self):    
        self.ClassTopic3 = Text(self, 0, "CLASS II", 900, 605)
        self.ClassTopic3.setFontSize(24) 
        self.ClassTopic3.setSize(300, 60)
        self.ClassTopic3.setStyle("color: white ; background-color: None; font-weight: Bold;")   

    #---------------------------------------------------------------------------------------------------------------------------#

    def __init__(self, parent = None):
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
        self.bigTopic.setAlignment(Qt.AlignCenter)


        self.ByTopic = Text(self, 0, "BY BLUEBLINK @FIBO KMUTT", 600, 100)
        self.ByTopic.setFontSize(7) 
        self.ByTopic.setSize(185, 18)
        self.ByTopic.setStyle("color: gray; background-color: None; font-weight: bold;") 
        self.ByTopic.setAlignment(Qt.AlignCenter)

        #---------------------------------------------------------------------------------------------------#

        # ระบบหยุดทำงานรอคำสั่งจากเครื่อง
        if (process.stateProcess == '0'):
            self.Detail()
            self.NumberInDetail()
            self.StateVa = Text(self, 0, "ระบบหยุดการทำงาน", 885, 55)
            self.StateVa.setFontSize(13) 
            self.StateVa.setSize(300, 100)
            self.StateVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkRed)) 
            self.StateVa.setAlignment(Qt.AlignCenter)

            self.setting = Button(self, 20, "  SETTING CRITERIA", 973, 745, self.gotoSettingWindow, QtCore.Qt.PointingHandCursor)
            self.setting.setFontSize(12) 
            self.setting.setSize(240, 40)
            self.setting.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))
            self.setting.Icon(QtGui.QIcon("icons/settings.png"))

            self.start = Button(self, 20, "START", 825, 745, self.runProgram, QtCore.Qt.PointingHandCursor)
            self.start.setFontSize(12) 
            self.start.setSize(120, 40)
            self.start.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))

        #---------------------------------------------------------------------------------------------------#

        # ระบบกำลังประมวลผลข้อมูล
        if (process.stateProcess == '1'):
            self.Detail()
            self.NumberInDetail()
            self.StateVa = Text(self, 0, "ระบบกำลังประมวลผล", 885, 55)
            self.StateVa.setFontSize(13) 
            self.StateVa.setSize(300, 100)
            self.StateVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkYellow)) 
            self.StateVa.setAlignment(Qt.AlignCenter)

            self.pause = Button(self, 20, "PAUSE", 825, 745, self.pauseProgram, QtCore.Qt.PointingHandCursor)
            self.pause.setFontSize(12) 
            self.pause.setSize(120, 40)
            self.pause.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))

        #---------------------------------------------------------------------------------------------------#

        #ระบบหยุดการทำงานชั่วคราว
        if (process.stateProcess == '2'):
            self.Detail()
            self.NumberInDetail()
            self.StateVa = Text(self, 0, "ระบบหยุดการทำงานชั่วคราว", 885, 55)
            self.StateVa.setFontSize(13) 
            self.StateVa.setSize(300, 100)
            self.StateVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkOrange)) 
            self.StateVa.setAlignment(Qt.AlignCenter)

            self.resume = Button(self, 20, "RESUME", 825, 745, self.resumeProgram, QtCore.Qt.PointingHandCursor)
            self.resume.setFontSize(12) 
            self.resume.setSize(120, 40)
            self.resume.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))

            self.setting = Button(self, 20, "  SETTING CRITERIA", 973, 745, self.gotoSettingWindow, QtCore.Qt.PointingHandCursor)
            self.setting.setFontSize(12) 
            self.setting.setSize(240, 40)
            self.setting.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))
            self.setting.Icon(QtGui.QIcon("icons/settings.png"))

        #---------------------------------------------------------------------------------------------------#

        # ระบบทำงานเสร็จสมบูรณ์ แสดงข้อมูลที่เกี่ยวข้อง
        if (process.stateProcess == '3'):
            self.Detail()
            self.NumberInDetail1()

            # check ลักษณะเนื้อทุเรียน
            if(HardnessValue == 1):
                self.Hardness = Text(self, 0, "เนื้อแข็ง", 895, 480)
                self.Hardness.setFontSize(13) 
                self.Hardness.setSize(150, 30)
                self.Hardness.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
                self.Hardness.setAlignment(Qt.AlignCenter) 
            elif(HardnessValue == 0):
                self.Hardness = Text(self, 0, "เนื้ออ่อน", 895, 480)
                self.Hardness.setFontSize(13) 
                self.Hardness.setSize(150, 30)
                self.Hardness.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
                self.Hardness.setAlignment(Qt.AlignCenter)                 


            # check รหัสขนาดของทุเรียน
            if(float(WeightValue) > 4.0):
                self.Code = Text(self, 0, "1", 890, 530)
                self.Code.setFontSize(13) 
                self.Code.setSize(150, 30)
                self.Code.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
                self.Code.setAlignment(Qt.AlignCenter)  
            elif(float(WeightValue) > 3.0 and float(WeightValue) <= 4.0):
                self.Code = Text(self, 0, "2", 890, 530)
                self.Code.setFontSize(13) 
                self.Code.setSize(150, 30)
                self.Code.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
                self.Code.setAlignment(Qt.AlignCenter)        
            elif(float(WeightValue) > 2.0 and float(WeightValue) <= 3.0):
                self.Code = Text(self, 0, "3", 890, 530)
                self.Code.setFontSize(13) 
                self.Code.setSize(150, 30)
                self.Code.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
                self.Code.setAlignment(Qt.AlignCenter)     
            elif(float(WeightValue) > 1.0 and float(WeightValue) <= 2.0):
                self.Code = Text(self, 0, "4", 890, 530)
                self.Code.setFontSize(13) 
                self.Code.setSize(150, 30)
                self.Code.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
                self.Code.setAlignment(Qt.AlignCenter)      
            elif(float(WeightValue) > 0.5 and float(WeightValue) <= 1.0):
                self.Code = Text(self, 0, "5", 890, 530)
                self.Code.setFontSize(13) 
                self.Code.setSize(150, 30)
                self.Code.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen)) 
                self.Code.setAlignment(Qt.AlignCenter)                      


            # Check Class
            if(HardnessValue == 1):

                # Extra Class
                if((float(WeightValue) >= float(extraClassSave.weightInitDurian) and float(WeightValue) <= float(extraClassSave.weightFinalDurian)) and (float(PerBadValue) >= float(extraClassSave.perBadInitDurian) and float(PerBadValue) <= float(extraClassSave.perBadFinalDurian)) and (float(PerShapeValue) >= float(extraClassSave.perShapeInitDurian) and float(PerShapeValue) <= float(extraClassSave.perShapeFinalDurian))):
                    if(extraClassSave.HTUAmountDurian == '     มากกว่าหรือเท่ากับ'):
                        if(float(AmountValue) >= float(extraClassSave.amountDurian)):
                            self.outputExtra()
                        else:
                            self.outputOut()
                    elif(extraClassSave.HTUAmountDurian == '     มากกว่า'):
                        if(float(AmountValue) > float(extraClassSave.amountDurian)):
                            self.outputExtra()
                        else:
                            self.outputOut()
                    elif(extraClassSave.HTUAmountDurian == '     เท่ากับ'):
                        if(float(AmountValue) == float(extraClassSave.amountDurian)):
                            self.outputExtra()
                        else:
                            self.outputOut()
                    elif(extraClassSave.HTUAmountDurian == '     น้อยกว่าหรือเท่ากับ'):
                        if(float(AmountValue) <= float(extraClassSave.amountDurian)):
                            self.outputExtra()
                        else:
                            self.outputOut()
                    elif(extraClassSave.HTUAmountDurian == '     น้อยกว่า'):
                        if(float(AmountValue) < float(extraClassSave.amountDurian)):
                            self.outputExtra()
                        else:
                            self.outputOut()
                    else:
                        self.outputOut()

                # Class I
                elif((float(WeightValue) >= float(classISave.weightInitDurian) and float(WeightValue) <= float(classISave.weightFinalDurian)) and (float(PerBadValue) >= float(classISave.perBadInitDurian) and float(PerBadValue) <= float(classISave.perBadFinalDurian)) and (float(PerShapeValue) >= float(classISave.perShapeInitDurian) and float(PerShapeValue) <= float(classISave.perShapeFinalDurian))):
                    if(classISave.HTUAmountDurian == '     มากกว่าหรือเท่ากับ'):
                        if(float(AmountValue) >= float(classISave.amountDurian)):
                            self.outputClassI()
                        else:
                            self.outputOut()
                    elif(classISave.HTUAmountDurian == '     มากกว่า'):
                        if(float(AmountValue) > float(classISave.amountDurian)):
                            self.outputClassI()
                        else:
                            self.outputOut()
                    elif(classISave.HTUAmountDurian == '     เท่ากับ'):
                        if(float(AmountValue) == float(classISave.amountDurian)):
                            self.outputClassI()
                        else:
                            self.outputOut()
                    elif(classISave.HTUAmountDurian == '     น้อยกว่าหรือเท่ากับ'):
                        if(float(AmountValue) <= float(classISave.amountDurian)):
                            self.outputClassI()
                        else:
                            self.outputOut()
                    elif(classISave.HTUAmountDurian == '     น้อยกว่า'):
                        if(float(AmountValue) < float(classISave.amountDurian)):
                            self.outputClassI()
                        else:
                            self.outputOut()
                    else:
                        self.outputOut()
                
                # Class II
                elif((float(WeightValue) >= float(classIISave.weightInitDurian) and float(WeightValue) <= float(classIISave.weightFinalDurian)) and (float(PerBadValue) >= float(classIISave.perBadInitDurian) and float(PerBadValue) <= float(classIISave.perBadFinalDurian)) and (float(PerShapeValue) >= float(classIISave.perShapeInitDurian) and float(PerShapeValue) <= float(classIISave.perShapeFinalDurian))):
                    if(classIISave.HTUAmountDurian == '     มากกว่าหรือเท่ากับ'):
                        if(float(AmountValue) >= float(classIISave.amountDurian)):
                            self.outputClassII()
                        else:
                            self.outputOut()
                    elif(classIISave.HTUAmountDurian == '     มากกว่า'):
                        if(float(AmountValue) > float(classIISave.amountDurian)):
                            self.outputClassII()
                        else:
                            self.outputOut()
                    elif(classIISave.HTUAmountDurian == '     เท่ากับ'):
                        if(float(AmountValue) == float(classIISave.amountDurian)):
                            self.outputClassII()
                        else:
                            self.outputOut()
                    elif(classIISave.HTUAmountDurian == '     น้อยกว่าหรือเท่ากับ'):
                        if(float(AmountValue) <= float(classIISave.amountDurian)):
                            self.outputClassII()
                        else:
                            self.outputOut()
                    elif(classIISave.HTUAmountDurian == '     น้อยกว่า'):
                        if(float(AmountValue) < float(classIISave.amountDurian)):
                            self.outputClassII()
                        else:
                            self.outputOut()
                    else:
                        self.outputOut()
                
                # Out
                else:
                    self.outputOut()
            elif(HardnessValue == 0):
                self.outputOut()
            else:
                self.outputOut()

            #---------------------------------------------------------------------------------------------------#

            self.StateVa = Text(self, 0, "ระบบทำงานเสร็จสมบูรณ์", 885, 55)
            self.StateVa.setFontSize(13) 
            self.StateVa.setSize(300, 100)
            self.StateVa.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 
            self.StateVa.setAlignment(Qt.AlignCenter)

            self.Pic1 = Text(self, 0, "ภาพมุมที่ 1", 42, 640)
            self.Pic1.setFontSize(10) 
            self.Pic1.setSize(300, 100)
            self.Pic1.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 
            self.Pic1.setAlignment(Qt.AlignCenter)  

            self.Pic2 = Text(self, 0, "ภาพมุมที่ 2", 272, 640)
            self.Pic2.setFontSize(10) 
            self.Pic2.setSize(300, 100)
            self.Pic2.setStyle("color: {}; background-color: None; font-weight: Bold;".format(self.color.darkGreen)) 
            self.Pic2.setAlignment(Qt.AlignCenter)  

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

            self.setting = Button(self, 20, "  SETTING CRITERIA", 973, 745, self.gotoSettingWindow, QtCore.Qt.PointingHandCursor)
            self.setting.setFontSize(12) 
            self.setting.setSize(240, 40)
            self.setting.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))
            self.setting.Icon(QtGui.QIcon("icons/settings.png"))

            self.finish = Button(self, 20, "FINISH", 825, 745, self.finishProgram, QtCore.Qt.PointingHandCursor)
            self.finish.setFontSize(12) 
            self.finish.setSize(120, 40)
            self.finish.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))

    #---------------------------------------------------------------------------------------------------------------------------#

    def gotoSettingWindow(self):
        SettingWindow = settingWindow()
        widget.addWidget(SettingWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
   
    #---------------------------------------------------------------------------------------------------------------------------#

    def runProgram(self):
        process.stateProcess = '1'
        MainWindow    = mainWindow()
        widget.addWidget(MainWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #---------------------------------------------------------------------------------------------------------------------------#

    def finishProgram(self):
        process.stateProcess = '0'
        MainWindow    = mainWindow()
        widget.addWidget(MainWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #---------------------------------------------------------------------------------------------------------------------------#

    def pauseProgram(self):
        process.stateProcess = '2'
        MainWindow    = mainWindow()
        widget.addWidget(MainWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #---------------------------------------------------------------------------------------------------------------------------#

    def resumeProgram(self):
        process.stateProcess = '1'
        MainWindow    = mainWindow()
        widget.addWidget(MainWindow)
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

        #---------------------------------------------------------------------------------------------------#

        if (process.stateProcess == '0'):
            painter4 = QPainter(self)
            painter4.setPen(QPen(QColor(211, 47, 47, 15)))
            painter4.setBrush(QBrush(QColor(211, 47, 47, 15), Qt.SolidPattern))
            # For status
            painter4.drawRoundedRect(840, 74, 350, 60, 20.0, 20.0)

            painter5 = QPainter(self)
            painter5.setPen(QPen(QColor(211, 47, 47)))
            painter5.setBrush(QBrush(QColor(211, 47, 47), Qt.SolidPattern))
            # For title
            painter5.drawEllipse(868, 91, 28, 28)

        #---------------------------------------------------------------------------------------------------#

        if (process.stateProcess == '1'):
            painter4 = QPainter(self)
            painter4.setPen(QPen(QColor(255, 210, 85, 15)))
            painter4.setBrush(QBrush(QColor(255, 210, 85, 15), Qt.SolidPattern))
            # For status
            painter4.drawRoundedRect(840, 74, 350, 60, 20.0, 20.0)

            painter5 = QPainter(self)
            painter5.setPen(QPen(QColor(255, 210, 85)))
            painter5.setBrush(QBrush(QColor(255, 210, 85), Qt.SolidPattern))
            # For title
            painter5.drawEllipse(868, 91, 28, 28)

        #---------------------------------------------------------------------------------------------------#

        if (process.stateProcess == '2'):
            painter4 = QPainter(self)
            painter4.setPen(QPen(QColor(232, 122, 35, 15)))
            painter4.setBrush(QBrush(QColor(232, 122, 35, 15), Qt.SolidPattern))
            # For status
            painter4.drawRoundedRect(840, 74, 350, 60, 20.0, 20.0)

            painter5 = QPainter(self)
            painter5.setPen(QPen(QColor(232, 122, 35)))
            painter5.setBrush(QBrush(QColor(232, 122, 35), Qt.SolidPattern))
            # For title
            painter5.drawEllipse(868, 91, 28, 28)

        #---------------------------------------------------------------------------------------------------#

        if (process.stateProcess == '3'):
            painter4 = QPainter(self)
            painter4.setPen(QPen(QColor(163, 195, 48, 15)))
            painter4.setBrush(QBrush(QColor(163, 195, 48, 15), Qt.SolidPattern))
            # For status
            painter4.drawRoundedRect(840, 74, 350, 60, 20.0, 20.0)

            painter5 = QPainter(self)
            painter5.setPen(QPen(QColor(82, 137, 1)))
            painter5.setBrush(QBrush(QColor(82, 137, 1), Qt.SolidPattern))
            # For title
            painter5.drawEllipse(868, 91, 28, 28)
        
        
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
        self.settingTopic.setAlignment(Qt.AlignCenter)

        self.gradeTopic = Text(self, 0, "SELECT CLASS", 130, 285)
        self.gradeTopic.setFontSize(13) 
        self.gradeTopic.setSize(190, 40)
        self.gradeTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))

        self.criteriaTopic = Text(self, 0, "DETAILS OF CRITERIA", 130, 350)
        self.criteriaTopic.setFontSize(13) 
        self.criteriaTopic.setSize(250, 40)
        self.criteriaTopic.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGreen))

        self.weightCriTopic = Text(self, 0, "น้ำหนักผลทุเรียน", 160, 410)
        self.weightCriTopic.setFontSize(13) 
        self.weightCriTopic.setSize(250, 40)
        self.weightCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.weightCriTopic1 = Text(self, 0, "กิโลกรัม      ถึง", 578, 410)
        self.weightCriTopic1.setFontSize(13) 
        self.weightCriTopic1.setSize(250, 40)
        self.weightCriTopic1.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))
        
        self.weightCriTopic2 = Text(self, 0, "กิโลกรัม", 890, 410)
        self.weightCriTopic2.setFontSize(13) 
        self.weightCriTopic2.setSize(250, 40)
        self.weightCriTopic2.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.notSelect1 = Text(self, 0, "Not Select", 1090, 415)
        self.notSelect1.setFontSize(12) 
        self.notSelect1.setSize(250, 40)
        self.notSelect1.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGray))

        self.perBadCriTopic = Text(self, 0, "เปอร์เซ็นต์ตำหนิ", 160, 475)
        self.perBadCriTopic.setFontSize(13) 
        self.perBadCriTopic.setSize(250, 40)
        self.perBadCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.perBadCriTopic1 = Text(self, 0, "เปอร์เซ็นต์   ถึง", 578, 475)
        self.perBadCriTopic1.setFontSize(13) 
        self.perBadCriTopic1.setSize(250, 40)
        self.perBadCriTopic1.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.perBadCriTopic2 = Text(self, 0, "เปอร์เซ็นต์", 890, 475)
        self.perBadCriTopic2.setFontSize(13) 
        self.perBadCriTopic2.setSize(250, 40)
        self.perBadCriTopic2.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.notSelect2 = Text(self, 0, "Not Select", 1090, 480)
        self.notSelect2.setFontSize(12) 
        self.notSelect2.setSize(250, 40)
        self.notSelect2.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGray))

        self.perShapeCriTopic = Text(self, 0, "เปอร์เซ็นต์ความสมมาตร", 160, 540)
        self.perShapeCriTopic.setFontSize(13) 
        self.perShapeCriTopic.setSize(250, 40)
        self.perShapeCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.perShapeCriTopic = Text(self, 0, "เปอร์เซ็นต์   ถึง", 578, 540)
        self.perShapeCriTopic.setFontSize(13) 
        self.perShapeCriTopic.setSize(250, 40)
        self.perShapeCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.perShapeCriTopic2 = Text(self, 0, "เปอร์เซ็นต์", 890, 540)
        self.perShapeCriTopic2.setFontSize(13) 
        self.perShapeCriTopic2.setSize(250, 40)
        self.perShapeCriTopic2.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.notSelect3 = Text(self, 0, "Not Select", 1090, 545)
        self.notSelect3.setFontSize(12) 
        self.notSelect3.setSize(250, 40)
        self.notSelect3.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGray))

        self.amountCriTopic = Text(self, 0, "จำนวนพูสมบูรณ์", 160, 605)
        self.amountCriTopic.setFontSize(13) 
        self.amountCriTopic.setSize(250, 40)
        self.amountCriTopic.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.amountCriTopic2 = Text(self, 0, "พู", 890, 605)
        self.amountCriTopic2.setFontSize(13) 
        self.amountCriTopic2.setSize(250, 40)
        self.amountCriTopic2.setStyle("color: {}; background-color: None;".format(self.color.darkGreen))

        self.notSelect4 = Text(self, 0, "Not Select", 1090, 610)
        self.notSelect4.setFontSize(12) 
        self.notSelect4.setSize(250, 40)
        self.notSelect4.setStyle("color: {}; background-color: None; font-weight: bold;".format(self.color.darkGray))

        #---------------------------------------------------------------------------------------------------#

        self.backToMain = Button(self, 20, "  BACK", 1013, 745, self.gotoMainWindow, QtCore.Qt.PointingHandCursor)
        self.backToMain.setFontSize(12) 
        self.backToMain.setSize(200, 40)
        self.backToMain.setStyle("color:{}; background-color: {}; border-radius: 10; font-weight: Bold;".format(self.color.darkGray, self.color.lightGray))
        self.backToMain.Icon(QtGui.QIcon("icons/back.png"))

        self.save = Button(self, 20, "SAVE", 680, 670, self.saveCriteria, QtCore.Qt.PointingHandCursor)
        self.save.setFontSize(11) 
        self.save.setSize(120, 35)
        self.save.setStyle("color:{}; background-color: rgb(90, 90, 90); border-radius: 10; font-weight: Bold;".format(self.color.white))

        self.cancel = Button(self, 20, "CANCEL", 520, 670, self.cancelCriteria, QtCore.Qt.PointingHandCursor)
        self.cancel.setFontSize(11) 
        self.cancel.setSize(120, 35)
        self.cancel.setStyle("color:{}; background-color: rgb(90, 90, 90); border-radius: 10; font-weight: Bold;".format(self.color.white))

        #---------------------------------------------------------------------------------------------------#

        self.selectClass = dropDownList(self, 12, 435, 275, QtCore.Qt.PointingHandCursor, self.handleSelectClass)
        self.selectClass.setItem('     Select Class')
        self.selectClass.setItem('     Extra Class')
        self.selectClass.setItem('     Class I')
        self.selectClass.setItem('     Class II')
        self.selectClass.setSize(300, 33)
        style = """
            QComboBox{
                color: rgb(43, 43, 43); 
                background-color: rgb(172, 171, 172, 50);  
                border : 1.5px solid rgb(43, 43, 43, 50); 
                font-weight: Bold; 
                border-radius: 4px;
                padding: 2px;
            }

            QComboBox QAbstractItemView {
                outline: none;
            }
            
            QComboBox::down-arrow {
                image: url(icons/downArrow.png);
                width: 20px;
                height: 20px;
                margin: 10px;
                padding-right: 30px;
            } 

            QComboBox::drop-down {
                border: 0px;
            } 

            QComboBox QAbstractItemView {
                background-color: rgb(90, 90, 90); 
                color: rgb(255, 255, 255);  
                border: None;
                selection-background-color: rgb(43, 43, 43);
            }
        """
        self.selectClass.setStyle(style)

        # ------------------------------------------------------------------------------------------#

        self.selectAmount = dropDownList(self, 12, 435, 605, QtCore.Qt.PointingHandCursor, self.handleSelectAmount)
        self.selectAmount.setItem('     Select')
        self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
        self.selectAmount.setItem('     มากกว่า')
        self.selectAmount.setItem('     เท่ากับ')
        self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
        self.selectAmount.setItem('     น้อยกว่า')
        self.selectAmount.setSize(250, 33)
        style = """
            QComboBox{
                color: rgb(43, 43, 43); 
                background-color: rgb(172, 171, 172, 50);  
                border : 1.5px solid rgb(43, 43, 43, 50); 
                font-weight: Bold; 
                border-radius: 4px;
                padding: 2px;
            }

            QComboBox QAbstractItemView {
                outline: none;
            }
            
            QComboBox::down-arrow {
                image: url(icons/downArrow.png);
                width: 20px;
                height: 20px;
                margin: 10px;
                padding-right: 30px;
            } 

            QComboBox::drop-down {
                border: 0px;
            } 

            QComboBox QAbstractItemView {
                background-color: rgb(90, 90, 90); 
                color: rgb(255, 255, 255);  
                border: None;
                selection-background-color: rgb(43, 43, 43);
            }
        """
        self.selectAmount.setStyle(style)

        # ------------------------------------------------------------------------------------------#

        style = """
            QCheckBox{
                background-color: white;
                border-radius: 2; 
                border-color: rgb(43, 43, 43);
            }
            QCheckBox::indicator{
                width: 20px;
                height: 20px;
            }
            QCheckBox::indicator:checked{
                background: url(icons/tick.png);
                background-position: center;
                background-repeat: no-repeat;
                border-radius: 2; 
                border-color: rgb(43, 43, 43);
            }

        """

        #---------------------------------------------------------------------------------------------------#

        self.checkbox1 = CheckBox(self, 1050, 415, QtCore.Qt.PointingHandCursor, self.CheckSelectWeight)
        self.checkbox1.setStyle(style)
        self.checkbox1.setSize(25,25)
        self.checkbox1.setCheck(False)

        self.checkbox2 = CheckBox(self, 1050, 480, QtCore.Qt.PointingHandCursor, self.CheckSelectPerBad)
        self.checkbox2.setStyle(style)
        self.checkbox2.setSize(25,25)
        self.checkbox2.setCheck(False)

        self.checkbox3 = CheckBox(self, 1050, 545, QtCore.Qt.PointingHandCursor, self.CheckSelectPerShape)
        self.checkbox3.setStyle(style)
        self.checkbox3.setSize(25,25)        
        self.checkbox3.setCheck(False)

        self.checkbox4 = CheckBox(self, 1050, 610, QtCore.Qt.PointingHandCursor, self.CheckSelectAmount)
        self.checkbox4.setStyle(style)
        self.checkbox4.setSize(25,25) 
        self.checkbox4.setCheck(False) 

        self.weightInputInit = InputBox(self, 15, 435, 410, QtCore.Qt.IBeamCursor, self.weightInit)
        self.weightInputInit.setFontSize(12)
        self.weightInputInit.setSize(120, 33)
        self.weightInputInit.placeHolderText("0")

        self.weightInputFinal = InputBox(self, 15, 750, 410, QtCore.Qt.IBeamCursor, self.weightFinal)
        self.weightInputFinal.setFontSize(12)
        self.weightInputFinal.setSize(120, 33)
        self.weightInputFinal.placeHolderText("0")

        self.perBadInputInit = InputBox(self, 15, 435, 475, QtCore.Qt.IBeamCursor, self.perBadInit)
        self.perBadInputInit.setFontSize(12)
        self.perBadInputInit.setSize(120, 33)
        self.perBadInputInit.placeHolderText("0")

        self.perBadInputFinal = InputBox(self, 15, 750, 475, QtCore.Qt.IBeamCursor, self.perBadFinal)
        self.perBadInputFinal.setFontSize(12)
        self.perBadInputFinal.setSize(120, 33)
        self.perBadInputFinal.placeHolderText("0")

        self.perShapeInputInit = InputBox(self, 15, 435, 540, QtCore.Qt.IBeamCursor, self.perShapeInit)
        self.perShapeInputInit.setFontSize(12)
        self.perShapeInputInit.setSize(120, 33)
        self.perShapeInputInit.placeHolderText("0")

        self.perShapeInputFinal = InputBox(self, 15, 750, 540, QtCore.Qt.IBeamCursor, self.perShapeFinal)
        self.perShapeInputFinal.setFontSize(12)
        self.perShapeInputFinal.setSize(120, 33)
        self.perShapeInputFinal.placeHolderText("0")

        self.amountInput = InputBox(self, 15, 750, 605, QtCore.Qt.IBeamCursor, self.amountIn)
        self.amountInput.setFontSize(12)
        self.amountInput.setSize(120, 33)
        self.amountInput.placeHolderText("0")

    #---------------------------------------------------------------------------------------------------------------------------#

    def handleSelectClass(self, value):
        self.ClassIn = value
        if (self.ClassIn == "     Extra Class"):
            self.weightInputInit.placeHolderText(extraClassSave.weightInitDurian)
            self.weightInputFinal.placeHolderText(extraClassSave.weightFinalDurian)
            self.perBadInputInit.placeHolderText(extraClassSave.perBadInitDurian)
            self.perBadInputFinal.placeHolderText(extraClassSave.perBadFinalDurian)   
            self.perShapeInputInit.placeHolderText(extraClassSave.perShapeInitDurian)
            self.perShapeInputFinal.placeHolderText(extraClassSave.perShapeFinalDurian)   
            self.amountInput.placeHolderText(extraClassSave.amountDurian)           

            self.selectAmount.clearData()
            self.selectAmount.setItem(extraClassSave.HTUAmountDurian)
            self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     มากกว่า')
            self.selectAmount.setItem('     เท่ากับ')
            self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     น้อยกว่า')

            if (ECheckSave.weightDurian == 0):
                self.checkbox1.setCheck(True)
            else:
                self.checkbox1.setCheck(False)

            if (ECheckSave.perBadDurian == 0):
                self.checkbox2.setCheck(True)
            else:
                self.checkbox2.setCheck(False)

            if (ECheckSave.perShapeDurian == 0):
                self.checkbox3.setCheck(True)
            else:
                self.checkbox3.setCheck(False) 

            if (ECheckSave.amountDurian == 0):
                self.checkbox4.setCheck(True)
            else:
                self.checkbox4.setCheck(False) 

        if (self.ClassIn == "     Class I"):
            self.weightInputInit.placeHolderText(classISave.weightInitDurian)
            self.weightInputFinal.placeHolderText(classISave.weightFinalDurian)
            self.perBadInputInit.placeHolderText(classISave.perBadInitDurian)
            self.perBadInputFinal.placeHolderText(classISave.perBadFinalDurian)   
            self.perShapeInputInit.placeHolderText(classISave.perShapeInitDurian)
            self.perShapeInputFinal.placeHolderText(classISave.perShapeFinalDurian)   
            self.amountInput.placeHolderText(classISave.amountDurian)        

            self.selectAmount.clearData()
            self.selectAmount.setItem(classISave.HTUAmountDurian)
            self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     มากกว่า')
            self.selectAmount.setItem('     เท่ากับ')
            self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     น้อยกว่า')

            if (ICheckSave.weightDurian == 0):
                self.checkbox1.setCheck(True)
            else:
                self.checkbox1.setCheck(False)

            if (ICheckSave.perBadDurian == 0):
                self.checkbox2.setCheck(True)
            else:
                self.checkbox2.setCheck(False)

            if (ICheckSave.perShapeDurian == 0):
                self.checkbox3.setCheck(True)
            else:
                self.checkbox3.setCheck(False) 

            if (ICheckSave.amountDurian == 0):
                self.checkbox4.setCheck(True)
            else:
                self.checkbox4.setCheck(False) 

        if (self.ClassIn == "     Class II"):
            self.weightInputInit.placeHolderText(classIISave.weightInitDurian)
            self.weightInputFinal.placeHolderText(classIISave.weightFinalDurian)
            self.perBadInputInit.placeHolderText(classIISave.perBadInitDurian)
            self.perBadInputFinal.placeHolderText(classIISave.perBadFinalDurian)
            self.perShapeInputInit.placeHolderText(classIISave.perShapeInitDurian)
            self.perShapeInputFinal.placeHolderText(classIISave.perShapeFinalDurian)      
            self.amountInput.placeHolderText(classIISave.amountDurian)        
            
            self.selectAmount.clearData()
            self.selectAmount.setItem(classIISave.HTUAmountDurian)
            self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     มากกว่า')
            self.selectAmount.setItem('     เท่ากับ')
            self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     น้อยกว่า')

            if (IICheckSave.weightDurian == 0):
                self.checkbox1.setCheck(True)
            else:
                self.checkbox1.setCheck(False)

            if (IICheckSave.perBadDurian == 0):
                self.checkbox2.setCheck(True)
            else:
                self.checkbox2.setCheck(False)

            if (IICheckSave.perShapeDurian == 0):
                self.checkbox3.setCheck(True)
            else:
                self.checkbox3.setCheck(False) 

            if (IICheckSave.amountDurian == 0):
                self.checkbox4.setCheck(True)
            else:
                self.checkbox4.setCheck(False) 

        print(self.ClassIn)
 
    #---------------------------------------------------------------------------------------------------------------------------#

    def weightInit(self, valueWeight):
        self.WeightInit = valueWeight
        if (self.ClassIn == "     Extra Class"):
            extraClass.weightInitDurian = self.WeightInit
        if (self.ClassIn == "     Class I"):
            classI.weightInitDurian = self.WeightInit
        if (self.ClassIn == "     Class II"):
            classII.weightInitDurian = self.WeightInit

    def weightFinal(self, valueWeight):
        self.WeightFinal = valueWeight
        if (self.ClassIn == "     Extra Class"):
            extraClass.weightFinalDurian = self.WeightFinal
        if (self.ClassIn == "     Class I"):
            classI.weightFinalDurian = self.WeightFinal
        if (self.ClassIn == "     Class II"):
            classII.weightFinalDurian = self.WeightFinal

    def perBadInit(self, valuePerBad):
        self.PerBadInit = valuePerBad
        if (self.ClassIn == "     Extra Class"):
            extraClass.perBadInitDurian = self.PerBadInit
        if (self.ClassIn == "     Class I"):
            classI.perBadInitDurian = self.PerBadInit
        if (self.ClassIn == "     Class II"):
            classII.perBadInitDurian = self.PerBadInit

    def perBadFinal(self, valuePerBad):
        self.PerBadFinal = valuePerBad
        if (self.ClassIn == "     Extra"):
            extraClass.perBadFinalDurian = self.PerBadFinal
        if (self.ClassIn == "     Class I"):
            classI.perBadFinalDurian = self.PerBadFinal
        if (self.ClassIn == "     Class II"):
            classII.perBadFinalDurian = self.PerBadFinal

    def perShapeInit(self, valuePerShape):
        self.PerShapeInit = valuePerShape
        if (self.ClassIn == "     Extra Class"):
            extraClass.perShapeInitDurian = self.PerShapeInit
        if (self.ClassIn == "     Class I"):
            classI.perShapeInitDurian = self.PerShapeInit
        if (self.ClassIn == "     Class II"):
            classII.perShapeInitDurian = self.PerShapeInit

    def perShapeFinal(self, valuePerShape):
        self.PerShapeFinal = valuePerShape
        if (self.ClassIn == "     Extra Class"):
            extraClass.perShapeFinalDurian = self.PerShapeFinal
        if (self.ClassIn == "     Class I"):
            classI.perShapeFinalDurian = self.PerShapeFinal
        if (self.ClassIn == "     Class II"):
            classII.perShapeFinalDurian = self.PerShapeFinal

    def amountIn(self, valueAmount):
        self.AmountIn = valueAmount
        if (self.ClassIn == "     Extra Class"):
            extraClass.amountDurian = self.AmountIn
        if (self.ClassIn == "     Class I"):
            classI.amountDurian = self.AmountIn
        if (self.ClassIn == "     Class II"):
            classII.amountDurian = self.AmountIn

    #---------------------------------------------------------------------------------------------------------------------------# 

    def handleSelectAmount(self, valueHTUAmount):
        self.HTUAmountIn = valueHTUAmount
        if (self.ClassIn == "     Extra Class"):
            extraClass.HTUAmountDurian = self.HTUAmountIn
        if (self.ClassIn == "     Class I"):
            classI.HTUAmountDurian = self.HTUAmountIn
        if (self.ClassIn == "     Class II"):
            classII.HTUAmountDurian = self.HTUAmountIn

    #---------------------------------------------------------------------------------------------------------------------------#

    def CheckSelectWeight(self, state):
        if state == QtCore.Qt.Checked:
            if (self.ClassIn == "     Extra Class"):
                ECheck.weightDurian = 0
                extraClass.weightInitDurian = '0'
                extraClass.weightFinalDurian = '0'
                self.weightInputInit.placeHolderText(extraClass.weightInitDurian)
                self.weightInputFinal.placeHolderText(extraClass.weightFinalDurian)
            if (self.ClassIn == "     Class I"):
                ICheck.weightDurian = 0                
                classI.weightInitDurian = '0'
                classI.weightFinalDurian = '0'
                self.weightInputInit.placeHolderText(classI.weightInitDurian)
                self.weightInputFinal.placeHolderText(classI.weightFinalDurian)
            if (self.ClassIn == "     Class II"):
                IICheck.weightDurian = 0                     
                classII.weightInitDurian = '0'
                classII.weightFinalDurian = '0'
                self.weightInputInit.placeHolderText(classII.weightInitDurian)
                self.weightInputFinal.placeHolderText(classII.weightFinalDurian)
        else:
            if (self.ClassIn == "     Extra Class"):
                ECheck.weightDurian = 1     
                self.weightInputInit.placeHolderText(extraClassSave.weightInitDurian)
                self.weightInputFinal.placeHolderText(extraClassSave.weightFinalDurian)
            if (self.ClassIn == "     Class I"):
                ICheck.weightDurian = 1 
                self.weightInputInit.placeHolderText(classISave.weightInitDurian)
                self.weightInputFinal.placeHolderText(classISave.weightFinalDurian)
            if (self.ClassIn == "     Class I"):
                IICheck.weightDurian = 1 
                self.weightInputInit.placeHolderText(classIISave.weightInitDurian)
                self.weightInputFinal.placeHolderText(classIISave.weightFinalDurian)

    def CheckSelectPerBad(self, state):
        if state == QtCore.Qt.Checked:
            if (self.ClassIn == "     Extra Class"):
                ECheck.perBadDurian = 0                     
                extraClass.perBadInitDurian = '0'
                extraClass.perBadFinalDurian = '0'
                self.perBadInputInit.placeHolderText(extraClass.perBadInitDurian)
                self.perBadInputFinal.placeHolderText(extraClass.perBadFinalDurian)   
            if (self.ClassIn == "     Class I"):
                ICheck.perBadDurian = 0  
                classI.perBadInitDurian = '0'
                classI.perBadFinalDurian = '0'
                self.perBadInputInit.placeHolderText(classI.perBadInitDurian)
                self.perBadInputFinal.placeHolderText(classI.perBadFinalDurian) 
            if (self.ClassIn == "     Class II"):
                IICheck.perBadDurian = 0  
                classII.perBadInitDurian = '0'
                classII.perBadFinalDurian = '0'
                self.perBadInputInit.placeHolderText(classII.perBadInitDurian)
                self.perBadInputFinal.placeHolderText(classII.perBadFinalDurian) 
        else:
            if (self.ClassIn == "     Extra Class"):
                ECheck.perBadDurian = 1  
                self.perBadInputInit.placeHolderText(extraClassSave.perBadInitDurian)
                self.perBadInputFinal.placeHolderText(extraClassSave.perBadFinalDurian)      
            if (self.ClassIn == "     Class I"):
                ICheck.perBadDurian = 1 
                self.perBadInputInit.placeHolderText(classISave.perBadInitDurian)
                self.perBadInputFinal.placeHolderText(classISave.perBadFinalDurian) 
            if (self.ClassIn == "     Class II"):
                IICheck.perBadDurian = 1  
                self.perBadInputInit.placeHolderText(classIISave.perBadInitDurian)
                self.perBadInputFinal.placeHolderText(classIISave.perBadFinalDurian)      

    def CheckSelectPerShape(self, state):
        if state == QtCore.Qt.Checked:
            if (self.ClassIn == "     Extra Class"):
                ECheck.perShapeDurian = 0                     
                extraClass.perShapeInitDurian = '0'
                extraClass.perShapeFinalDurian = '0'
                self.perShapeInputInit.placeHolderText(extraClass.perShapeInitDurian)
                self.perShapeInputFinal.placeHolderText(extraClass.perShapeFinalDurian)   
            if (self.ClassIn == "     Class I"):
                ICheck.perShapeDurian = 0  
                classI.perShapeInitDurian = '0'
                classI.perShapeFinalDurian = '0'
                self.perShapeInputInit.placeHolderText(classI.perShapeInitDurian)
                self.perShapeInputFinal.placeHolderText(classI.perShapeFinalDurian) 
            if (self.ClassIn == "     Class II"):
                IICheck.perShapeDurian = 0  
                classII.perShapeInitDurian = '0'
                classII.perShapeFinalDurian = '0'
                self.perShapeInputInit.placeHolderText(classII.perShapeInitDurian)
                self.perShapeInputFinal.placeHolderText(classII.perShapeFinalDurian) 
        else:
            if (self.ClassIn == "     Extra Class"):
                ECheck.perShapeDurian = 1    
                self.perShapeInputInit.placeHolderText(extraClassSave.perShapeInitDurian)
                self.perShapeInputFinal.placeHolderText(extraClassSave.perShapeFinalDurian)   
            if (self.ClassIn == "     Class I"):
                ICheck.perShapeDurian = 1 
                self.perShapeInputInit.placeHolderText(classISave.perShapeInitDurian)
                self.perShapeInputFinal.placeHolderText(classISave.perShapeFinalDurian)
            if (self.ClassIn == "     Class II"):
                IICheck.perShapeDurian = 1  
                self.perShapeInputInit.placeHolderText(classIISave.perShapeInitDurian)
                self.perShapeInputFinal.placeHolderText(classIISave.perShapeFinalDurian) 

    def CheckSelectAmount(self, state):
        if state == QtCore.Qt.Checked:
            if (self.ClassIn == "     Extra Class"):
                ECheck.amountDurian = 0       
                extraClass.amountDurian = '0'
                extraClass.HTUAmountDurian = '     มากกว่าหรือเท่ากับ'
                self.amountInput.placeHolderText(extraClass.amountDurian) 
            if (self.ClassIn == "     Class I"):
                ICheck.amountDurian = 0                 
                classI.amountDurian = '0'
                classI.HTUAmountDurian = '     มากกว่าหรือเท่ากับ'
                self.amountInput.placeHolderText(classI.amountDurian) 
            if (self.ClassIn == "     Class II"):
                IICheck.amountDurian = 0                  
                classII.amountDurian = '0'
                classI.HTUAmountDurian = '     มากกว่าหรือเท่ากับ'
                self.amountInput.placeHolderText(classII.amountDurian) 
        else:
            if (self.ClassIn == "     Extra Class"):
                ECheck.amountDurian = 1    
                self.amountInput.placeHolderText(extraClassSave.amountDurian) 
                self.selectAmount.clearData()
                self.selectAmount.setItem(classISave.HTUAmountDurian)
                self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
                self.selectAmount.setItem('     มากกว่า')
                self.selectAmount.setItem('     เท่ากับ')
                self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
                self.selectAmount.setItem('     น้อยกว่า') 
            if (self.ClassIn == "     Class I"):
                ICheck.amountDurian = 1
                self.amountInput.placeHolderText(classISave.amountDurian) 
                self.selectAmount.clearData()
                self.selectAmount.setItem(classISave.HTUAmountDurian)
                self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
                self.selectAmount.setItem('     มากกว่า')
                self.selectAmount.setItem('     เท่ากับ')
                self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
                self.selectAmount.setItem('     น้อยกว่า')
            if (self.ClassIn == "     Class II"): 
                IICheck.amountDurian = 1   
                self.amountInput.placeHolderText(classIISave.amountDurian) 
                self.selectAmount.clearData()
                self.selectAmount.setItem(classISave.HTUAmountDurian)
                self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
                self.selectAmount.setItem('     มากกว่า')
                self.selectAmount.setItem('     เท่ากับ')
                self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
                self.selectAmount.setItem('     น้อยกว่า')

    #---------------------------------------------------------------------------------------------------------------------------#

    def gotoMainWindow(self):
        MainWindow    = mainWindow()
        widget.addWidget(MainWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #---------------------------------------------------------------------------------------------------------------------------#

    def saveCriteria(self):
        print("Save Value")
        if (self.ClassIn == "     Extra Class"):
            extraClassSave.claDurian = 'E'
            extraClassSave.weightInitDurian         = extraClass.weightInitDurian
            extraClassSave.weightFinalDurian        = extraClass.weightFinalDurian
            extraClassSave.perBadInitDurian         = extraClass.perBadInitDurian
            extraClassSave.perBadFinalDurian        = extraClass.perBadFinalDurian
            extraClassSave.perShapeInitDurian       = extraClass.perShapeInitDurian
            extraClassSave.perShapeFinalDurian      = extraClass.perShapeFinalDurian
            extraClassSave.amountDurian             = extraClass.amountDurian
            extraClassSave.HTUAmountDurian          = extraClass.HTUAmountDurian

            ECheckSave.weightDurian             = ECheck.weightDurian
            ECheckSave.perBadDurian             = ECheck.perBadDurian
            ECheckSave.perShapeDurian           = ECheck.perShapeDurian
            ECheckSave.amountDurian             = ECheck.amountDurian

            print(vars(extraClassSave))

        if (self.ClassIn == "     Class I"):
            classISave.claDurian = 'I'
            classISave.weightInitDurian             = classI.weightInitDurian
            classISave.weightFinalDurian            = classI.weightFinalDurian
            classISave.perBadInitDurian             = classI.perBadInitDurian
            classISave.perBadFinalDurian            = classI.perBadFinalDurian
            classISave.perShapeInitDurian           = classI.perShapeInitDurian
            classISave.perShapeFinalDurian          = classI.perShapeFinalDurian
            classISave.amountDurian                 = classI.amountDurian
            classISave.HTUAmountDurian              = classI.HTUAmountDurian

            ICheckSave.weightDurian                 = ICheck.weightDurian
            ICheckSave.perBadDurian                 = ICheck.perBadDurian
            ICheckSave.perShapeDurian               = ICheck.perShapeDurian
            ICheckSave.amountDurian                 = ICheck.amountDurian
            
            print(vars(classISave))

        if (self.ClassIn == "     Class II"):
            classIISave.claDurian = 'II'
            classIISave.weightInitDurian            = classII.weightInitDurian
            classIISave.weightFinalDurian           = classII.weightFinalDurian
            classIISave.perBadInitDurian            = classII.perBadInitDurian
            classIISave.perBadFinalDurian           = classII.perBadFinalDurian
            classIISave.perShapeInitDurian          = classII.perShapeInitDurian
            classIISave.perShapeFinalDurian         = classII.perShapeFinalDurian
            classIISave.amountDurian                = classII.amountDurian
            classIISave.HTUAmountDurian             = classII.HTUAmountDurian

            IICheckSave.weightDurian            = IICheck.weightDurian
            IICheckSave.perBadDurian            = IICheck.perBadDurian
            IICheckSave.perShapeDurian          = IICheck.perShapeDurian
            IICheckSave.amountDurian            = IICheck.amountDurian

            print(vars(classIISave))

    #---------------------------------------------------------------------------------------------------------------------------#

    def cancelCriteria(self):
        print("Cancel Value")
        if (self.ClassIn == "     Extra Class"):
            self.weightInputInit.placeHolderText(extraClassSave.weightInitDurian)
            self.weightInputFinal.placeHolderText(extraClassSave.weightFinalDurian)
            self.perBadInputInit.placeHolderText(extraClassSave.perBadInitDurian)
            self.perBadInputFinal.placeHolderText(extraClassSave.perBadFinalDurian)   
            self.perShapeInputInit.placeHolderText(extraClassSave.perShapeInitDurian)
            self.perShapeInputFinal.placeHolderText(extraClassSave.perShapeFinalDurian)   
            self.amountInput.placeHolderText(extraClassSave.amountDurian)          

            self.selectAmount.clearData()
            self.selectAmount.setItem(extraClassSave.HTUAmountDurian)
            self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     มากกว่า')
            self.selectAmount.setItem('     เท่ากับ')
            self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     น้อยกว่า')

            if (ECheckSave.weightDurian == 0):
                self.checkbox1.setCheck(True)
            else:
                self.checkbox1.setCheck(False)

            if (ECheckSave.perBadDurian == 0):
                self.checkbox2.setCheck(True)
            else:
                self.checkbox2.setCheck(False)

            if (ECheckSave.perShapeDurian == 0):
                self.checkbox3.setCheck(True)
            else:
                self.checkbox3.setCheck(False) 

            if (ECheckSave.amountDurian == 0):
                self.checkbox4.setCheck(True)
            else:
                self.checkbox4.setCheck(False) 


        if (self.ClassIn == "     Class I"):
            self.weightInputInit.placeHolderText(classISave.weightInitDurian)
            self.weightInputFinal.placeHolderText(classISave.weightFinalDurian)
            self.perBadInputInit.placeHolderText(classISave.perBadInitDurian)
            self.perBadInputFinal.placeHolderText(classISave.perBadFinalDurian)   
            self.perShapeInputInit.placeHolderText(classISave.perShapeInitDurian)
            self.perShapeInputFinal.placeHolderText(classISave.perShapeFinalDurian)   
            self.amountInput.placeHolderText(classISave.amountDurian)   

            self.selectAmount.clearData()
            self.selectAmount.setItem(classISave.HTUAmountDurian)
            self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     มากกว่า')
            self.selectAmount.setItem('     เท่ากับ')
            self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     น้อยกว่า')

            if (ICheckSave.weightDurian == 0):
                self.checkbox1.setCheck(True)
            else:
                self.checkbox1.setCheck(False)

            if (ICheckSave.perBadDurian == 0):
                self.checkbox2.setCheck(True)
            else:
                self.checkbox2.setCheck(False)

            if (ICheckSave.perShapeDurian == 0):
                self.checkbox3.setCheck(True)
            else:
                self.checkbox3.setCheck(False) 

            if (ICheckSave.amountDurian == 0):
                self.checkbox4.setCheck(True)
            else:
                self.checkbox4.setCheck(False) 

        if (self.ClassIn == "     Class II"):
            self.weightInputInit.placeHolderText(classIISave.weightInitDurian)
            self.weightInputFinal.placeHolderText(classIISave.weightFinalDurian)
            self.perBadInputInit.placeHolderText(classIISave.perBadInitDurian)
            self.perBadInputFinal.placeHolderText(classIISave.perBadFinalDurian)   
            self.perShapeInputInit.placeHolderText(classIISave.perShapeInitDurian)
            self.perShapeInputFinal.placeHolderText(classIISave.perShapeFinalDurian)   
            self.amountInput.placeHolderText(classIISave.amountDurian)   

            self.selectAmount.clearData()
            self.selectAmount.setItem(classIISave.HTUAmountDurian)
            self.selectAmount.setItem('     มากกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     มากกว่า')
            self.selectAmount.setItem('     เท่ากับ')
            self.selectAmount.setItem('     น้อยกว่าหรือเท่ากับ')
            self.selectAmount.setItem('     น้อยกว่า')

            if (IICheckSave.weightDurian == 0):
                self.checkbox1.setCheck(True)
            else:
                self.checkbox1.setCheck(False)

            if (IICheckSave.perBadDurian == 0):
                self.checkbox2.setCheck(True)
            else:
                self.checkbox2.setCheck(False)

            if (IICheckSave.perShapeDurian == 0):
                self.checkbox3.setCheck(True)
            else:
                self.checkbox3.setCheck(False) 

            if (IICheckSave.amountDurian == 0):
                self.checkbox4.setCheck(True)
            else:
                self.checkbox4.setCheck(False) 

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
        painter2.drawRoundedRect(135, 420, 12, 12, 2, 2)
        painter2.drawRoundedRect(135, 480, 12, 12, 2, 2)
        painter2.drawRoundedRect(135, 550, 12, 12, 2, 2)
        painter2.drawRoundedRect(135, 615, 12, 12, 2, 2)


#---------------------------------------------------------------------------------------------------------------------------#

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    MainWindow    = mainWindow()
    widget.addWidget(MainWindow)
    widget.setFixedSize(1280, 800)
    widget.show()
    widget.setWindowTitle("ระบบคัดแยกคุณภาพผลทุเรียนอัตโนมัติ")
    widget.setWindowIcon(QtGui.QIcon("icons/durian.png"))
    sys.exit(app.exec_()) 