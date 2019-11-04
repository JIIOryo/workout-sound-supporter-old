#coding:utf-8
from flask import Flask, render_template, redirect
import os

from lib.file_services import * 

app = Flask(__name__)

@app.route('/')
def index():
    menus = get_menus()
    return render_template('index.html', menus = menus)


@app.route('/start/<int:id>')
def start(id):
    pid = os.environ.get('WORK_OUT_SOUNDER_PID')
    if pid != '0':
        return redirect('/')
    menus = get_menus()
    for menu in menus:
        if menu['id'] == id:
            cmd = 'python /home/pi/workout-sound-supporter/main.py /home/pi/workout-sound-supporter/menus/{}.json'.format(id)
            proc = subprocess.Popen(cmd.split())
            os.environ['WORK_OUT_SOUNDER_PID'] = str(proc.pid)
    return render_template('work_out.html', menu = get_workout_by_id(id))


@app.route('/stop')
def stop():
    pid = os.environ.get('WORK_OUT_SOUNDER_PID')
    if pid != '0':
        subprocess.Popen(['kill', str(pid)])
        os.environ['WORK_OUT_SOUNDER_PID'] = '0'
        print('stop the work out')
    return redirect('/')

if __name__ == '__main__':
    os.environ['WORK_OUT_SOUNDER_PID'] = '0'
    app.run(host = '0.0.0.0', port = 8000, debug = True)
