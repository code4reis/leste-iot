from flask import Flask, request, jsonify, render_template, Blueprint
import json
app = Blueprint('historico',__name__)

@app.route('/historico')
def historico():
    with open('speedteste_results.json', 'r') as f:
        json_data = json.load(f)
    return render_template('historico.html', items=json_data)
