import RPi.GPIO as GPIO
from time import sleep

forward = True

left_fwd = 17
left_bwd = 27
left_spd = 22

right_fwd = 24
right_bwd = 23
right_spd = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_fwd,GPIO.OUT)
GPIO.setup(left_bwd,GPIO.OUT)
GPIO.setup(right_fwd,GPIO.OUT)
GPIO.setup(right_bwd,GPIO.OUT)
GPIO.setup(left_spd,GPIO.OUT)
GPIO.setup(right_spd,GPIO.OUT)
GPIO.output(left_fwd,GPIO.LOW)
GPIO.output(left_bwd,GPIO.LOW)
GPIO.output(right_fwd,GPIO.LOW)
GPIO.output(right_bwd,GPIO.LOW)
left_pwm=GPIO.PWM(left_spd,1000)
right_pwm=GPIO.PWM(right_spd,1000)
right_pwm.start(0)
left_pwm.start(0)

throttle = 0
steering = 50
left_motor = 0
right_motor = 0

GPIO.output(left_fwd,GPIO.LOW)
GPIO.output(left_bwd,GPIO.HIGH)
GPIO.output(right_fwd,GPIO.LOW)
GPIO.output(right_bwd,GPIO.HIGH)

forward = False

def SetMotors(throttle, steering):

    #Don't have motors yet, so just using integers to represent speed of each motor. Will replace with GPIO later.
    global left_motor
    global right_motor
    left_motor = throttle
    right_motor = throttle

    if steering < 50:
        left_offset = steering/50
        left_motor = left_motor*left_offset
    if steering > 50:
        right_offset = (100-steering)/70
        right_motor = right_motor*right_offset

    if forward == True:
        tmp = right_motor
        right_motor = left_motor
        left_motor = tmp
 
    right_motor = right_motor * 0.69

    OldMax = 100
    OldMin = 0
    NewMax = 150
    NewMin = 30
    OldRange = (OldMax - OldMin)  
    NewRange = (NewMax - NewMin)  
    # NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
    left_motor_scaled = (((int(left_motor) - OldMin) * NewRange) / OldRange) + NewMin
    right_motor_scaled = (((int(right_motor) - OldMin) * NewRange) / OldRange) + NewMin
    if int(left_motor) == 0 and int(right_motor) == 0:
       left_motor_scaled = 0
       right_motor_scaled = 0


    print("Left: {}    |    Right: {}".format(int(left_motor_scaled), int(right_motor_scaled)))
    left_pwm.ChangeDutyCycle(int(left_motor_scaled))
    right_pwm.ChangeDutyCycle(int(right_motor_scaled))



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
