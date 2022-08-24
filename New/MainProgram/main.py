from communication import Communicator
import time
# from processing import Master

class Main:

    def __init__(self):

        # self.main_processor = Master()
        self.main_communicator = Communicator()

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