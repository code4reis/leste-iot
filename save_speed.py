from flask import Flask, request, jsonify, render_template, Blueprint
import json
import os
from datetime import datetime
import requests


app = Blueprint('save_speed', __name__)

#Caminho para salvar os reslutados do arquivo JSON
RESULTS_FILE = 'speedteste_results.json'

#Função para carregar os reslutados do arquivo JSON 
def load_results():
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r') as file:
            return json.load(file)
    return []

#Função para salvar os resuitados no arquivo json 

def save_results(results):
    with open(RESULTS_FILE, 'w') as file:
        json.dump(results, file, indent=4)


#Rota para salvar os resultados no arquivo json 

@app.route('/save_speedteste', methods=['POST'])
def save_speed_teste():
    data = request.json
    results = load_results()
    new_result = {
        'download_speed': data['download_speed_mbps'],
        'upload_speed': data['upload_speed_mbps'],
        'ping': data['ping_ms'],
        'server': data['server'],
        'timestamp': datetime.utcnow().isoformat()
    }
    results.append(new_result)
    save_results(results)
    return jsonify({"message": "Resultados salvos"}), 200
    
