import math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Color():
    def __init__(self):
      self.white      = "rgb(255, 255, 255)"
      self.grey       = "rgb(172, 172, 172)" 
      self.darkGrey   = "rgb(43, 43, 43)" 
      self.yellow     = "rgb(255, 210, 85)" 
      self.darkYellow = "rgb(97, 88, 0)"
      self.lightGreen = "rgb(163, 195, 48)"
      self.green      = "rgb(82, 137, 1)" 
      self.darkGreen  = "rgb(56, 70, 9)" 
      self.blackGreen = "rgb(28, 36, 0)" 
      self.red        = "rgb(211, 47, 47)" 
      self.darkRed    = "rgb(65, 0, 0)" 


#-------------------------------------------------------#


class Text():
    def __init__(self, window, fontSize, word, posX, posY):
        self.object = QLabel(window)
        self.object.setText(word)
        self.object.setFont(QFont("Prompt", fontSize))
        self.object.move(posX, posY)
        self.object.setAlignment(Qt.AlignCenter)

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


#-------------------------------------------------------#


class Button():
   def __init__(self, window, fontSize, word, posX, posY):
      self.object = QPushButton(window)
      self.object.setText(word)
      self.object.setFont(QFont("Prompt", fontSize))
      self.object.move(posX, posY)
      self.object.clicked.connect(self.buttonClick)
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

   def buttonClick(self):
      self.pressed = True

   def disable(self):
      self.object.setStyleSheet("color: rgb(43, 43, 43); background-color: None")
   
   def enable(self):
      self.object.setStyleSheet(self.style)


#-------------------------------------------------------#
        
