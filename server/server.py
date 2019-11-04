#coding:utf-8
from flask import Flask, render_template

from lib.file_services import * 


app = Flask(__name__)

@app.route('/')
def index():

    menus = get_menus()
    return render_template('index.html', s = menus)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)
