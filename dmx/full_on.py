#!/usr/bin/python3

import time 
from dmx import send_batch_dmx
from random import random

port = '/dev/enttec'

send_batch_dmx(50, port)
time.sleep(0.05)  # ~20 fps, reasonable update rate

