#!/usr/bin/python3

import time 
from dmx import send_dmx, send_batch_dmx
from random import random

port = '/dev/enttec'
max_intensity = 100

send_batch_dmx(0)


try:
    while 1:
        ch=(int)(random()*12)+9
        send_dmx(ch,(int)(random()*max_intensity),port)    # On
except KeyboardInterrupt:
    pass
