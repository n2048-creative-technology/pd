#!/usr/bin/python3

import time 
from dmx import send_dmx
from random import random

port = '/dev/enttec'

send_dmx(2,255,port)    # On
time.sleep(0.05)  # ~20 fps, reasonable update rate
