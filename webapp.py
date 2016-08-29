#!/usr/bin/python  
import os

from controller import init_gpio, gate_toggle, cleanup_gpio
from flask import Flask, request, render_template


init_gpio()    
application = Flask(__name__, static_folder='static', static_url_path='/static')
application.secret_key = os.environ['SECRET']
application.config.update(
     DEBUG=True,
     PROPAGATE_EXCEPTIONS=True
)

@application.route('/')
def index():
    return render_template('index.html')


@application.route('/toggle', methods=['POST'])
def toggle():
    if request.method == 'POST':
        gate_toggle()
    return "Done"


if __name__ == '__main__':
    application.run()

