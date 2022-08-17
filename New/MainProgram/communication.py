import platform
import serial
import time
import cv2

class Communicator:

    def __init__(self):

        # Connection Part
        main_OS = platform.platform()[0].upper()
        if main_OS == 'M': #Mac
            self.main_connection = serial.Serial('/dev/cu.usbmodem1201', 115200, parity='E', stopbits=1, timeout=1)
        elif main_OS == 'W': #Windows
            self.main_connection = serial.Serial('COM10',115200,parity='E',stopbits=1,timeout=1)
        else:
            print("!!Connection error.")

        self.communication_Rx_buffer = []
        self.communication_Tx_buffer = []
        
        # Storage Part
        self.main_storage_path = 'storage'
        self.clip_storage_path = self.main_storage_path + 'clip'
        self.side_storage_path = self.main_storage_path + 'side'
        self.bottom_storage_path = self.main_storage_path + 'bottom'
        self.stick_storage_path = self.main_storage_path + 'stick'

        # Camera Part
        self.top_camera_number = 2
        self.side_camera_number = 0
        self.bottom_camera1_number = 1
        self.bottom_camera2_number = 3
        self.focus_time = 0.1

        # Parameters Part
        self.sound_magnitude = [] # Magnitude of sound in 0 - 500 Hz
        self.force_magnitude = [] # Magnitude of force in 0 - 3 mm
        self.press_distance = [] # Distance of Gripper press in Durian stick

    def serialWait(self):
        while (self.main_connection.in_waiting == 0):
            pass

    def checkSum(self, dataFrame):
        return (~(sum(dataFrame)%256))%256

    def imgCapture(self, camState):
        if camState == "TOP" or camState == "SIDE":
            if camState == "TOP":
                camera = cv2.VideoCapture(self.top_camera_number)
                while not camera.isOpened():
                    pass
                name = "bottom_img"
                path = self.bottom_storage_path + "/" + name + ".jpg"
            elif camState == "SIDE":
                camera = cv2.VideoCapture(self.top_camera_number)
                while not camera.isOpened():
                    pass
                name = "side_img"
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
            name1 = "stick_img_frame1"
            name2 = "stick_img_frame2"
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
        startTime = time.time()*1000
        time.sleep(self.focus_time)
        while ((time.time()*1000) - startTime <= 7150):
            ret, frame = camera.read()
            if ret == True:
                count += 1
                cv2.imwrite(self.clip_storage_path + '/' + count + '.jpg', frame)
        camera.release()

    def communicateToDriver(self):
        pass

    def communicateToLED(self, ledState):
        if ledState == "TOP":
            self.communication_Tx_buffer = [178, 169]
            self.communication_Tx_buffer.append(self.checkSum(self.communication_buffer))
            self.main_connection.write(self.communication_Tx_buffer)
            self.serialWait()
            for i in range(3):   
                self.communication_Rx_buffer.append(self.main_connection.read(1))
            if self.communication_Rx_buffer[-1] == self.checkSum(self.communication_Rx_buffer[0:2]):
                print('Top LED is opened.')
                return True
            else:
                print('Failed to open Top LED.')
                return False
        elif ledState == "SIDE":
            self.communication_Tx_buffer = [178, 167]
            self.communication_Tx_buffer.append(self.checkSum(self.communication_buffer))
            self.main_connection.write(self.communication_Tx_buffer)
            self.serialWait()
            for i in range(3):   
                self.communication_Rx_buffer.append(self.main_connection.read(1))
            if self.communication_Rx_buffer[-1] == self.checkSum(self.communication_Rx_buffer[0:2]):
                print('Side LED is opened.')
                return True
            else:
                print('Failed to open Side LED.')
                return False
        elif ledState == "BOTTOM":
            self.communication_Tx_buffer = [178, 165]
            self.communication_Tx_buffer.append(self.checkSum(self.communication_buffer))
            self.main_connection.write(self.communication_Tx_buffer)
            self.serialWait()
            for i in range(3):   
                self.communication_Rx_buffer.append(self.main_connection.read(1))
            if self.communication_Rx_buffer[-1] == self.checkSum(self.communication_Rx_buffer[0:2]):
                print('Bottom LED is opened.')
                return True
            else:
                print('Failed to open Bottom LED.')
                return False
          
