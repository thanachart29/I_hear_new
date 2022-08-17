import tensorflow as tf
import keras
import cv2
import os

class Master:

    def __init__(self):
        # Storage Part
        self.main_storage_path = 'storage'
        self.clip_storage_path = self.main_storage_path + 'clip'
        self.side_storage_path = self.main_storage_path + 'side'
        self.bottom_storage_path = self.main_storage_path + 'bottom'
        self.stick_storage_path = self.main_storage_path + 'stick'

    def puCountingFunction(self):
        frameList = os.listdir(self.clip_storage_path)
        frameAmount = len(frameList)
        degPerFrame = 360/frameAmount
        for frame_name in frameList:
            frame_loc = self.clip_storage_path + '/' + frame_name
            img = cv2.imread(frame_loc)
            