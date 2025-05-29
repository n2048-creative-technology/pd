import time 
from dmx import send_dmx
from random import random

port = '/dev/ttyUSB1'

while 1:
    for i in range(256):
        send_dmx(4+(int)(random()*2),(int)(random()*255),port)    # On
        time.sleep(random()/10)
