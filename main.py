from config import *
from flask import Flask
from flask_cors import CORS

# Instancia Flask
app = Flask(__name__)

# CORS, para permitir requisições de mesma origem http
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
    ssl_context = None
    if SSL_CERTIFICATE:
        ssl_context=(CRT_PATH, KEY_PATH)

    app.run(
        host=APLICATION_IP,
        port=int(APLICATION_PORT),
        ssl_context=ssl_context,
        debug=DEBUG_MODE
    )