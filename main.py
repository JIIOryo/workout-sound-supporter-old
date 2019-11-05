# coding: utf-8
import RPi.GPIO as GPIO
import time
from consts import *
import sound 
import json
import subprocess
import sys
import os

# python main.py {menu path}

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOUND_PIN, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setwarnings(False)
    subprocess.Popen('clear')
    time.sleep(1)


def json_loader(file_path):
    f = open(file_path)
    data = json.load(f)
    f.close()
    return data


def work_out_start(file_path):
    work_out = json_loader(file_path)

    trainings = work_out['menu']
    for training in trainings:

        length = training['length']
        times = training['times']
        sets = training['sets']
        after_interval = training['after_interval']

        print('workout start!')

        sound.count_down()
        for _ in range(sets):
            sound.counter(times, length)

        time.sleep(after_interval)

    sound.power_up()

    

if __name__ == '__main__':

    init()
    # work out start
    work_out_start(sys.argv[1])
    # work out end
    print('workout finish!')
    GPIO.cleanup()
