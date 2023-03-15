
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QFrame, QGroupBox, QLabel
import serial
import time
import atexit
import json



class QMotorInput(QGroupBox):

    _motAddr = None

    _QLineEditMotor = None
    _QButtonMotor = None

    

    trans = {
            "Motor Bottom Left"  : "BL",
            "Motor Bottom Right" : "BR",
            "Motor Top Left" : "TL",
            "Motor Top Right" : "TR"
        }
    _widgetName = None;

    def __init__(self, motAddr, startVal=0, widgetName="Motor"):

        super().__init__(widgetName)

        self._widgetName = self.trans[widgetName]

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

        json_object = QMotorSet.get_json_object()

        val = int(self.get_QLineEditMotor_text())
        if(not(val >= 0 and val <= 63)):
            self._QLineEditMotor.setText(str(json_object[self._widgetName]))
        val = int(self.get_QLineEditMotor_text())


        msg = int((self._motAddr << 6) + val)
        print("This is the sent message", msg)

        msg = msg.to_bytes(1, "big")
        serialInst.write(msg)


    def get_QLineEditMotor_text(self):
        return self._QLineEditMotor.text()

    def set_QLineEditMotor_text(self, msg):
        return self._QLineEditMotor.setText(msg)




class QSettings(QGroupBox):

    _json_object = None

    _QLineEditBL = None  
    _QLineEditBR = None 
    _QLineEditTL = None 
    _QLineEditTR = None 

    def __init__(self):

        super().__init__("Settings")


        self.setFixedSize(300, 300)

        layoutMI = QGridLayout()

        QInstructSet = QLabel("This allows us to configure the stop throttle value in volts")

        QLabelBL = QLabel("BL")
        QLabelBR = QLabel("BR")
        QLabelTL = QLabel("TL")
        QLabelTR = QLabel("TR")


        QInstructSet.setFixedSize(150, 150)
        QInstructSet.setWordWrap(True)

        QLabelBL.setFixedSize(20, 20)
        QLabelBR.setFixedSize(20, 20)
        QLabelTL.setFixedSize(20, 20)
        QLabelTR.setFixedSize(20, 20)

        QLabelBL.setContentsMargins(10, 10, 10, 10)
        QLabelBR.setContentsMargins(10, 10, 10, 10)
        QLabelTL.setContentsMargins(10, 10, 10, 10)
        QLabelTR.setContentsMargins(10, 10, 10, 10)


        self._json_object = self.readFromFile()


        self._QLineEditBL = QLineEdit(str(self._json_object["BL"]))
        self._QLineEditBR = QLineEdit(str(self._json_object["BR"]))
        self._QLineEditTL = QLineEdit(str(self._json_object["TL"]))
        self._QLineEditTR = QLineEdit(str(self._json_object["TR"]))

        self._QLineEditBL.setFixedSize(50, 20)
        self._QLineEditBL.setStyleSheet("background-color: white;")

        self._QLineEditBR.setFixedSize(50, 20)
        self._QLineEditBR.setStyleSheet("background-color: white;")

        self._QLineEditTL.setFixedSize(50, 20)
        self._QLineEditTL.setStyleSheet("background-color: white;")
        
        self._QLineEditTR.setFixedSize(50, 20)
        self._QLineEditTR.setStyleSheet("background-color: white;")


        QButtonApply = QPushButton("Apply")
        QButtonApply.setFixedSize(50, 20)
        QButtonApply.setStyleSheet("background-color: white;")
        QButtonApply.clicked.connect(self.QButtonApply_func)
       

        layoutMI.addWidget(QInstructSet, 0, 0)

        layoutMI.addWidget(QLabelBL, 1, 0)
        layoutMI.addWidget(QLabelBR, 2, 0)
        layoutMI.addWidget(QLabelTL, 3, 0)
        layoutMI.addWidget(QLabelTR, 4, 0)

        layoutMI.addWidget(self._QLineEditBL, 1, 1)
        layoutMI.addWidget(self._QLineEditBR, 2, 1)
        layoutMI.addWidget(self._QLineEditTL, 3, 1)
        layoutMI.addWidget(self._QLineEditTR, 4, 1)

        layoutMI.addWidget(QButtonApply, 5, 2)

        self.setStyleSheet("background-color: grey;")

        self.setLayout(layoutMI)

    def QButtonApply_func(self):

        print("Apply", type(self._json_object))

        self.writeToFile(float(self._QLineEditBL.text()), 
                         float(self._QLineEditBR.text()), 
                         float(self._QLineEditTL.text()), 
                         float(self._QLineEditTR.text()))


    def writeToFile(self, BL=2.1, BR=2.1, TL=2.1, TR=2.1):
        
        dictionary = {
                'BL': BL,
                'BR': BR,
                'TL': TL,
                'TR': TR
            }

        with open("config.json", "w") as outfile:
            json.dump(dictionary, outfile)
        
        self._json_object = self.readFromFile()


    def readFromFile(self):
        try:
            with open('config.json', 'r') as openfile:
                self._json_object = json.load(openfile)
        except:
            self.writeToFile()

        return self._json_object


    def get_json_object(self):
        return self._json_object
    


    
