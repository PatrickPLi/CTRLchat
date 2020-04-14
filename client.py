from solace import *
import time
import keyboard

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QColor, QPalette
from PyQt5.QtCore import pyqtSlot

throttle = 0
steering = 50

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Client")

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        widget = QWidget()

        accelerate_btn = QPushButton(widget)
        accelerate_btn.setText("Accelerate")
        # accelerate_btn.move(64, 32)
        accelerate_btn.clicked.connect(accelerate)

        decelerate_btn = QPushButton(widget)
        decelerate_btn.setText("Decelerate")
        # decelerate_btn.move(64, 64)
        decelerate_btn.clicked.connect(decelerate)


        left_btn = QPushButton(widget)
        left_btn.setText("Left")
        # left_btn.move(32, 64)
        left_btn.clicked.connect(left)

        right_btn = QPushButton(widget)
        right_btn.setText("Right")
        # right_btn.move(96, 64)
        right_btn.clicked.connect(right)

        self.throttle = QProgressBar(widget)
        self.throttle.setOrientation(0x2)
        self.throttle.setProperty("value", 0)
        self.steering = QDial(widget)
        self.steering.setMinimum(0)
        self.steering.setMaximum(100)
        self.steering.setProperty("value", 50)

        hbox.addWidget(left_btn)
        hbox.addWidget(decelerate_btn)
        hbox.addWidget(right_btn)
        vbox.addWidget(accelerate_btn)
        vbox.addLayout(hbox)
        vbox.addWidget(self.throttle)
        vbox.addWidget(self.steering)
        
        main_widget = QWidget()
        main_widget.setLayout(vbox)
        self.setCentralWidget(main_widget)

    def set_throttle(self, tval):
        self.throttle.setProperty("value", tval)

    def set_steering(self, sval):
        self.steering.setProperty("value", sval)

def accelerate():
    print("w")
    global throttle
    throttle += 10
    if throttle > 99:
        throttle = 100
    client.publish('throttle', payload=throttle)
    window.set_throttle(throttle)

def decelerate():
    print("s")
    global throttle
    throttle -= 10
    if throttle < 1:
        throttle = 0
    client.publish('throttle', payload=throttle)
    window.set_throttle(throttle)

def left():
    print("a")
    global steering
    steering -= 10
    if steering < 1:
        steering = 0
    client.publish('steering', payload=steering)
    window.set_steering(steering)


def right():
    print("d")
    global steering
    steering += 10
    if steering > 99:
        steering = 100
    client.publish('steering', payload=steering)
    window.set_steering(steering)


client = initialize()

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()