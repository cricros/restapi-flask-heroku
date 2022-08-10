import requests, json
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/all', methods = ['GET'])
def home():
    """Retorna todos los pokemon"""
    data = []
    name_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    while True:
        resp = requests.get(name_url)
        json = resp.json()
        data.extend(json.get('results', []))
        name_url = json.get('next')
        if not name_url: break
    return jsonify(data)

@app.route('/pokemon/<string:name>', methods = ['GET'])
def pokemonName(name):
    """Para buscar un pokemon en especifico"""
    name_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    result = requests.get(name_url)
    resultJson = result.json()
    return jsonify(resultJson)



if __name__ == '__main__':
    app.run(debug= True)
