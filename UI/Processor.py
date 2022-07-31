import threading
import queue

class Main:

    def __init__(self):

        que_Pu = queue.Queue()
        que_Shape = queue.Queue()
        que_Defect = queue.Queue()
        que_Hardness = queue.Queue()

        thread_Pu = threading.Thread(target = lambda q, arg : que_Pu.put(self.puCounter(arg)), args = (que_Pu, []))
        thread_Shape = threading.Thread(target = lambda q, arg : que_Shape.put(self.shapeDetector(arg)), args = (que_Shape, []))
        thread_Defect = threading.Thread(target = lambda q, arg : que_Defect.put(self.defectDetector(arg)), args = (que_Defect, []))
        thread_Hardness = threading.Thread(target = lambda q, arg : que_Hardness.put(self.hardnessChecker(arg)), args = (que_Hardness, []))

    def setData(self):
        pass

    def puCounter(self):
        pass

    def shapeDetector(self):
        pass

    def defectDetector(self):
        pass

    def hardnessChecker(self):
        pass