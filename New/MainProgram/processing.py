from New.MainProgram.model.Mask_RCNN.mrcnn.config import Config
from New.MainProgram.model.Mask_RCNN.mrcnn import model as modellib, utils
from New.MainProgram.model.Mask_RCNN.mrcnn.defect import DefectConfig, InferenceConfig

import tensorflow as tf
import numpy as np
import cv2
import os

class Master:

    def __init__(self):
        # Storage Part
        self.main_storage_path = 'New/MainProgram/storage'
        self.clip_storage_path = self.main_storage_path + '/clip'
        self.side_storage_path = self.main_storage_path + '/side'
        self.bottom_storage_path = self.main_storage_path + '/bottom'
        self.stick_storage_path = self.main_storage_path + '/stick'

        # Model Part
        self.main_model_path = 'New/MainProgram/model/'
        self.sideRemoveModel = tf.keras.models.load_model(self.main_model_path + 'RemoveBackgroundVer10.h5')

        inference_config = InferenceConfig()
        model_detect_df_folder = self.main_model_path + 'Mask_RCNN/logs/defect20220821T1729'
        model_detect_df_name = 'mask_rcnn_defect_00010.h5'
        self.model_detect_df = modellib.MaskRCNN(mode="inference", config=inference_config, model_dir=model_detect_df_folder)
        self.model_detect_df.load_weights(os.path.join(model_detect_df_folder, model_detect_df_name), by_name=True)


    def imgPreProcess(self, image, size, color):
        if color:
            res_image = cv2.resize(image, size)
            res_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return res_image
        else:
            res_image = cv2.resize(image, size)
            res_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            return res_image

    def find_defect(self):
        #Remove Background
        image_x = 256 #h
        image_y = 144 #w
        img_name = os.listdir(self.side_storage_path)[0]
        img = cv2.imread(self + '/' + img_name)
        img_resize = (self.imgPreProcess(img, (image_x, image_y), True))/255
        k = self.sideRemoveModel.predict(np.array([img_resize]))
        k = k.reshape(image_y,image_x)
        _,k = cv2.threshold(k,0.3,1.0,cv2.THRESH_BINARY)

        durain_area = cv2.resize(k, (img.shape[1],img.shape[0]))
        durian_pixel = (durain_area > 0.3).sum()                  #count pixels which are durain

        k = cv2.resize(k,(img.shape[1],img.shape[0])).reshape(img.shape[0],img.shape[1],1)
        img_removed = np.multiply(img / 255.,np.repeat(k,3,axis = 2))
        img_removed_scale = img_removed * 255

        #Detect Background
        class_name = ['BG', 'defect']
        results = self.model_detect_df.detect([img_removed_scale], verbose=0)
        r = results[0]
        mask = r['masks']                                          #got mask of defect -> shape (1080,1920,x)
        mask = (np.sum(mask, -1, keepdims=True) >= 1)              #combine all mask
        defect_pixel = (mask == True).sum()                        #count pixels which are defect

        #Percentage
        self.defect_percent = (defect_pixel/durian_pixel)*100


    def puCountingFunction(self):
        maxR = 0
        maxL = 0
        radiusDurian = []
        frameList = os.listdir(self.clip_storage_path)
        frameAmount = len(frameList)
        for frame_name in frameList:
            frame_loc = self.clip_storage_path + '/' + frame_name
            side_frame = cv2.imread(frame_loc)
            preprocessed_frame = self.imgPreProcess(side_frame, (256, 144), True)
            input_array = preprocessed_frame/255
            output_array = self.sideRemoveModel.predict(np.array([input_array]))
            output_frame = (output_array.reshape(144,256))*255
            filtered_frame = cv2.threshold(output_frame, 0.6)
            while (True):
                if count >3:
                    maxL -= 5
                    break
                elif ((list(filtered_frame[maxL]).count(255) != 0)):
                    count += 1
                maxL += 1
                count = 0
            while(True):
                if count > 3:
                    maxR += 5
                    break
                elif ((list(filtered_frame[maxR]).count(255) != 0)):
                    count += 1
                maxR -= 1
                radiusDurian.append(maxR - maxL)

        y_axis = radiusDurian
        reNoise = []
        for i in range(len(y_axis)):
            if i < 5:
                reNoise.append(sum(y_axis[i:i+5])/5)
            elif i > len(y_axis)-6:
                reNoise.append(sum(y_axis[i-4:i+1])/5)
            else:
                reNoise.append(sum(y_axis[i-5:i+6])/11)

        reNoise = np.asarray(reNoise)
        test1 = list(reNoise)
        test1.extend(test1[0:test1.index((min(test1)))])
        del test1[0:test1.index((min(test1)))]
        reNoise = np.asarray(test1)

        test = []
        ans = []
        count = 0
        stock = 0

        for i in range(5, len(reNoise)-5, 1):
            condition3 = ((reNoise[i-5] - reNoise[i])/5 > 0) 
            condition4 = ((reNoise[i+5] - reNoise[i])/5 > 0)
            if (condition3 and ((reNoise[i+5] - reNoise[i])/5 >= -0.025)):
                test.append(i)
            elif (condition4 and ((reNoise[i-5] - reNoise[i])/5 >= -0.025)):
                test.append(i)

        for i in (range(0,len(test)-1,1)):
            if (test[i+1] - test[i] < 8):
                stock += test[i]
                count += 1
            if ((test[i+1] - test[i] >= 8) and count > 0):
                print('Count : ' + str(count))
                ans.append(int(stock/count))
                count = 0
                stock = 0
            elif ((test[i+1] - test[i] >= 8) and count <= 0):
                count = 0
                stock = 0
        if (stock > 0 and count > 0):
            print('Count : ' + str(count))
            ans.append(int(stock/count))
            count = 0
            stock = 0

        puCount = len(ans) + 1
        puList = list(ans)
        condition1 = ((len(reNoise)*1)/(puCount*2))
        condition2 = ((len(reNoise)*1)/(puCount*4))
        if ((puCount-1) == len(puList)):
            puList.insert(0,0)
            puList.append(len(reNoise))
        puList = sorted(puList, reverse=True)
        puTypeList = []

        for i in range(len(puList)-1):
            if ((puList[i] - puList[i+1]) > condition1):
                puTypeList.insert('Complete_Pu', 0)
            elif ((puList[i] - puList[i+1]) < condition2):
                puTypeList.insert('Incorrect_Pu', 0)
            else:
                puTypeList.insert('Incomplete_Pu', 0)