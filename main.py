import requests
from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#las siguientes rutas corresponden a la pokeapi

@app.route('/all', methods = ['GET'])
def allPokemonGET():
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

@app.route('/pokedex', methods = ['POST'])
def pokedex():
    """Generar respuesta JSON mediante envio de solicitud mediante postman por el body"""
    if request.method == 'POST':
        name = request.json['name']
        name_url = f"https://pokeapi.co/api/v2/pokedex/{name}"
        result = requests.get(name_url)
        resultJson  = result.json()
        return jsonify(resultJson)

@app.route('/pokedex/<string:name>', methods = ['GET'])
def pokedexGET(name):
    """Generar respuesta JSON mediante envio de parametros"""
    if request.method == 'GET':
        name_url = f"https://pokeapi.co/api/v2/pokedex/{name}"
        result = requests.get(name_url)
        resultJson  = result.json()
        return jsonify(resultJson)

@app.route('/pokemon', methods = ['POST'])
def pokemonName():
    """Generar respuesta JSON mediante envio de solicitud mediante postman por el body"""
    if request.method == 'POST':
        name = request.json['name']
        name_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        result = requests.get(name_url)
        resultJson  = result.json()
        return jsonify({
        "id":resultJson['id'],
        "name":resultJson['name'],
        "types":resultJson['types'],
        "stats":resultJson['stats'], 
        "game_indices":resultJson['game_indices']})

@app.route('/pokemon/<string:name>', methods = ['GET'])
def pokemonNameGET(name):
    """Para buscar un pokemon en especifico"""
    name_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    result = requests.get(name_url)
    resultJson = result.json()
    return jsonify({
        "id":resultJson['id'],
        "name":resultJson['name'],
        "types":resultJson['types'],
        "stats":resultJson['stats'], 
        "game_indices":resultJson['game_indices']
    })

@app.route('/type', methods = ['POST'])
def pokemonType():
    """Para buscar un typo pokemon en especifico"""
    if request.method == 'POST':
        type = request.json['type']
        name_url = f"https://pokeapi.co/api/v2/type/{type}"
        result = requests.get(name_url)
        resultJson  = result.json()
        return jsonify({
        "id":resultJson['id'],
        "name":resultJson['name'],
        "game_indices":resultJson['game_indices']
    })

@app.route('/type/<string:nametype>', methods = ['GET'])
def pokemonTypeGET(nametype):
    """Para buscar un pokemon en especifico"""
    name_url = f"https://pokeapi.co/api/v2/pokemon/{nametype}"
    result = requests.get(name_url)
    resultJson = result.json()
    return jsonify({
        "id":resultJson['id'],
        "name":resultJson['name'],
        "types":resultJson['types'],
        "stats":resultJson['stats'], 
        "game_indices":resultJson['game_indices']
    })

def handle_error_404(error):
    return "<h1>No existe...</h1>"
    
if __name__ == '__main__':
    app.run(debug= True)
    app.register_error_handler(404, handle_error_404)
    
