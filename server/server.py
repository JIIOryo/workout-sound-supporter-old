#coding:utf-8
from flask import Flask, render_template, redirect

from lib.file_services import * 


app = Flask(__name__)

@app.route('/')
def index():
    menus = get_menus()
    return render_template('index.html', menus = menus)


@app.route('/start/<int:id>')
def start(id):
    menus = get_menus()
    for menu in menus:
        if menu['id'] == id:
            cmd = 'python /home/pi/workout-sound-supporter/main.py /home/pi/workout-sound-supporter/menus/{}.json'.format(id)
            subprocess.Popen(cmd.split())
            print(cmd)
    return redirect('/')


@app.route('/stop')
def stop():
    return redirect('/')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)
