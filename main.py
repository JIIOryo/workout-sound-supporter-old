# coding: utf-8
import RPi.GPIO as GPIO
import time
from consts import *
import sound 

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOUND_PIN, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setwarnings(False)


if __name__ == '__main__':

    init()
    sound.counter(5)
    sound.power_up()

    GPIO.cleanup()
