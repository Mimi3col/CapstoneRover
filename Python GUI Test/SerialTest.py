
import serial
import time

serialInst = serial.Serial("COM6", 9600)


# serialInst = serial.Serial("/dev/cu.usbmodem1101", 9600)


#msg = 0b01101110
#print(msg)


#msg = input("...")

msg = 0b01101110


msg = msg.to_bytes(1, "big")
time.sleep(3)


serialInst.write(msg)



'''
msg = 'n'
serialInst.write(bytes(msg, "utf-8"))
'''


'''
while(True):
  #msg = input("Cont..")
  serialInst.write(msg)

  if(msg == "e"):
    break
'''

serialInst.close()

'''
TOP/Bottom
  xxxxxxxx
& 10000000
'''

'''
Right/Left
  xxxxxxxx
& 01000000
'''

'''

e



if(TB) { #TOP
  if(RL) {
      # Control TR

  } else {
      # Control TL

  }
} else { #BOTTOM
  if(RL) {
      # Control BR


  } else { 
      # Control BL

  }
}



'''




