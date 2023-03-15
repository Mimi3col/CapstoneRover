
import serial
import time

serialInst = serial.Serial("COM6", 9600)



msg = 0b10100000


msg = msg.to_bytes(1, "big")
time.sleep(3)


serialInst.write(msg)

serialInst.close()
