# coding: utf-8
import RPi.GPIO as GPIO
import time
from consts import *



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


def power_up():


    FA = 698.46 * r ** pun
    MI = 622.25 * r ** pun
    SO = 783 * r ** pun


    pi(SOUND_PIN, 0.05, FA)
    time.sleep(0.07)
    pi(SOUND_PIN, 0.05, FA)
    time.sleep(0.07)
    pi(SOUND_PIN, 0.05, FA)
    time.sleep(0.07)
    pi(SOUND_PIN, 0.05, FA)
    time.sleep(0.15)
    pi(SOUND_PIN, 0.1, MI)
    time.sleep(0.15)
    pi(SOUND_PIN, 0.1, SO)
    time.sleep(0.15)
    pi(SOUND_PIN, 0.5, FA)

    return


def counter(n):
    for _ in range(n-1):
        pi_1sec(SOUND_PIN, length, f)
    pi_1sec(SOUND_PIN, 6 * length,  r ** 5 * f)
    return 
