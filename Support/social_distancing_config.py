# base path to YOLO directory
from sqlalchemy import true

# define the minimum safe distance (in pixels) that two people can be
# from each other
MIN_DISTANCE = 50

MODEL_PATH = "C:\\Users\\Krishna\\OneDrive\\Desktop\\Realtime-Social-Distance-Detection-with-GUI-in-Python-main\\Support\\yolo-coco"

# initialize minimum probability to filter weak detections along with
# the threshold when applying non-maxima suppression
MIN_CONF = 0.3
NMS_THRESH = 0.3

#social distance enable
USE_SOCIAL_DISTANCE=True

#realtime Human Count
USE_HUMAN_COUNT=True

#use both
USE_BOTH=True

#boolean to check whether mobile camera is used 
USE_MOBILE_CAMERA=False

#device camera
USE_DEVICE_CAMERA=True

#ip webcam address
IP_WEBCAM_ADDRESS="none"

# boolean indicating if NVIDIA CUDA GPU should be used
USE_GPU = True

#cpu should be used
USE_CPU = True

#define max number of people at a time.
#if it increases above limit alarm triggered
MAX_PEOPLE=20

#Data social distance and human count
USE_DATA_BOTH=True

#Data social distance
USE_DATA_SOCIAL_DISTANCE=True

#Data human count
USE_DATA_HUMAN_COUNT=True

#Write Data Text File
Write_Data_Text_File=True

#Write Data Word File
Write_Data_Word_File=True

#no data write
No_Data_Write=True

#write data excel file
Write_Data_Excel_File=True

#camera check
webcamworking=True
