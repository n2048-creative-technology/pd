import time 
from dmx import send_dmx
from random import random

port = '/dev/ttyUSB0'
send_dmx(0,0,port)    # On
        