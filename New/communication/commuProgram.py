from distutils.command.check import check
import platform
import serial
import sys

class Communication():

    def __init__(self, os):

        self.os = os
        if self.os == 'D': #Mac
            self.ser = serial.Serial('/dev/cu.usbmodem1303', 115200, parity='E', stopbits=1, timeout=1)
        elif self.os == 'W': #Windows
            self.ser = serial.Serial('COM10',115200,parity='E',stopbits=1,timeout=1)
        
        self.ready = False
        self.camera = False
        self.running = False
        self.takeImg = False
        self.takeClip = False
        
        self.force = 0
        self.weight = 0
        self.r_axis_force = 0
        self.theta_force = 0
        self.theta_sound = 0
        self.h_axis_sound = 0

        self.start()

    def start(self):

        self.request_mode()
        if self.ready:
            self.weight_mode()

    def request_mode(self): # mode_1 : 177

        self.ser.write([177])
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

    def camera_mode(self): # mode_2 : 178
        
        buffer = [178, 0]
        self.ser.write([buffer, self.checkSum(buffer)])
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

    def weight_mode(self): # mode_3 : 179
 
        buffer = [179, 165]
        self.ser.write([buffer, self.checkSum(buffer)])
        self.serialWait()
        serialRead = self.ser.read(2)
        serialList = []
        serialList.append(serialRead[0], serialRead[1])
        if ((serialRead[0] == 179)&(serialRead[1] == 164)):
            for i in range(5):
                serialList.append(self.ser.read(1))
            print(serialList)
            print(self.checkSum(serialList[:-1]))
            if(self.checkSum(serialList[:-1]) == serialList[-1]):
                self.weight = (serialList[2]*256 + serialList[3])
                print("Durian weight : " + str(self.weight) + ' kg')

    def force_mode(self): # mode_4 : 180

        buffer = [180, 163, int(self.r_axis_force/256), int(self.r_axis_force%256), int(self.theta_force/256), int(self.theta_force%256)]
        self.ser.write(buffer, self.checkSum(buffer))
        self.serialWait()
        serialRead = self.ser.read(2)
        serialList = []
        serialList.append(serialRead[0], serialRead[1])
        if ((serialRead[0] == 179)&(serialRead[1] == 164)):
            for i in range(5):
                serialList.append(self.ser.read(1))
            print(serialList)
            print(self.checkSum(serialList[:-1]))
            if(self.checkSum(serialList[:-1]) == serialList[-1]):
                self.force = (serialList[2]*256 + serialList[3])
                print("Force on durian stem : " + str(self.force) + ' N')

    def sound_mode(self): # mode_5 : 181

        buffer = [180, 163, int(self.r_axis_force/256), int(self.r_axis_force%256), int(self.theta_force/256), int(self.theta_force%256)]
        self.ser.write(buffer, self.checkSum(buffer))
        self.serialWait()
        serialRead = self.ser.read(2)
        serialList = []
        serialList.append(serialRead[0], serialRead[1])
        if ((serialRead[0] == 179)&(serialRead[1] == 164)):
            for i in range(501):
                serialList.append(self.ser.read(1))
            print(serialList)
            print(self.checkSum(serialList[:-1]))
            if(self.checkSum(serialList[:-1]) == serialList[-1]):
                print("Get Sound Signal.")

    def checkSum(self,dataFrame):
        return (~(sum(dataFrame)%256))%256

    def serialWait(self):
        while(self.ser.in_waiting == 0):
            pass
        
if __name__ == '__main__':
   app = Communication(platform.platform()[0].upper())
   sys.exit(app.exec_())








