import serial
import time

arduino = serial.Serial('COM7', 9600, timeout=.1)
time.sleep(3)
arduino.write(b'1') # writes '1' to the arduino