def QButtonStop_func():

    json_object = QMotorSet.get_json_object()

    print("Stop BUtton")
    print(json_object)

    QMotorInputTL.set_QLineEditMotor_text(str(json_object["TL"]))
    QMotorInputTR.set_QLineEditMotor_text(str(json_object["TR"]))
    QMotorInputBL.set_QLineEditMotor_text(str(json_object["BL"]))
    QMotorInputBR.set_QLineEditMotor_text(str(json_object["BR"]))

    # Could just call send all
    QMotorInputTL.QButtonMotor_func()
    QMotorInputTR.QButtonMotor_func()
    QMotorInputBL.QButtonMotor_func()
    QMotorInputBR.QButtonMotor_func()

def QSendAll_func():
    QMotorInputTL.QButtonMotor_func()
    QMotorInputTR.QButtonMotor_func()
    QMotorInputBL.QButtonMotor_func()
    QMotorInputBR.QButtonMotor_func()

def QStart_func():



    QMotorInputTL.set_QLineEditMotor_text(str(0))
    QMotorInputTR.set_QLineEditMotor_text(str(0))
    QMotorInputBL.set_QLineEditMotor_text(str(32))
    QMotorInputBR.set_QLineEditMotor_text(str(32))

    QSendAll_func()

    time.sleep(2)

    QMotorInputTL.set_QLineEditMotor_text(str(0))
    QMotorInputTR.set_QLineEditMotor_text(str(0))
    QMotorInputBL.set_QLineEditMotor_text(str(44)) #20
    QMotorInputBR.set_QLineEditMotor_text(str(46)) #18

    QSendAll_func()

    time.sleep(4)

    QMotorInputTL.set_QLineEditMotor_text(str(0))
    QMotorInputTR.set_QLineEditMotor_text(str(0))
    QMotorInputBL.set_QLineEditMotor_text(str(39)) #30
    QMotorInputBR.set_QLineEditMotor_text(str(41)) #28

    QSendAll_func()



# Connect to Serial Port (May want to incorporate some UI stuff for this)
# Also will need to change Com port between connections 
serialInst = serial.Serial("COM3", 9600)


# Give the serial Com 3 seconds time to connect
time.sleep(3)






app = QApplication([])
window = QWidget()

#window.setFixedSize(800, 500)

layout = QGridLayout()



QMotorSet = QSettings()


QButtonStop = QPushButton('STOP!')
QButtonStop.setFixedSize(100, 100)
QButtonStop.setStyleSheet("background-color: red;")
QButtonStop.clicked.connect(QButtonStop_func)



QInstruction = QLabel("The value should range from 0 to 63. Look at the README or code comments to know more.")
QInstruction.setFixedSize(100, 100)
QInstruction.setWordWrap(True)


QMotorInputBL = QMotorInput(0, widgetName="Motor Bottom Left")
QMotorInputBR = QMotorInput(1, widgetName="Motor Bottom Right")
QMotorInputTL = QMotorInput(2, widgetName="Motor Top Left")
QMotorInputTR = QMotorInput(3, widgetName="Motor Top Right")

QMotorSendAll = QPushButton('Send All')
QMotorSendAll.setFixedSize(150, 100)
QMotorSendAll.setStyleSheet("background-color: blue;")
QMotorSendAll.clicked.connect(QSendAll_func)


QMotorStart = QPushButton('Start Off')
QMotorStart.setFixedSize(150, 100)
QMotorStart.setStyleSheet("background-color: green;")
QMotorStart.clicked.connect(QStart_func)



layout.addWidget(QMotorSet, 0, 3, 3, 1)

layout.addWidget(QButtonStop, 0, 1)
layout.addWidget(QInstruction, 1, 1)

layout.addWidget(QMotorSendAll, 3, 1)

layout.addWidget(QMotorInputTL, 2, 0)
layout.addWidget(QMotorInputTR, 2, 2)

layout.addWidget(QMotorInputBL, 4, 0)
layout.addWidget(QMotorInputBR, 4, 2)

layout.addWidget(QMotorStart, 2, 1)


window.setLayout(layout)
window.show()


# Close application and serial com
app.exec()
atexit.register(lambda: serialInst.close())

