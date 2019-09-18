import time
from datetime import datetime
import subprocess
import os

class camera:
    def __init__(self,n=None,m=None):
        self.n = n
        self.m = m
    def rotate (self):
        while True:
            os.system(('fswebcam  -S 3 --jpeg 50 --rotate {} --save /home/pi/to_transmit/%H%M%S.jpg').format(self.n))
            time.sleep(60)
    def invert(self):
        while True:
            os.system('fswebcam  -S 3 --jpeg 50 --invert --save /home/pi/to_transmit/%H%M%S.jpg')
            time.sleep(60)
    def greyscale(self):
        while True:
            os.system('fswebcam  -S 3 --jpeg 50 --greyscale --save /home/pi/to_transmit/%H%M%S.jpg')
            time.sleep(60)
    def resolution(self):
        while True:
            os.system(('fswebcam  -r {}*{} -S 3 --jpeg 50  --save /home/pi/to_transmit/%H%M%S.jpg').format(self.n,self.m))
            time.sleep(60)
    def default(self):
        while True:
            os.system(('fswebcam   --jpeg 50 --rotate 30 --save /home/pi/to_transmit/%H%M%S.jpg'))
            time.sleep(60)
            os.system('fswebcam  -S 3 --jpeg 50 --invert --save /home/pi/to_transmit/%H%M%S.jpg')
            time.sleep(60)
            os.system('fswebcam  -S 3 --jpeg 50 --greyscale --save /home/pi/to_transmit/%H%M%S.jpg')
            time.sleep(60)
            os.system(('fswebcam  -r 1900*1080 -S 3 --jpeg 50  --save /home/pi/to_transmit/%H%M%S.jpg'))
            time.sleep(60)

print("HEY ! ENTER THE TYPE OF PHOTOS YOU WANT")
c=input().split()
if(c[0]=="invert"):
    cam=camera()
    cam.invert()
        
elif(c[0]=="rotate"):
    cam=camera(c[1],0)
    cam.rotate()

elif(c[0]=="resolution"):
    cam=camera(c[1],c[2])
    cam.resolution()
        
elif(c[0]=="greyscale"):
    cam=camera()
    cam.greyscale()
      
else:
    cam=camera()
    cam.default()
        
