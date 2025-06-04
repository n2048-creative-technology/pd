import time 
from dmx import send_batch_dmx
from random import random

port = '/dev/enttec'

send_batch_dmx(0,port)    # Off
        
