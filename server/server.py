#coding:utf-8
from flask import Flask, render_template, redirect, Response, abort, request
import os

from lib.file_services import * 

app = Flask(__name__)

@app.route('/')
def index():
    menus = get_menus()
    return render_template('index.html', menus = menus)


@app.route('/start/<string:id>')
def start(id):
    pid = os.environ.get('WORK_OUT_SOUNDER_PID')
    if pid != '0':
        return redirect('/')
    menus = get_menus()
    for menu in menus:
        if menu['id'] == id:
            cmd = 'python /home/pi/workout-sound-supporter-old/main.py /home/pi/workout-sound-supporter-old/menus/{}.json'.format(id)
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


@app.route('/edit/<string:id>')
def edit(id):
    menu = get_workout_by_id(id)
    if not menu:
        return redirect('/')
    return render_template('edit.html', menu = menu)


@app.route('/new')
def new():
    return render_template('new.html')


@app.route('/work_out/<string:id>')
def get_work_out(id):
    menu = get_workout_by_id(id)
    if not menu:
        abort(404)
    return_data = json.dumps(menu, ensure_ascii=False, indent = 6)
    return Response(return_data, mimetype='application/json')


@app.route('/work_out/<string:id>', methods=['POST'])
def update_work_out(id):
    update_workout_by_id(id, request.json)
    return Response(response=None, status=204)

@app.route('/work_out/new', methods=['POST'])
def new_work_out():
    create_workout(request.json)
    return redirect('/')

if __name__ == '__main__':
    os.environ['WORK_OUT_SOUNDER_PID'] = '0'
    app.run(host = '0.0.0.0', port = 8000, debug = True)
