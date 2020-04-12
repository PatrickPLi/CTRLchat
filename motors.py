import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.out)
pwm=GPIO.PWM(03, 50)
pwm.start(0)

servo_angle = 90

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)

def fwd():
    print("Forward")

def left():
    print("Left")
    servo_angle -=5
    SetAngle(servo_angle)

def back():
    print("Backward")

def right():
    print("Right")
    servo_angle +=5
    SetAngle(servo_angle)
