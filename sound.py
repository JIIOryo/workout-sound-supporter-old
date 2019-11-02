# coding: utf-8
import RPi.GPIO as GPIO
import time


def pi(SOUND_PIN, length, f):
    p = GPIO.PWM(SOUND_PIN, 1)
    p.start(20)
    p.ChangeFrequency(f)
    time.sleep(length)
    p.stop()
    return


def pi_1sec(SOUND_PIN, length, f):
    if length <= 0 or 1 <= length:
        print('Please input an length that is greater than 0 seconds and less than 1 second.')
        return
    pi(SOUND_PIN, length, f)
    time.sleep(1 - length)
    return


