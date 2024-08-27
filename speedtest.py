from flask import Flask, request, jsonify, render_template, Blueprint
import requests
import time

app = Blueprint('speedtest', __name__)

@app.route('/speedtest')
def speedtest():
    return render_template('speedtest.html')
