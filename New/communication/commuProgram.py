import platform
import serial
import sys

class Communication():

    def __init__(self, os):

        self.os = os
        if self.os == 'D': #Mac
            self.ser = serial.Serial('/dev/cu.usbmodem1303', 115200, parity='E', stopbits=1, timeout=1)
        elif self.os == 'W': #Windows
            self.ser = serial.Serial('COM3',115200,parity='E',stopbits=1,timeout=1)
        self.ready = False
        self.camera = False
        self.running = False
        self.takeImg = False
        self.takeClip = False
        self.weight = 0
        self.start()

    def start(self):

        self.request_mode()
        if self.ready:
            self.weight_mode()


    def request_mode(self): # mode_1

        self.ser.write([177, 0])
        self.serialWait()
        serialRead = self.ser.read(2)
        if ((serialRead[0] == 177) & (serialRead[1] == 0)):
            self.ready = True
        elif (serialRead[0] == 178):
            self.camera = True
            if serialRead[1] - 171 > 0:
                self.takeImg = True
            elif serialRead[1] == 170:
                self.takeClip = True

    def camera_mode(self): # mode_2
        
        self.ser.write([178, 175])
        for i in range(4):
            self.request_mode()
            if self.camera & self.takeImg:
                for i in range(167,170,2):
                    self.ser.write([178, i])
                    self.serialWait()
                    serialRead = self.ser.read(3)
                    if ((self.checkSum(serialRead[:-1])) & (serialRead[0] == 178)):
                        print('take a img')
            elif self.camera & self.takeClip:
                self.ser.write([178, 167])
                self.serialWait()
                serialRead = self.ser.read(3)
                if ((self.checkSum(serialRead[:-1])) & (serialRead[0] == 178)):
                    print('take a video')

    def weight_mode(self): # mode_3

        self.ser.write([179, 165])
        self.serialWait()
        serialRead = self.ser.read(3)
        serialList = []
        if ((self.checkSum(serialRead[:-1])) & (serialRead[0] == 178)):
            for i in range(4):
                serialList.append(self.ser.read(1))
            if( self.checkSum(serialList[:-1]) == serialList[-1]):
                self.weight = ((serialList[0]*256 + serialList[1]) + ((serialList[2]*256 + serialList[3])/1000))
                print("Durian weight : " + str(self.weight) + ' kg')

    def force_mode(self): # mode_4
        return 0

    def sound_mode(self): # mode_5
        return 0

    def checkSum(self,dataFrame):
        return (~(sum(dataFrame)%256))%256

if __name__ == '__main__':
   app = Communication(platform.platform()[0].upper())
   sys.exit(app.exec_())








