import threading
import queue
import time

class Main:

    def __init__(self):
        self.pu = ''
        self.shape = ''
        self.defect = ''
        self.hardness = ''

        self.test1 = ['_123']
        self.test2 = ['_321']
        self.test3 = ['_313']
        self.test4 = ['_424']

        self.thread_Pu = threading.Thread(target = self.puCounter, args=self.test1)
        self.thread_Shape = threading.Thread(target = self.shapeDetector, args=self.test2)
        self.thread_Defect = threading.Thread(target = self.defectDetector, args=self.test3)
        self.thread_Hardness = threading.Thread(target = self.hardnessChecker, args=self.test4)

    def run(self):
        test = time.time()
        self.thread_Pu.start()
        self.thread_Shape.start()
        self.thread_Defect.start()
        self.thread_Hardness.start()

        self.thread_Pu.join()
        self.thread_Shape.join()
        self.thread_Defect.join()
        self.thread_Hardness.join()
        print('runtime : ' + str(time.time() - test) + ' sec.')
        print('Pu : ' + self.pu)
        print('Shape : ' + self.shape)
        print('Defect : ' + self.defect)
        print('Hardness : ' + self.hardness)

    def setData(self):
        pass

    def getData(self):
        pass

    def puCounter(self, a):
        time.sleep(4)
        self.pu = 'Pu' + str(a)

    def shapeDetector(self, b):
        time.sleep(3)
        self.shape = 'Shape' + str(b)

    def defectDetector(self, c):
        time.sleep(2)
        self.defect = 'Defect' + str(c)

    def hardnessChecker(self, d):
        time.sleep(1)
        self.hardness = 'Hardness' + str(d)