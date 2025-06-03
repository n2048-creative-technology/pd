# blink_test.py
import time
from dmx_controller import send_dmx

while True:
    send_dmx(4, 255)   # On
    time.sleep(1)
    send_dmx(4, 0)     # Off
    time.sleep(1)
    send_dmx(5, 255)   # On
    time.sleep(1)
    send_dmx(5, 0)     # Off
    time.sleep(1)
