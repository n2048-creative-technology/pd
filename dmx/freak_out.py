import time 
from dmx import send_dmx
from random import random

port = '/dev/ttyUSB0'
max_intensity = 30

while 1:
    for i in range(10):
        ch1=(int)(random()*7)+4
        ch2=(int)(random()*7)+4
        send_dmx(ch1,(int)(random()*max_intensity),port)    # On
        send_dmx(ch2,(int)(random()*max_intensity),port)    # On
        time.sleep(random()/10)
    send_dmx(ch1,0,port)    # On
    send_dmx(ch2,0,port)    # On
        