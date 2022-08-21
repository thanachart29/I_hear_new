#GIT HUB LIBRARY
'''
import os 
# !!! CHANGE folder destination to save github repository
os.chdir('/content/drive/Shareddrives/Durian Project/Programming/Jearn/Colab/MaskRCNN_Ver5')  
!git clone https://github.com/njrean/Mask_RCNN.git
'''

#Use only this version!!!
'''
!pip install h5py==2.10.0
!pip install tensorflow==2.4.0 
!pip install keras==2.4.3
'''

#Need to Import
'''
import os 
import cv2
import numpy as np
import tensorflow as tf
import keras
'''
# !!! CHANGE to folder of library to import function in library
'''
os.chdir('/content/drive/Shareddrives/Durian Project/Programming/Jearn/Colab/MaskRCNN_Ver5/Mask_RCNN')
from mrcnn.config import Config
from mrcnn import model as modellib, utils
from mrcnn.defect import DefectConfig, InferenceConfig
'''

#Set Path to Model
# !!! CHANGE path to created model
'''
model_remove_bg_path = '/content/drive/Shareddrives/Durian Project/Programming/Jearn/model/RemoveBackgroundVer10.h5'                            #path to remove background model file
model_detect_df_folder = "/content/drive/Shareddrives/Durian Project/Programming/Jearn/Colab/MaskRCNN_Ver5/Mask_RCNN/logs/defect20220821T1729"  #just path to folder which has detect model inside
model_detect_df_name = 'mask_rcnn_defect_00010.h5'                                                                                              #name of detect model
'''

#Load Model
#-> for remove background
'''
model_remove_bg = tf.keras.models.load_model(model_remove_bg_path)
'''
#-> for detect defect
'''
inference_config = defect.InferenceConfig()
model_detect_df = modellib.MaskRCNN(mode="inference", config=inference_config, model_dir=model_detect_df_folder)
model_detect_df.load_weights(os.path.join(model_detect_df_folder, model_detect_df_name), by_name=True)
'''
#FUNCTION
def find_defect(img, model_remove_bg):
  #Remove Background
  image_x = 256 #h
  image_y = 144 #w
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  img_resize = cv2.resize(img, (image_x,image_y))
  img_resize = img_resize/255
  k = model_remove_bg.predict(np.array([img_resize]))
  k = k.reshape(image_y,image_x)
  _,k = cv2.threshold(k,0.3,1.0,cv2.THRESH_BINARY)

  durain_area = cv2.resize(k, (img.shape[1],img.shape[0]))
  durian_pixel = (durain_area > 0.3).sum()                  #count pixels which are durain

  k = cv2.resize(k,(img.shape[1],img.shape[0])).reshape(img.shape[0],img.shape[1],1)
  img_removed = np.multiply(img / 255.,np.repeat(k,3,axis = 2))
  img_removed_scale = img_removed * 255

  #Detect Background
  class_name = ['BG', 'defect']
  results = model_detect_df.detect([img_removed_scale], verbose=0)
  r = results[0]
  mask = r['masks']                                          #got mask of defect -> shape (1080,1920,x)
  mask = (np.sum(mask, -1, keepdims=True) >= 1)              #combine all mask
  defect_pixel = (mask == True).sum()                        #count pixels which are defect

  #Percentage
  defect_percent = (defect_pixel/durian_pixel)*100

  return defect_percent

#HOW TO USE
# !!! CHANGE path to image
'''
img_test_path = '/content/drive/Shareddrives/Durian Project/Programming/Jearn/Colab/MaskRCNN_Ver5/test/2022-06-16_00-05-44.jpg'
img = cv2.imread(img_test_path)
x = find_defect(img, model_remove_bg)
print('defect : {}%'.format(x))
'''