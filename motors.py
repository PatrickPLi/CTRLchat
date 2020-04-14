# import RPi.GPIO as GPIO
from time import sleep

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3, GPIO.OUT)
# pwm=GPIO.PWM(3, 50)
# pwm.start(0)

throttle = 0
steering = 0
left_motor = 0
right_motor = 0

def SetMotors(throttle, steering):

    #Don't have motors yet, so just using integers to represent speed of each motor. Will replace with GPIO later.
    global left_motor
    global right_motor
    print("dosihfoishofieoiofiseoihf")
    print(type(steering))
    left_motor = throttle
    right_motor = throttle
    if steering < 50:
        left_offset = steering/50
        left_motor = left_motor*left_offset
    if steering > 50:
        right_offset = (100-steering)/50
        right_motor = right_motor*right_offset

    print("Left: {}    |    Right: {}".format(int(left_motor), int(right_motor)))

# def SetAngle(angle):
#     duty = angle / 18 + 2
#     GPIO.output(3, True)
#     pwm.ChangeDutyCycle(duty)
#     sleep(0.1)
#     GPIO.output(3, False)
#     pwm.ChangeDutyCycle(0)

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