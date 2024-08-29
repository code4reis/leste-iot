from config import *
from flask import render_template, Blueprint, jsonify
import requests
from collections import defaultdict
from datetime import datetime

app = Blueprint('consumo', __name__)

@app.route('/consumo')
def consumo():
    url = f"{APLICATION_PROTOCOL}://{CLIENT_IP}:{APLICATION_PORT}/consumo"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        data = response.json()

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

        # Renderizar o template com os valores totais
        return render_template('consumo.html', totais=totais_formatados)
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": f"Erro ao acessar {url}: {e}"}), 500
