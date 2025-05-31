import time 
from dmx import send_batch_dmx
from random import random

port = '/dev/ttyUSB0'

for ch in range(12):
    send_batch_dmx(255,port)    # On
