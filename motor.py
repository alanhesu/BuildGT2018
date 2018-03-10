import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)

pwm1 = 18
pwm2 = 19
dir1 = 17
dir2 = 22
GPIO.setup(pwm1,GPIO.OUT)
GPIO.setup(pwm2,GPIO.OUT)
GPIO.setup(dir1,GPIO.OUT)
GPIO.setup(dir2,GPIO.OUT)

#p1 = GPIO.PWM(pwm1,800)
#p2 = GPIO.PWM(pwm2,800)

def slap():
    lifter(1,2)
    time.sleep(.1)
    lifter(0,2)

def lifter(direction, dur):
    if direction == 1:
        GPIO.output(pwm1, GPIO.LOW)
        GPIO.output(pwm2, GPIO.HIGH)
        time.sleep(dur)
        print("running")
    elif direction == 0:
        GPIO.output(pwm2, GPIO.LOW)
        GPIO.output(pwm1, GPIO.HIGH)
        time.sleep(dur)
    GPIO.output(pwm1, GPIO.LOW)
    GPIO.output(pwm2, GPIO.LOW)

slap()

