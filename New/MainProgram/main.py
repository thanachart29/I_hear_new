from MainProgram.communication import Communicator
# from MainProgram.processing import Master

class Main:

    def __init__(self):

        # self.main_processor = Master()
        pass

    def openConnection(self):
        
        self.main_communicator = Communicator()

    def getDurianData(self):
        self.main_communicator.resetStorage()
        for i in range(4):
            if self.main_communicator.communicateToDriverQuarter():
                if self.main_communicator.communicateToLED("TOP"):
                    self.main_communicator.imgCapture("TOP", i)
                if self.main_communicator.communicateToLED("SIDE"):
                    self.main_communicator.imgCapture("SIDE", i)
                if self.main_communicator.communicateToLED("BOTTOM"):
                    self.main_communicator.imgCapture("BOTTOM", i)
        self.main_communicator.videoCapture()
        self.main_communicator.communicateTOGripperAndSoundModule()