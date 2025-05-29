import time 
from dmx import send_dmx

port = '/dev/ttyUSB1'

period=.1
wait_time=period/255.

while 1:
    for i in range(256):
        send_dmx(4,i,port)    # On
        time.sleep(wait_time)
    for i in range(256):
        send_dmx(5,i,port)    # On
        time.sleep(wait_time)
    for i in range(256):
        send_dmx(4,255-i,port)    # On
        time.sleep(wait_time)
    for i in range(256):
        send_dmx(5,255-i,port)    # On
        time.sleep(wait_time)
