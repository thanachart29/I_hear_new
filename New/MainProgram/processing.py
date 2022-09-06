from MainProgram.model.Mask_RCNN.mrcnn.config import Config
from MainProgram.model.Mask_RCNN.mrcnn import model as modellib, utils
from MainProgram.model.Mask_RCNN.mrcnn.defect import DefectConfig, InferenceConfig

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util

import tensorflow as tf
import numpy as np
import random
import math
import time
import six
import cv2
import os

class Master:

    def __init__(self):

        self.image_x = 640
        self.image_y = 360

        self.path = {
        'topcam_folder':os.path.join('storage', 'bottom'),
        'sidecam_folder':os.path.join('storage', 'side'),
        'stickcam_folder':os.path.join('storage', 'stick'),
        'top_checkpoint_path':os.path.join('symmetric', 'Model', 'my_ssd_mobnet4'),
        'stick_checkpoint_path':os.path.join('symmetric', 'Model', 'my_stick_ssd_mobnet2')
        }
        self.file = {
        'topcam_removeBG_model':os.path.join('symmetric', 'Model', 'RemoveBottomBackground2.h5'),
        'sidecam_removeBG_model':os.path.join('symmetric', 'Model', 'RemoveBackgroundVer9.h5'),
        'top_pipeline_config':os.path.join(self.path['top_checkpoint_path'], 'pipeline.config'),
        'stick_pipeline_config':os.path.join(self.path['stick_checkpoint_path'], 'pipeline.config'),
        'top_label_map':os.path.join('symmetric', 'annotations', 'label_map.pbtxt'),
        'stick_label_map':os.path.join('symmetric', 'annotations', 'stick_label_map2.pbtxt')
        }

        self.top_category_index = label_map_util.create_category_index_from_labelmap(self.file['top_label_map'])
        self.top_configs = config_util.get_configs_from_pipeline_file(self.file['top_pipeline_config'])
        self.top_detection_model = model_builder.build(model_config = self.top_configs['model'], is_training=False)
        self.top_ckpt = tf.compat.v2.train.Checkpoint(model = self.top_detection_model)
        self.top_ckpt.restore(os.path.join(self.path['top_checkpoint_path'], 'ckpt-201')).expect_partial()

        self.stick_category_index = label_map_util.create_category_index_from_labelmap(self.file['stick_label_map'])
        self.stick_configs = config_util.get_configs_from_pipeline_file(self.file['stick_pipeline_config'])
        self.stick_detection_model = model_builder.build(model_config = self.stick_configs['model'], is_training=False)
        self.stick_ckpt = tf.compat.v2.train.Checkpoint(model = self.stick_detection_model)
        self.stick_ckpt.restore(os.path.join(self.path['stick_checkpoint_path'], 'ckpt-201')).expect_partial()

        # Storage Part
        self.main_storage_path = 'MainProgram/storage'
        self.clip_storage_path = self.main_storage_path + '/clip'
        self.side_storage_path = self.main_storage_path + '/side'
        self.bottom_storage_path = self.main_storage_path + '/bottom'
        self.stick_storage_path = self.main_storage_path + '/stick'

        # Model Part
        self.main_model_path = 'MainProgram/model'
        self.sideRemoveModelName = 'RemoveBackgroundVer10.h5'
        self.sideRemoveModel = tf.keras.models.load_model(os.path.join(self.main_model_path, self.sideRemoveModelName))

        inference_config = InferenceConfig()
        model_detect_df_folder = self.main_model_path + '/Mask_RCNN/logs/defect20220821T1729'
        model_detect_df_name = 'mask_rcnn_defect_0010.h5'
        self.model_detect_df = modellib.MaskRCNN(mode="inference", config=inference_config, model_dir=model_detect_df_folder)
        self.model_detect_df.load_weights(os.path.join(model_detect_df_folder, model_detect_df_name), by_name=True)

        # Result Parameter Part
        self.defect_percent = 0

    @tf.function
    def bottom_detect_fn(self, image):
        image, shapes = self.top_detection_model.preprocess(image)
        prediction_dict = self.top_detection_model.predict(image, shapes)
        detections = self.top_detection_model.postprocess(prediction_dict, shapes)
        return detections

    @tf.function
    def stick_detect_fn(self, image):
        image, shapes = self.stick_detection_model.preprocess(image)
        prediction_dict = self.stick_detection_model.predict(image, shapes)
        detections = self.stick_detection_model.postprocess(prediction_dict, shapes)
        return detections

    def getCenterFromModel(self, detections, hight, width):
        ##### input detections['detection_boxes'][max score index]
        ##### output (x,y) 
        ymin = np.array(detections[0] * hight)
        xmin = np.array(detections[1] * width)
        ymax = np.array(detections[2] * hight)
        xmax = np.array(detections[3] * width)
        center_x = ((xmax - xmin)/2) + xmin
        center_y = ((ymax - ymin)/2) + ymin
        return center_x, center_y

    def rotatePointZaxis(self, angle, point):
        ##### Rotation Matrix #####
        theta = np.radians(angle)
        [cos, sin] = np.cos(theta), np.sin(theta)
        [x_new, y_new, z_new,  _] = [((point[0]*cos) - (point[1]*sin)), ((point[2]*sin) + (point[1]*cos)), point[2], 1]
        point_new = [x_new, y_new, z_new]
        
        return point_new

    def rotatePointXaxis(self, angle, point):
        ##### Rotation Matrix #####|
        theta = np.radians(angle)
        [cos, sin] = np.cos(theta), np.sin(theta)
        [x_new, y_new, z_new,  _] = [point[0], ((point[1]*cos) - (point[2]*sin)), ((point[1]*sin) + (point[2]*cos)), 1]
        point_new = [x_new, y_new, z_new]
        
        return point_new

    def transaltePointXaxis(self, x, point):
        [x_new, y_new, z_new, _] = [point[0] + x, point[1], point[2], 1]
        point_new = [x_new, y_new, z_new]

        return point_new

    def translatePointZaxis(self, z, point):
        [x_new, y_new, z_new, _] = [point[0], point[1], point[2] + z, 1]
        point_new = [x_new, y_new, z_new]

        return point_new

    def scaleMatrix(self, scale, point):
        [x_new, y_new, z_new, _] = [point[0]*scale[0], point[1]*scale[1], point[2]*scale[2], 1]
        point_new = [x_new, y_new, z_new]

        return point_new

    def Bottom_Detection(self, image):
        ##### return image with Input shape (360x640)#####
        src = cv2.resize(image, (self.image_x, self.image_y))
        [hight,width,_] = src.shape
        image_np = np.array(src).astype(np.uint8)
        
        input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
        detections = self.bottom_detect_fn(input_tensor)
        
        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
        detections['num_detections'] = num_detections
        
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
        
        label_id_offset = 1
        image_np_with_detections = image_np.copy()
        
        viz_utils.visualize_boxes_and_labels_on_image_array(
                    image_np_with_detections,
                    detections['detection_boxes'],
                    detections['detection_classes'] + label_id_offset,
                    detections['detection_scores'],
                    self.top_category_index,
                    use_normalized_coordinates = True,
                    max_boxes_to_draw = 2,
                    min_score_thresh = (0.18),
                    agnostic_mode = False)

        if(detections['detection_scores'][0] >= 0.18):
            detected = True
        else:
            detected = False
        
        bottom_detect_point = self.getCenterFromModel(detections['detection_boxes'][0], hight, width)
        
        return image_np_with_detections, bottom_detect_point, detected

    

    def imgPreProcess(self, image, size, color):
        if color:
            res_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            res_image = cv2.resize(image, size)
            return res_image
        else:
            res_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            res_image = cv2.resize(image, size)
            return res_image

    def find_defect(self):
        #Remove Background
        image_x = 256 #h
        image_y = 144 #w
        frameList = os.listdir(self.side_storage_path)
        frameAmount = len(frameList)
        for frame_name in frameList:
            frame_loc = self.side_storage_path + '/' + frame_name
            img = cv2.imread(frame_loc)
            img_resize = self.imgPreProcess(img, [image_x, image_y], True)
            img_resize = img_resize/255
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
            self.defect_percent += (defect_pixel/durian_pixel)*100
        self.defect_percent = self.defect_percent/frameAmount
        print('defect percent : ' + str(self.defect_percent) + '%')

    def puCountingFunction(self):
        #Remove Background
        image_x = 256 #h
        image_y = 144 #w
        maxR = 0
        maxL = 0
        radiusDurian = []
        frameList = os.listdir(self.clip_storage_path)
        frameAmount = len(frameList)
        for frame_name in frameList:
            frame_loc = self.clip_storage_path + '/' + frame_name
            side_frame = cv2.imread(frame_loc)
            preprocessed_frame = self.imgPreProcess(side_frame, [image_x, image_y], True)
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