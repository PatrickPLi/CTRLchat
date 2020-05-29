from solace import *
import time
import keyboard

import sys
from PyQt5.QtWidgets import QWidget, QShortcut, QStackedLayout, QLabel, QApplication, QHBoxLayout, QDial, QVBoxLayout, QHBoxLayout, QSlider, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon, QColor, QPalette, QKeySequence, QPixmap, QTransform
from PyQt5 import QtCore

throttle_val = 0
steering_val = 50

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
        hbox2 = QHBoxLayout()

        wheel_stack = QStackedLayout()

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

        self.throttle = QSlider(widget)
        self.throttle.setOrientation(0x2)
        self.throttle.setProperty("value", 0)

        ss = "::handle {image: url(pedal.svg)}"
        self.throttle.setStyleSheet(ss)
        self.steering = QDial(widget)
        self.steering.setMinimum(0)
        self.steering.setMaximum(100)
        self.steering.setProperty("value", 50)
        self.steering.valueChanged.connect(change_steering)
        self.throttle.valueChanged.connect(change_throttle)

        self.steering_wheel = QPixmap('steering-wheel.svg')
        self.wheel_label = QLabel(self)
        self.wheel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wheel_label.setMinimumSize(400,400)
        self.wheel_label.setPixmap(self.steering_wheel)

        self.accel_shortcut = QShortcut(QKeySequence("w"), self)
        self.accel_shortcut.activated.connect(accelerate)

        self.decel_shortcut = QShortcut(QKeySequence("s"), self)
        self.decel_shortcut.activated.connect(decelerate)

        self.left_shortcut = QShortcut(QKeySequence("a"), self)
        self.left_shortcut.activated.connect(left)

        self.right_shortcut = QShortcut(QKeySequence("d"), self)
        self.right_shortcut.activated.connect(right)


        hbox.addWidget(left_btn)
        hbox.addWidget(decelerate_btn)
        hbox.addWidget(right_btn)
        vbox.addWidget(accelerate_btn)
        vbox.addLayout(hbox)
        hbox2.addWidget(self.throttle)
        wheel_stack.addWidget(self.wheel_label)
        wheel_stack.addWidget(self.steering)
        hbox2.addLayout(wheel_stack)
        vbox.addLayout(hbox2)
        
        main_widget = QWidget()
        main_widget.setLayout(vbox)
        self.setCentralWidget(main_widget)

    def set_throttle(self, tval):
        self.throttle.setProperty("value", tval)

    def set_steering(self, sval):
        self.steering.setProperty("value", sval)
        transform = QTransform()
        transform.rotate(sval*2-100)
        steering_wheel = QPixmap('steering-wheel.svg')
        self.steering_wheel = steering_wheel.transformed(transform)
        self.wheel_label.setPixmap(self.steering_wheel)

def change_steering():
    global steering_val
    steering_val = window.steering.value()
    client.publish('steering', payload=steering_val)

def change_throttle():
    global throttle_val
    throttle_val = window.throttle.value()
    client.publish('throttle', payload=throttle_val)

def accelerate():
    print("w")
    global throttle_val
    throttle_val += 100
    if throttle_val > 99:
        throttle_val = 100
    window.set_throttle(throttle_val)

def decelerate():
    print("s")
    global throttle_val
    throttle_val -= 100
    if throttle_val < 1:
        throttle_val = 0
    window.set_throttle(throttle_val)

def left():
    print("a")
    global steering_val
    steering_val = 0
    if steering_val < 1:
        steering_val = 0
    window.set_steering(steering_val)
    time.sleep(0.5)
    steering_val = 50
    window.set_steering(steering_val)


def right():
    print("d")
    global steering_val
    steering_val = 100
    if steering_val > 99:
        steering_val = 100
    window.set_steering(steering_val)
    time.sleep(0.5)
    steering_val = 50
    window.set_steering(steering_val)


client = initialize()

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

change_steering()
change_throttle
# Start the event loop.
app.exec_()