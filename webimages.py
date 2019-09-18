import time
import datetime
import os
import subprocess
import azure
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

block_blob_service = BlockBlobService(account_name='account_name' , account_key='account_key')

class camera:
    def __init__(self,n=None,m=None):
        self.n = n
        self.m = m
    
    def default(self):
        name_plant = input("Enter which plant it is ?")
        while True:
            f=datetime.datetime.now()
            os.system(('fswebcam -F 30 -S 3 --jpeg 50 --no-banner --save /home/pi/Downloads/redirect/{}.jpg').format(f.strftime("%m%d%H%S")+name_plant))
            block_blob_service.create_blob_from_path('hydroponics','INTERNAL/{}.jpg'.format(f.strftime("%m%d%H%S")+name_plant),'/home/pi/Downloads/redirect/{}.jpg'.format(f.strftime("%m%d%H%S")+name_plant),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)
            f2=datetime.datetime.now()
            os.system(('fswebcam  -F 30 -S 3 --jpeg 50 --no-banner --rotate 90 --save /home/pi/Downloads/redirect/{}.jpg').format(f2.strftime("%m%d%H%S")+name_plant))
            block_blob_service.create_blob_from_path('hydroponics','INTERNAL/{}.jpg'.format(f2.strftime("%m%d%H%S")+name_plant),'/home/pi/Downloads/redirect/{}.jpg'.format(f2.strftime("%m%d%H%S")+name_plant),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)
            f3=datetime.datetime.now()
            os.system(('fswebcam  -F 30 -S 3 --jpeg 50 --no-banner --invert --save /home/pi/Downloads/redirect/{}.jpg').format(f3.strftime("%m%d%H%S")+name_plant))
            block_blob_service.create_blob_from_path('hydroponics','INTERNAL/{}.jpg'.format(f3.strftime("%m%d%H%S")+name_plant),'/home/pi/Downloads/redirect/{}.jpg'.format(f3.strftime("%m%d%H%S")+name_plant),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)
            f4=datetime.datetime.now()
            os.system(('fswebcam  -F 30 -S 3 --jpeg 50 --no-banner --greyscale --save /home/pi/Downloads/redirect/{}.jpg').format(f4.strftime("%m%d%H%S")+name_plant))
            block_blob_service.create_blob_from_path('hydroponics','INTERNAL/{}.jpg'.format(f4.strftime("%m%d%H%S")+name_plant),'/home/pi/Downloads/redirect/{}.jpg'.format(f4.strftime("%m%d%H%S")+name_plant),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)
            f5=datetime.datetime.now()
            os.system(('fswebcam  -F 30 -S 3 --no-banner -S 3 --jpeg 50  --save /home/pi/Downloads/redirect/{}.jpg').format(f5.strftime("%m%d%H%S")+name_plant))
            block_blob_service.create_blob_from_path('hydroponics','INTERNAL/{}.jpg'.format(f5.strftime("%m%d%H%S")+name_plant),'/home/pi/Downloads/redirect/{}.jpg'.format(f5.strftime("%m%d%H%S")+name_plant),content_settings=ContentSettings(content_type = 'image/jpeg'))
            time.sleep(60)

cam=camera()
cam.default()
        

