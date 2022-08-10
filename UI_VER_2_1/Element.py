from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Color():
    def __init__(self):
      self.white      = "rgb(255, 255, 255)"
      self.lightGray  = "rgb(242, 242, 242)" 
      self.gray       = "rgb(172, 172, 172)" 
      self.darkGray   = "rgb(43, 43, 43)" 
      self.yellow     = "rgb(300, 210, 85)" 
      self.darkYellow = "rgb(100, 88, 0)"
      self.orange     = "rgb(232, 122, 35)" 
      self.darkOrange = "rgb(190, 88, 60)"
      self.lightGreen = "rgb(163, 195, 48)"
      self.green      = "rgb(82, 137, 1)" 
      self.darkGreen  = "rgb(56, 70, 9)" 
      self.blackGreen = "rgb(24, 33, 20)" 
      self.red        = "rgb(220, 50, 50)" 
      self.darkRed    = "rgb(50, 0, 0)" 

#-----------------------------------------------------------------------------------------------------------#

class Text():
    def __init__(self, window, fontSize, word, posX, posY):
        self.object = QLabel(window)
        self.object.setText(word)
        self.object.setFont(QFont("Prompt", fontSize))
        self.object.move(posX, posY)
        self.object.setAlignment(Qt.AlignLeft)

    def setFontSize(self, fontSize):
        self.object.setFont(QFont("Prompt", fontSize))
      
    def setPosition(self, posX, posY):
        self.object.move(posX, posY)

    def setSize(self, sizeX, sizeY):
        self.object.resize(sizeX, sizeY)

    def setStyle(self, style):
        self.object.setStyleSheet(style)

    def setText(self, text):
        self.object.setText(text)

    def normal(self):
        self.object.setStyleSheet("color: rgb(255, 255, 255)")

    def setAlignment(self, alignment):
      self.object.setAlignment(alignment)

#-----------------------------------------------------------------------------------------------------------#

class Button():
   def __init__(self, window, fontSize, word, posX, posY, Goto, cursor):
      self.object = QPushButton(window)
      self.object.setText(word)
      self.object.setFont(QFont("Prompt", fontSize))
      self.object.move(posX, posY)
      self.object.clicked.connect(Goto)
      self.object.setCursor(QCursor(cursor))
      self.style = ""
      self.pressed = False
      self.ready = False

   def setFontSize(self, fontSize):
      self.object.setFont(QFont("Prompt", fontSize))
      
   def setPosition(self, posX, posY):
      self.object.move(posX, posY)

   def setSize(self, sizeX, sizeY):
      self.object.resize(sizeX, sizeY)

   def setStyle(self, style):
      self.style = style
      self.object.setStyleSheet(style)

   def Icon(self, pic):
      self.object.setIcon(pic)

   def disable(self):
      self.object.setStyleSheet("color: rgb(43, 43, 43)")
   
   def enable(self):
      self.object.setStyleSheet(self.style)

#-----------------------------------------------------------------------------------------------------------#

class QLineEdit(QLineEdit):
   focusSignal = pyqtSignal()

   def focusInEvent(self, event):
      self.focusSignal.emit()
      super(QLineEdit, self).focusInEvent(event)
   
   def focusOutEvent(self, event):
      self.focusSignal.emit()
      super(QLineEdit, self).focusOutEvent(event)
      self.setStyleSheet("color: rgb(120, 120, 120); background-color : rgb(172, 172, 172, 50); border : 1.5px solid rgb(43, 43, 43, 50); font-weight: Bold; border-radius: 4px") 

#-----------------------------------------------------------------------------------------------------------#

