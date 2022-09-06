from communication import Communicator
import time
import os
# from processing import Master

class Main:

    def __init__(self):
        
        # self.main_processor = Master()
        self.main_communicator = Communicator()

    def resetDurianData(self):

        os.chdir(self.main_communicator.main_storage_path)
        os.chdir('clip')
        for i in os.listdir():
            os.remove(i)
        print(os.listdir())
        os.chdir(self.main_communicator.main_storage_path)
        os.chdir('side')
        for i in os.listdir():
            os.remove(i)
        print(os.listdir())
        os.chdir(self.main_communicator.main_storage_path)
        os.chdir('stick')
        for i in os.listdir():
            os.remove(i)
        print(os.listdir())
        os.chdir(self.main_communicator.main_storage_path)
        os.chdir('bottom')
        for i in os.listdir():
            os.remove(i)
        print(os.listdir())

    def getDurianData(self):

        for i in range(4):
            if self.main_communicator.communicateToDriverQuarter():
                if self.main_communicator.communicateToLED("TOP"):
                    self.main_communicator.imgCapture("TOP", i+1)
                if self.main_communicator.communicateToLED("SIDE"):
                    self.main_communicator.imgCapture("SIDE", i+1)
                if self.main_communicator.communicateToLED("BOTTOM"):
                    self.main_communicator.imgCapture("BOTTOM", i+1)
        self.main_communicator.communicateToLoadcell()
        if self.main_communicator.communicateToLED("SIDE"):
            self.main_communicator.videoCapture()
            self.main_communicator.serialWait()
            check = list(self.main_communicator.main_connection.read(3))
            if ((check[0] == 177) and (check[1] == 176) and (check[2] == 158)):
                print('All durian image is rescieved.')

    def process(self):
        pass

    def getFuturePlanData(self):
        self.main_communicator.communicateTOGripperAndSoundModule()