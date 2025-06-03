# blink_test.py
import time
from dmx_controller import ramp_up, ramp_down

while True:
    ramp_up(4+9,3)
    ramp_down(4+9,3)
