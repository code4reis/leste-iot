from flask import render_template, Blueprint


app = Blueprint('consumo', __name__)

@app.route('/consumo')
def speedtest():
    return render_template('consumo.html')
