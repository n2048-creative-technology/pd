import serial
import time

def send_dmx(ch, value):
    start_code = 0x00
    dmx_data = bytearray([0] * 512)   # 512 channels
    dmx_data[ch-1] = value           # CH1 = your value

    # Message structure
    message = bytearray()
    message.append(0x7E)              # Start of message
    message.append(0x06)              # Label: Send DMX Packet

    data_length = len(dmx_data) + 1   # +1 for start code
    message.append(data_length & 0xFF)        # LSB
    message.append((data_length >> 8) & 0xFF) # MSB

    message.append(start_code)        # Start code
    message.extend(dmx_data)          # DMX channel data
    message.append(0xE7)              # End of message

    # Send via serial
    with serial.Serial('/dev/ttyUSB0', baudrate=57600) as ser:
        ser.write(message)

# Example: Blink CH1
while 1:
    send_dmx(1,127)    # On
    time.sleep(1)
    send_dmx(1,0)    # Off
    time.sleep(1)
