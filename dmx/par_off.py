#!/usr/bin/python3

import time 
from dmx import send_dmx
from random import random

port = '/dev/enttec'

try:
    while True:
        for ch in range(8):
            send_dmx(ch+1,0,port)    # On
            time.sleep(0.05)  # ~20 fps, reasonable update rate
except KeyboardInterrupt:
    pass
