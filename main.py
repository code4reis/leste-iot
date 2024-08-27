from flask import Flask, Blueprint
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


# Páginas
from config import *

from home import app as home_app
app.register_blueprint(home_app)

from speedtest import app as speedtest_app
app.register_blueprint(speedtest_app)

from save_speed import app as save_speed_app
app.register_blueprint(save_speed_app)

from history import app as history_app
app.register_blueprint(history_app)

from consumo import app as consumo_app
app.register_blueprint(consumo_app)

if __name__ == '__main__':
    app.run('192.168.100.107', debug=True)