from flask import render_template, Blueprint

app = Blueprint('home',__name__)

@app.route('/')
def home():
    return render_template('home.html')