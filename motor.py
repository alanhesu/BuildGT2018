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

p1 = GPIO.PWM(pwm1,800)
p2 = GPIO.PWM(pwm2,800)

def slap:
    lifter(1,2)
    time.sleep(.1)
    slapper(1,2)
    time.sleep(.1)

    lifter(0,2)
    time.sleep(.1)
    slapper(0,2)
    time.sleep(.1)

def lifter(direction, dur):
    GPIO.output(dir1, direction)
    p1.start(50)
    time.sleep(dur)
    GPIO.output(dir1, direction)
    p1.stop()

def slapper(dir, dur):
    GPIO.output(dir2, direction)
    p2.start(50)
    time.sleep(dur)
    GPIO.output(dir1, direction)
    p2.stop()