from flask import Flask, make_response, jsonify, json, request
from db import carros

## instanciar o flask
app = Flask('mongoDB-flask-api') #mas poderia usar __name__ porque ele assume o nome do módulo atual
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET']) #decorator do flask pra identificar uma rota pro flask
def get_carros():
    return carros

#da pra fazer de outra forma usando make responde:
@app.route('/carros_alternativa', methods=['GET'])
def get_carros_usando_make_response():
    return make_response(
        jsonify(carros) #dessa forma eu consigo ter os dados retornados de forma mais bonita
    )
# nesse momento retornou exatamente a mesma coisa, mas acredito que em versões mais antigas do flask isso
# fazia alguma diferença, ou talvez dados que venham diretamente do banco de dados

@app.route('/create_carro', methods=['POST'])
def create_carro():
    carro = request.json #aqui a gente consegue pegar o corpo da requisição e qualquer informação dentro dela, nesse caro, pegamos todas as informações
    carros.append(carro)
    return jsonify(
        mensagem = "Carro criado com sucesso",
        dados = carro
    )

app.run() #pra iniciar a api/rodar a instancia do flask
