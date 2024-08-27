from flask import render_template, Blueprint
import os, json


app = Blueprint('consumo', __name__)


RESULTS_FILE = 'consumo.json'

# funcao para carregar os resultados do json

def load_results():
    if os.path.exists(RESULTS_FILE):
        with open (RESULTS_FILE, 'r') as file:
            try: 
                data = json.load(file)
                print('Dados carregados: ', data)
                return data
            except json.JSONDecodeError:
                print('Algum erro ocorreu')
                return [] # se o arquivo estiver corrompido ou vazio

@app.route('/consumo')
def consumo():
    items = load_results()
    print('Dados carregados para o template: ', items)
    return render_template('consumo.html', items = items)
 