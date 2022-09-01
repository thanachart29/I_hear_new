from communication import Communicator
from processing import Master

class Main:

    def __init__(self):

        self.main_processor = Master()

    def openConnection(self):
        
        self.main_communicator = Communicator()

    def getDurianData(self):

        for i in range(4):
            if self.main_communicator.communicateToDriver():
                if self.main_communicator.communicateToLED("TOP"):
                    self.main_communicator.imgCapture("TOP")
                if self.main_communicator.communicateToLED("SIDE"):
                    self.main_communicator.imgCapture("SIDE")
                if self.main_communicator.communicateToLED("BOTTOM"):
                    self.main_communicator.imgCapture("BOTTOM")
            