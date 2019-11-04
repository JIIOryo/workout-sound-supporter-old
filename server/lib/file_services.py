#coding:utf-8

import subprocess
import json

def get_all_files(path):
    cmd = 'ls -1 {0}'.format( path )
    proc = subprocess.Popen( cmd.split(), stdout=subprocess.PIPE )
    return [path + '/' + line.rstrip() for line in proc.stdout]


def json_loader(file_path):
    f = open(file_path)
    data = json.load(f)
    f.close()
    return data


def get_menus():
    menus = []
    menu_paths = get_all_files('/home/pi/workout-sound-supporter/menus')
    for menu_path in menu_paths:
        menu = json_loader(menu_path)
        menus.append(menu)
    return menus
