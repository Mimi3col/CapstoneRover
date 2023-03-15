
import serial

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

'''

ser = serial.Serial('COM3', 9600)  # open serial port at 9600 baud rate

while True:
    if ser.in_waiting > 0:  # check if there are bytes waiting to be read
        data = ser.read()  # read a single byte from serial port
        print(data)  # print the byte to the console

'''

