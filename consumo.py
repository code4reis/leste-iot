from flask import render_template, Blueprint, jsonify
import requests, os, json
from collections import defaultdict
from datetime import datetime
from flask_cors import CORS

app = Blueprint('consumo', __name__)

@app.route('/consumo')
def consumo():
    url = "http://192.168.128.57:5000/consumo"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        data = response.json()

        # Calcular as somas de download e upload


        #dicionario para armazenar os totais por data
        totais_por_data = defaultdict(lambda: {"Download (MB)": 0, "Upload (MB)": 0,})

        for item in data:
            data_hora = item.get("Hora")
            data_formatada = datetime.strptime(data_hora, '%d-%m-%Y %H:%M:%S').strftime('%d/%m/%Y')

            totais_por_data[data_formatada]["Download (MB)"] += item.get("Download (MB)", 0)
            totais_por_data[data_formatada]["Upload (MB)"] += item.get("Upload (MB)", 0)


        totais_formatados = sorted(
            [{"Data": data, "Total Download (MB)": total["Download (MB)"], "Total Upload (MB)": total["Upload (MB)"]}
             for data, total in totais_por_data.items()],
            key=lambda x: datetime.strptime(x["Data"], '%d/%m/%Y'),
            reverse=True
        )
            

        # total_download = sum(item.get("Download (MB)", 0) for item in data)
        # total_upload = sum(item.get("Upload (MB)", 0) for item in data)

        # print(total_download)
        # print(total_upload)
    

        # Renderizar o template com os valores totais
        return render_template('consumo.html', totais=totais_formatados)
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": f"Erro ao acessar {url}: {e}"}), 500


# RESULTS_FILE = 'consumo.json'

# # funcao para carregar os resultados do json

# def load_results():
#     if os.path.exists(RESULTS_FILE):
#         with open (RESULTS_FILE, 'r') as file:
#             try: 
#                 data = json.load(file)
#                 return data
#             except json.JSONDecodeError:
#                 print('Algum erro ocorreu')
#                 return [] # se o arquivo estiver corrompido ou vazio
        

# @app.route('/consumo')
# def consumo():
#     items = load_results()
#     print('Dados carregados para o template: ', items)
#     return render_template('consumo.html', items = items)
    