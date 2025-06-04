import time 
from dmx import send_batch_dmx
from random import random

port = '/dev/ttyUSB0'

send_batch_dmx(0,port)    # Off
        
