import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm.start(0)

servo_angle = 90

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.1)
    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)

def fwd():
    print("Forward")

def left():
    print("Left")
    global servo_angle
    servo_angle += 10
    SetAngle(servo_angle)
    print(servo_angle)
def back():
    print("Backward")

def right():
    print("Right")
    global servo_angle
    servo_angle -= 10
    SetAngle(servo_angle)
    print(servo_angle)
