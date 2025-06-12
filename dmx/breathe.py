#!/usr/bin/python3

import time 
from dmx import send_dmx, send_batch_dmx
from random import random

port = '/dev/ttyUSB0'

period=2
steps=256;
wait_time=period/steps
max_intensity=255

while 1:
    for i in range(steps):
        send_batch_dmx((int)(i*max_intensity/steps),port)    # fade in
        time.sleep(wait_time)
    for i in range(steps):
        send_batch_dmx((int)(max_intensity-i*max_intensity/steps),port)    # fade out
        time.sleep(wait_time)
