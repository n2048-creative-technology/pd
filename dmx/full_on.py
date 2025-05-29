import time 
from dmx import send_dmx
from random import random

port = '/dev/ttyUSB0'

for ch in range(12):
    send_dmx(ch+4,255,port)    # On
