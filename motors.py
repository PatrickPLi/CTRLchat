import RPi.GPIO as GPIO
from time import sleep

left1 = 24
left2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(left1,GPIO.OUT)
GPIO.setup(left2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(left1,GPIO.LOW)
GPIO.output(left2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)

throttle = 0
steering = 50
left_motor = 0
right_motor = 0

def SetMotors(throttle, steering):

    #Don't have motors yet, so just using integers to represent speed of each motor. Will replace with GPIO later.
    global left_motor
    global right_motor
    left_motor = throttle
    right_motor = throttle
    GPIO.output(left1,GPIO.HIGH)
    GPIO.output(left2,GPIO.LOW)
    if steering < 50:
        left_offset = steering/50
        left_motor = left_motor*left_offset
    if steering > 50:
        right_offset = (100-steering)/50
        right_motor = right_motor*right_offset

    print("Left: {}    |    Right: {}".format(int(left_motor), int(right_motor)))
    p.ChangeDutyCycle(int(left_motor));



def set_throttle(val):
    global throttle
    global steering
    throttle = int(val)
    SetMotors(throttle, steering)

def set_steering(val):
    global throttle
    global steering
    steering = int(val)
    SetMotors(throttle, steering)
