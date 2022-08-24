import platform
import serial
import time
import cv2

class Communicator:

    def __init__(self):
        # Connection Part
        main_OS = platform.platform()[0].upper()
        if main_OS == 'M': #Mac
            self.main_connection = serial.Serial('/dev/cu.usbmodem1101', 115200, parity='E', stopbits=1, timeout=1)
        elif main_OS == 'W': #Windows
            self.main_connection = serial.Serial('COM10',115200,parity='E',stopbits=1,timeout=1)
        else:
            print("!!Connection error.")
        time.sleep(2)
        self.serialWait()
        check = list(self.main_connection.read(3))

        if ((check[0] == 177) and (check[1] == 176) and (check[2] == 158)):
            print('Connection established successfully')
        else:
            print('Communication Error')

        self.communication_Rx_buffer = []
        self.communication_Tx_buffer = []
        
        # Storage Part
        self.main_storage_path = 'MainProgram/storage'
        self.clip_storage_path = self.main_storage_path + '/clip'
        self.side_storage_path = self.main_storage_path + '/side'
        self.bottom_storage_path = self.main_storage_path + '/bottom'
        self.stick_storage_path = self.main_storage_path + '/stick'

        # Camera Part
        self.top_camera_number = 2
        self.side_camera_number = 0
        self.bottom_camera1_number = 1
        self.bottom_camera2_number = 4
        self.focus_time = 0.5

        # Parameters Part
        self.sound_magnitude = [] # Magnitude of sound in 0 - 500 Hz
        self.force_magnitude = [] # Magnitude of force in 0 - 3 mm
        self.press_distance = [] # Distance of Gripper press in Durian stick
        self.current_theta = 0 # current angle of Durian Base
        self.weight = 0.0 # Weight of current durian on Durian Base

    def serialWait(self):
        while (self.main_connection.in_waiting == 0):
            pass

    def imgCapture(self, camState, count):
        if camState == "TOP" or camState == "SIDE":
            if camState == "TOP":
                camera = cv2.VideoCapture(self.top_camera_number)
                while not camera.isOpened():
                    pass
                name = "bottom_img_" + str(count)
                path = self.bottom_storage_path + "/" + name + ".jpg"
            elif camState == "SIDE":
                camera = cv2.VideoCapture(self.side_camera_number)
                while not camera.isOpened():
                    pass
                name = "side_img_" + str(count)
                path = self.side_storage_path + "/" + name + ".jpg"
            time.sleep(self.focus_time)
            ret, frame = camera.read()
            if ret == True:
                cv2.imwrite(path, frame)
                print(name + " recieved.")
            camera.release()
        elif camState == "BOTTOM":
            camera1 = cv2.VideoCapture(self.bottom_camera1_number)
            camera2 = cv2.VideoCapture(self.bottom_camera2_number)
            while not camera1.isOpened():
                while not camera2.isOpened():
                    pass   
                pass
            camera1.set(3, 1280)
            camera2.set(3, 1280)
            camera1.set(4, 720)
            camera2.set(4, 720)
            name1 = "stick_img_frame1_" + str(count)
            name2 = "stick_img_frame2_" + str(count)
            path1 = self.stick_storage_path + "/" + name1 + ".jpg"
            path2 = self.stick_storage_path + "/" + name2 + ".jpg"
            time.sleep(self.focus_time)
            ret1, frame1 = camera1.read()
            ret2, frame2 = camera2.read()
            if ret1 == True:
                cv2.imwrite(path1, frame1)
                print(name1 + " recieved.")
            if ret2 == True:
                cv2.imwrite(path2, frame2)
                print(name2 + " recieved.")
            camera1.release()
            camera2.release()

    def videoCapture(self):
        count = 0
        camera = cv2.VideoCapture(self.side_camera_number)
        while not camera.isOpened():
            pass
        self.communicateToDriverFull()
        startTime = time.time()*1000
        while (time.time()*1000 - startTime <= 8150):
            ret, frame = camera.read()
            if ret == True:
                count += 1
                cv2.imwrite(self.clip_storage_path + '/' + str(count) + '.jpg', frame)
                print('frame is recieved.')
        camera.release()

    def communicateToLoadcell(self):
        self.communication_Tx_buffer = [179, 163, 169]
        self.main_connection.write(self.communication_Tx_buffer)
        self.serialWait()
        self.communication_Rx_buffer = list(self.main_connection.read(7))
        print(self.communication_Rx_buffer)

    def communicateToLED(self, ledState):
        if ledState == "TOP":
            self.communication_Tx_buffer = [178, 165, 168]
            self.main_connection.write(self.communication_Tx_buffer)
            self.serialWait()
            self.communication_Rx_buffer = list(self.main_connection.read(3))
            if self.communication_Rx_buffer[-1] == 158:
                print('Top LED is opened.')
                return True
            else:
                print('Failed to open Top LED.')
                return False
        elif ledState == "SIDE":
            self.communication_Tx_buffer = [178, 167, 166]
            self.main_connection.write(self.communication_Tx_buffer)
            self.serialWait()
            self.communication_Rx_buffer = list(self.main_connection.read(3))
            if self.communication_Rx_buffer[-1] == 158:
                print('Side LED is opened.')
                return True
            else:
                print('Failed to open Side LED.')
                return False
        elif ledState == "BOTTOM":
            self.communication_Tx_buffer = [178, 169, 164]
            self.main_connection.write(self.communication_Tx_buffer)
            self.serialWait()
            self.communication_Rx_buffer = list(self.main_connection.read(3))
            if self.communication_Rx_buffer[-1] == 158:
                print('Bottom LED is opened.')
                return True
            else:
                print('Failed to open Bottom LED.')
                return False
          
    def communicateToDriverQuarter(self):
        self.communication_Tx_buffer = [178, 175, 158]
        self.main_connection.write(self.communication_Tx_buffer)
        self.serialWait()
        self.communication_Rx_buffer = list(self.main_connection.read(3))
        if self.communication_Rx_buffer[-1] == 158:
            return True
        else:
            return False

    def communicateToDriverFull(self):
        self.communication_Tx_buffer = [178, 174, 159]
        self.main_connection.write(self.communication_Tx_buffer)