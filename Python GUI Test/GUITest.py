
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QFrame, QGroupBox



class QMotorInput(QGroupBox):

    _value = 0.0

    def __init__(self, startVal=0.0, widgetName="Motor"):

        super().__init__(widgetName)

        _value = startVal

        self.setFixedSize(150, 100)

        layoutMI = QGridLayout()

        QLineEditMotor = QLineEdit()
        QLineEditMotor.setFixedSize(50, 20)
        QLineEditMotor.setStyleSheet("background-color: white;")

        QButtonMotor = QPushButton('Send')
        QButtonMotor.setFixedSize(50, 50)
        QButtonMotor.setStyleSheet("background-color: white;")

        layoutMI.addWidget(QLineEditMotor, 0, 0)
        layoutMI.addWidget(QButtonMotor, 0, 1)

        self.setStyleSheet("background-color: grey;")

        self.setLayout(layoutMI)



app = QApplication([])
window = QWidget()

window.setFixedSize(500, 500)

layout = QGridLayout()

QButtonStop = QPushButton('STOP!')
QButtonStop.setFixedSize(100, 100)
QButtonStop.setStyleSheet("background-color: red;")


QMotorInputTL = QMotorInput(0.0, "Motor Top Left")
QMotorInputTR = QMotorInput(0.0, "Motor Top Right")
QMotorInputBL = QMotorInput(0.0, "Motor Bottom Left")
QMotorInputBR = QMotorInput(0.0, "Motor Bottom Right")

layout.addWidget(QButtonStop, 0, 1)
layout.addWidget(QMotorInputTL, 1, 0)
layout.addWidget(QMotorInputTR, 1, 2)

layout.addWidget(QMotorInputBL, 2, 0)
layout.addWidget(QMotorInputBR, 2, 2)


window.setLayout(layout)
window.show()
app.exec()




