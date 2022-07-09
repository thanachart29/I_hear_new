from scipy.signal import find_peaks
from scipy.signal import lfilter
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import keras
import time
import cv2
import os

class PuCount(object):

    def __init__(self, model_name, frame, ret, image_size_w, image_size_h):

        self.model_name = model_name
        self.frame = frame
        self.ret = ret
        self.image_size_w = image_size_w
        self.image_size_h = image_size_h

    def imagePreprocess(self):

        if self.ret == False:
            return 0
        
        else:
            img = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            height, width, _ = img.shape
            if height != self.image_size_w:
                if(height > width):
                    tmp = int((self.image_size_h - self.image_size_w) / 2)
                    img = img[tmp:tmp + width, :]
                small = cv2.resize(img, (self.image_size_w,self.image_size_h))
            small = small/255
            return small

    def getRadius(self, input_img):

        filter = np.full((144, 256), 100)
        filtered = input_img - filter
        filtered[filtered<0] = 0
        filtered[filtered>0] = 255
        maxL = 0
        maxR = 143
        count = 0
        removeBgModel = tf.keras.model.load_model(self.model_name)
        res = removeBgModel.predict(np.array([input_img]))
        res = (res.reshape(self.image_size_h, self.image_size_w))*255
        while(True):
            if count >3:
                maxL -= 5
                break
            elif ((list(filtered[maxL]).count(255) != 0)):
                count += 1
            maxL += 1
        count = 0
        while(True):
            if count > 3:
                maxR += 5
                break
            elif ((list(filtered[maxR]).count(255) != 0)):
                count += 1
            maxR -= 1
        return (maxR - maxL)

    def predict(self, radiusDurian, a, n):

        y_axis = radiusDurian
        x_axis = list(range(1,len(radiusDurian)+1))
        n = 40
        b = [1.0 / n] * n
        a = 1
        reNoise = lfilter(b,a,y_axis)
        peaks, _ = find_peaks(reNoise, height=0)
        return peaks