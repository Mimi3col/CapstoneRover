
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QFrame, QGroupBox, QLabel
import serial
import time
import atexit



class QMotorInput(QGroupBox):

    _motAddr = None

    _QLineEditMotor = None
    _QButtonMotor = None

    def __init__(self, motAddr, startVal=0, widgetName="Motor"):

        super().__init__(widgetName)

        self._motAddr = motAddr

        self.setFixedSize(150, 100)

        layoutMI = QGridLayout()

        self._QLineEditMotor = QLineEdit()
        self._QLineEditMotor.setText(str(startVal))
        self._QLineEditMotor.setFixedSize(50, 20)
        self._QLineEditMotor.setStyleSheet("background-color: white;")

        self._QButtonMotor = QPushButton('Send')
        self._QButtonMotor.setFixedSize(50, 50)
        self._QButtonMotor.setStyleSheet("background-color: white;")
        self._QButtonMotor.clicked.connect(self.QButtonMotor_func)

        layoutMI.addWidget(self._QLineEditMotor, 0, 0)
        layoutMI.addWidget(self._QButtonMotor, 0, 1)

        self.setStyleSheet("background-color: grey;")

        self.setLayout(layoutMI)

    def QButtonMotor_func(self):

        val = int(self.get_QLineEditMotor_text())
        if(not(val >= 0 and val <= 63)):
            self._QLineEditMotor.setText(str(32))

        msg = (self._motAddr << 6) + int(self.get_QLineEditMotor_text())
        print(msg)

        msg = msg.to_bytes(1, "big")
        serialInst.write(msg)


    def get_QLineEditMotor_text(self):
        return self._QLineEditMotor.text()

    def set_QLineEditMotor_text(self, msg):
        return self._QLineEditMotor.setText(msg)
    

def QButtonStop_func():
    QMotorInputTL.set_QLineEditMotor_text(str(32))
    QMotorInputTR.set_QLineEditMotor_text(str(32))
    QMotorInputBL.set_QLineEditMotor_text(str(32))
    QMotorInputBR.set_QLineEditMotor_text(str(32))

    QMotorInputTL.QButtonMotor_func()
    QMotorInputTR.QButtonMotor_func()
    QMotorInputBL.QButtonMotor_func()
    QMotorInputBR.QButtonMotor_func()



# Connect to Serial Port (May want to incorporate some UI stuff for this)
# Also will need to change Com port between connections 
serialInst = serial.Serial("COM6", 9600)


# Give the serial Com 3 seconds time to connect
time.sleep(3)



app = QApplication([])
window = QWidget()

window.setFixedSize(500, 500)

layout = QGridLayout()

QButtonStop = QPushButton('STOP!')
QButtonStop.setFixedSize(100, 100)
QButtonStop.setStyleSheet("background-color: red;")
QButtonStop.clicked.connect(QButtonStop_func)


QInstruction = QLabel("The value should range from 0 to 63. Look at the README or code comments to know more.")
QInstruction.setFixedSize(100, 100)
QInstruction.setWordWrap(True)

QMotorInputTL = QMotorInput(0, widgetName="Motor Top Left")
QMotorInputTR = QMotorInput(1, widgetName="Motor Top Right")
QMotorInputBL = QMotorInput(2, widgetName="Motor Bottom Left")
QMotorInputBR = QMotorInput(3, widgetName="Motor Bottom Right")




layout.addWidget(QButtonStop, 0, 1)
layout.addWidget(QInstruction, 1, 1)


layout.addWidget(QMotorInputTL, 2, 0)
layout.addWidget(QMotorInputTR, 2, 2)

layout.addWidget(QMotorInputBL, 3, 0)
layout.addWidget(QMotorInputBR, 3, 2)


window.setLayout(layout)
window.show()


# Close application and serial com
app.exec()
atexit.register(lambda: serialInst.close())

