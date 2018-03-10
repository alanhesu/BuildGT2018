import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)

m11 = 18
m12 = 19
m21 = 20
m22 = 21
sw11 = 22
sw12 = 23
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.setup(sw11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sw12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#p1 = GPIO.PWM(pwm1,800)
#p2 = GPIO.PWM(pwm2,800)

def sw11_callback(channel):
    GPIO.output(m11, GPIO.RISING)

def sw12_callback(channel):
    GPIO.output(m12, GPIO.RISING)

#GPIO.add_event_detect(sw12, GPIO.RISING, callback=sw12_callback, bouncetime=100)

def slap():
    lifter(1,2)
    time.sleep(.1)
    #lifter(0,2)

def lifter(direction, dur):
    if direction == 1:
        GPIO.output(m11, GPIO.LOW)
        GPIO.output(m12, GPIO.HIGH)
        time.sleep(.1)
        while 1:
            if GPIO.input(sw12) == 1:
                break
        GPIO.output(m12, GPIO.LOW)
    elif direction == 0:
        GPIO.output(m12, GPIO.LOW)
        GPIO.output(m11, GPIO.HIGH)
        #time.sleep(dur)

print GPIO.input(sw12)
slap()

