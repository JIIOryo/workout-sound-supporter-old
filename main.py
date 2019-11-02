# coding: utf-8
import RPi.GPIO as GPIO
import time
import sound 

length = 0.05
f = 1500
SOUND_PIN = 21

def counter(n):
    for _ in range(n):
        sound.pi_1sec(SOUND_PIN, length, f)
    return 

if __name__ == '__main__':
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(SOUND_PIN, GPIO.OUT, initial = GPIO.LOW)
  GPIO.setwarnings(False)
  
  counter(10)
  
  GPIO.cleanup()
