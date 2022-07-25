import platform
import serial
import time
import sys
import cv2

class Communication():

    def __init__(self, os):

        self.os = os
        if self.os == 'M': #Mac
            self.ser = serial.Serial('/dev/cu.usbmodem1103', 115200, parity='E', stopbits=1, timeout=1)
        elif self.os == 'W': #Windows
            self.ser = serial.Serial('COM10',115200,parity='E',stopbits=1,timeout=1)

        time.sleep(2)

        self.ready = False
        self.camera = False
        self.running = False
        self.takeImg = False
        self.takeClip = False
        
        self.count = 0
        self.force = []
        self.weight = []
        self.distance = []
        self.frame_list = []
        self.sound_magnitude = []
        self.r_axis_force = 0
        self.theta_force = 0
        self.theta_sound = 0
        self.h_axis_sound = 0
        buffer = [177]
        buffer.append(self.checkSum(buffer))
        self.ser.write(buffer)
        self.serialWait()
        serialRead = bytearray(self.ser.read(3))
        if (serialRead[2] == self.checkSum([serialRead[0], serialRead[1]])):
            self.start()
        else:
            pass

    def start(self):

        self.count += 1
        self.camera_mode()
        pass

    def camera_mode(self): # mode_2 : 178

        camera = cv2.VideoCapture(0)
        self.frame_list.append([])
        for i in range(4):
            self.fram_list.append([[], [], []])
            buffer = [178, 175]
            buffer.append(self.checkSum(buffer))
            self.ser.write(buffer)
            self.serialWait()
            serialRead = bytearray(self.ser.read(3))

            if ((serialRead[2] == self.checkSum([serialRead[0], serialRead[1]])) and (int(serialRead[1])%170 < 5)):
                for i in range(167,170,2):
                    buffer = [178, i]
                    buffer.append(self.checkSum(buffer))
                    self.ser.write(buffer)
                    self.serialWait()
                    serialRead = bytearray(self.ser.read(3))
                    if ((serialRead[2] == self.checkSum([serialRead[0], serialRead[1]])) & (serialRead[0] == 178)):
                        if (i == 167):
                            ret, frame = camera.read()
                            if(ret == True):
                                self.frame_list[len(self.frame_list) - 1][0].append(frame)
                        elif (i == 169):
                            ret, frame = camera.read()
                            if(ret == True):
                                self.frame_list[len(self.frame_list) - 1][1].append(frame)

                buffer = [178, 167]
                buffer.append(self.checkSum(buffer))
                self.ser.write(buffer)
                self.serialWait()
                serialRead = bytearray(self.ser.read(3))
                if ((serialRead[2] == self.checkSum([serialRead[0], serialRead[1]])) & (serialRead[0] == 178)):
                    startTime = time.time()*1000
                    while((time.time()*1000 - startTime) < 8150):
                        ret, frame = camera.read()
                        if(ret == True):
                            self.frame_list[len(self.frame_list) - 1][0].append(frame)

    def weight_mode(self): # mode_3 : 179
        
        buffer = [179, 165]
        buffer.append(self.checkSum(buffer))
        self.ser.write(buffer)
        self.serialWait()
        serialRead = bytearray(self.ser.read(2))
        # print(type(serialList))
        if ((serialRead[0] == 179)&(serialRead[1] == 164)):
            for i in range(5):
                serialRead.append(int.from_bytes(self.ser.read(1), "little"))  
            if(self.checkSum(serialRead[:-1]) == serialRead[-1]):
                self.weight.append(serialRead[2]*256 + serialRead[3])
                print("Durian weight : " + str(self.weight) + ' kg')

    def force_mode(self): # mode_4 : 180

        buffer = [180, 163, int(self.r_axis_force/256), int(self.r_axis_force%256), int(self.theta_force/256), int(self.theta_force%256)]
        buffer.append(self.checkSum(buffer))
        self.ser.write(buffer)
        self.serialWait()
        serialRead = bytearray(self.ser.read(2))

        if ((serialRead[0] == 180)&(serialRead[1] == 162)):
            for i in range(5):
                serialRead.append(int.from_bytes(self.ser.read(1), "big"))
            
            print(list(serialRead))
            print(self.checkSum(serialRead[:-1]))
            if(self.checkSum(serialRead[:-1]) == serialRead[-1]):
                self.force.append(serialRead[2]*256 + serialRead[3])
                self.distance.append(serialRead[4]*256 + serialRead[5])
                print("Force on durian stem : " + str(self.force) + ' N')
                print("Distance on durian stem : " + str(self.distance) + ' N')

    def sound_mode(self): # mode_5 : 181

        buffer = [181, 161, int(self.r_axis_force/256), int(self.r_axis_force%256), int(self.theta_force/256), int(self.theta_force%256)]
        buffer.append(self.checkSum(buffer))
        self.ser.write(buffer)
        self.serialWait()
        serialRead = bytearray(self.ser.read(2))

        if ((serialRead[0] == 181)&(serialRead[1] == 160)):
            for i in range(1003):
                serialRead.append(int.from_bytes(self.ser.read(1), "little"))
            if(self.checkSum(serialRead[:-1]) == serialRead[-1]):
                self.sound_magnitude.append([])
                for k in range(2,1004,2):
                    self.sound_magnitude[len(self.sound_magnitude) - 1].append(serialRead[k]*256 + serialRead[k+1])

    def checkSum(self,dataFrame):
        return (~(sum(dataFrame)%256))%256

    def serialWait(self):
        while(self.ser.in_waiting == 0):
            pass
        
if __name__ == '__main__':
    os = platform.platform()[0].upper()
    print(os)
    app = Communication(os)
    sys.exit(app.exec_())