class InputBox():
   def __init__(self, window, fontSize, posX, posY, cursor, goto):
      self.object = QLineEdit(window)
      self.object.setFont(QFont("Prompt", fontSize))
      self.object.move(posX, posY)
      self.object.setAlignment(Qt.AlignCenter)
      self.object.setCursor(QCursor(cursor))
      self.enable()
      self.unfocus()
      self.focused = False
      self.object.focusSignal.connect(self.focus)
      self.object.textChanged.connect(goto)
      self.onlyDouble = QDoubleValidator()
      self.object.setValidator(self.onlyDouble)

   def setFontSize(self, fontSize):
      self.object.setFont(QFont("Prompt", fontSize))

   def setPosition(self, posX, posY):
      self.object.move(posX, posY)

   def setSize(self, sizeX, sizeY):
      self.object.resize(sizeX, sizeY)
   
   def clear(self):
      self.object.setText('')

   def focus(self):
      self.focused = True
      self.object.setStyleSheet("color: rgb(43, 43, 43); background-color : rgb(172, 172, 172, 50); border : 2.5px solid rgb(43, 43, 43, 140); font-weight: Bold; border-radius: 10px")

   def unfocus(self):
      self.focused = False
      self.object.setStyleSheet("color: rgb(120, 120, 120); background-color : rgb(172, 172, 172, 50); border : 1.5px solid rgb(43, 43, 43, 50); font-weight: Bold; border-radius: 4px")

   def disable(self):
      self.unfocus()
      self.object.setDisabled(True)
      
   def enable(self):
      self.object.setDisabled(False)
      
   def getInput(self):
      return self.object.text()

   def clearText(self):
      self.object.clear()
   
   def textChange(self, goto):
      self.object.textChanged.connect(goto)

   def placeHolderText(self, text):
      self.object.clear()
      self.object.setPlaceholderText(text)

#-----------------------------------------------------------------------------------------------------------#

class dropDownList():
   def __init__(self, window, fontSize, posX, posY, cursor, goto):
      self.comboState = QComboBox(window)
      self.comboState.setFont(QFont("Prompt", fontSize))
      self.comboState.move(posX, posY)
      self.comboState.setCursor(QCursor(cursor))
      self.comboState.currentTextChanged.connect(goto)
      self.style = ""

   def setFontSize(self, fontSize):
      self.comboState.setFont(QFont("Prompt", fontSize))

   def setPosition(self, posX, posY):
      self.comboState.move(posX, posY)

   def setSize(self, sizeX, sizeY):
      self.comboState.resize(sizeX, sizeY)

   def setItem(self, item):
      self.comboState.addItem(item)

   def setStyle(self, style):
      self.style = style
      self.comboState.setStyleSheet(style)

   def currentText(self, text):
      self.comboState.setCurrentText(text)

   def clearData(self):
      self.comboState.clear()
   
#-----------------------------------------------------------------------------------------------------------#

class CheckBox():
   def __init__(self, window, posX, posY, cursor, goto):
      self.check = QCheckBox(window)
      self.check.setChecked(True)
      self.check.move(posX, posY)
      self.check.setCursor(QCursor(cursor))
      self.check.stateChanged.connect(goto)
      self.check.setChecked(False)
      self.style = "" 

   def setPosition(self, posX, posY):
      self.check.move(posX, posY)

   def setSize(self, sizeX, sizeY):
      self.check.resize(sizeX, sizeY)

   def setStyle(self, style):
      self.style = style
      self.check.setStyleSheet(style)

   def setCheck(self, TorF):
      self.check.setChecked(TorF)

#-----------------------------------------------------------------------------------------------------------#

class criteriaDurian:
   def __init__(self, cla, weightInit, weightFinal, HTUAmount, amount, perBadInit, perBadFinal, perShapeInit, perShapeFinal, hardness):
      self.claDurian             = cla
      self.weightInitDurian      = weightInit
      self.weightFinalDurian     = weightFinal
      self.HTUAmountDurian       = HTUAmount
      self.amountDurian          = amount
      self.perBadInitDurian      = perBadInit
      self.perBadFinalDurian     = perBadFinal
      self.perShapeInitDurian    = perShapeInit
      self.perShapeFinalDurian   = perShapeFinal
      self.hardnessDurian        = hardness

#-----------------------------------------------------------------------------------------------------------#

class criteriaCheck:
   def __init__(self, weight, amount, perBad, perShape):
      self.weightDurian          = weight
      self.amountDurian          = amount
      self.perBadDurian          = perBad
      self.perShapeDurian        = perShape

#-----------------------------------------------------------------------------------------------------------#

class state:
   def __init__(self, State):
      self.stateProcess = State

#-----------------------------------------------------------------------------------------------------------#