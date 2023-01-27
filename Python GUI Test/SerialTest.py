
import serial
import time

serialInst = serial.Serial("COM3", 9600)


#msg = 0b10000001
#print(bin(65))
#print(chr(msg))



while(True):
  msg = input("Cont..")
  serialInst.write(bytes(msg, "utf-8"))
  if(msg == "e"):
    break


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




