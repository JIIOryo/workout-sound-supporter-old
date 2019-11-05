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

def get_workout_by_id(id):
    menus = get_menus()
    for menu in menus:
        if menu['id'] == id:
            return menu
    return None



def update_workout_by_id(id, new_menu):
    f = open('/home/pi/workout-sound-supporter/menus/{}.json'.format(id), 'w')
    json.dump(new_menu , f, indent = 6)
    f.close()
    return 
