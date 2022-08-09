from scipy.signal import find_peaks
from scipy.signal import lfilter
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import threading
import time
import cv2
import os

class Main:

    def __init__(self):

        self.model_name = tf.keras.models.load_model('RemoveBackgroundVer9.h5')

        self.puAmount = ''
        self.shape = ''
        self.percentDefect = ''
        self.hardnessType = ''

        self.clip = 0
        self.top_image = 0
        self.rear_image = 0
        self.bottom_image = 0
        self.magnitude_force = 0
        self.magnitude_sound = 0

        self.thread_Pu = threading.Thread(target = self.puCounter)
        self.thread_Shape = threading.Thread(target = self.shapeDetector)
        self.thread_Defect = threading.Thread(target = self.defectDetector)
        self.thread_Hardness = threading.Thread(target = self.hardnessChecker)

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

    def setData(self, clip, rear_img, top_image,  bottom_image, force, sound):

        self.clip = clip
        self.top_image = top_image
        self.rear_image = rear_img
        self.bottom_img = bottom_image
        self.magnitude_force = force
        self.magnitude_sound = sound

    def returnValue(self):

        return [self.puAmount, self.shape, self.percentDefect, self.hardnessType]

    def puCounter(self):

        time.sleep(4)
        self.puAmount = 'Pu'

    def shapeDetector(self):

        time.sleep(3)
        self.shape = 'Shape'

    def defectDetector(self):

        time.sleep(2)
        self.percentDefect = 'Defect'

    def hardnessChecker(self):

        time.sleep(1)
        self.hardnessType = 'Hardness'