import serial
import time

dmx_data = bytearray([0] * 512)   # 512 channels

def send_dmx(ch=1, value=255, port='/dev/ttyUSB0'):
    start_code = 0x00
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
    with serial.Serial(port, baudrate=57600) as ser:
        ser.write(message)


def send_batch_dmx(value=255, port='/dev/ttyUSB0'):
    start_code = 0x00
    dmx_data = bytearray([value] * 512)

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
    with serial.Serial(port, baudrate=57600) as ser:
        ser.write(message)
