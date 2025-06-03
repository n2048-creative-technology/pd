# dmx_controller.py
import serial

def send_dmx(ch, value, port='/dev/ttyUSB0', baudrate=57600):
    start_code = 0x00
    dmx_data = bytearray([0] * 512)
    dmx_data[ch - 1] = value

    message = bytearray()
    message.append(0x7E)
    message.append(0x06)

    data_length = len(dmx_data) + 1
    message.append(data_length & 0xFF)
    message.append((data_length >> 8) & 0xFF)

    message.append(start_code)
    message.extend(dmx_data)
    message.append(0xE7)

    with serial.Serial(port, baudrate=baudrate) as ser:
        ser.write(message)
# dmx_controller.py
import serial
import time

def send_dmx(ch, value, port='/dev/ttyUSB0', baudrate=57600):
    start_code = 0x00
    dmx_data = bytearray([0] * 512)
    dmx_data[ch - 1] = value

    message = bytearray()
    message.append(0x7E)
    message.append(0x06)

    data_length = len(dmx_data) + 1
    message.append(data_length & 0xFF)
    message.append((data_length >> 8) & 0xFF)

    message.append(start_code)
    message.extend(dmx_data)
    message.append(0xE7)

    with serial.Serial(port, baudrate=baudrate) as ser:
        ser.write(message)


def ramp_up(channel=1, duration=3.0, port='/dev/ttyUSB0'):
    steps = 255
    delay = duration / steps
    for value in range(256):
        send_dmx(channel, value, port)
        time.sleep(delay)

def ramp_down(channel=1, duration=3.0, port='/dev/ttyUSB0'):
    steps = 255
    delay = duration / steps
    for value in range(256):
        send_dmx(channel, 255-value, port)
        time.sleep(delay)