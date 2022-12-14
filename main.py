import requests
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# las siguientes rutas corresponden a la pokeapi


@app.errorhandler(404)
def pageNotfound(e):
    return jsonify({"Error ": "la pagina no existe, ingresa una direccion valida"})

@app.errorhandler(405)
def pageNotfound(e):
    return jsonify({"Error ": "verifica el tipo de metodo"})


@app.route('/')
def homeRESTAPI():
    return """<h1>Bienvenido</h1> 
        <h2>Contamos con 4 endpoins funcionales y uno de ayuda para tus peticiones</h2>
        <h3>/all - GET </h3>
        <h3>/pokedex - POST y GET </h3>
        <h3>/pokemon - POST y GET </h3>
        <h3>/type - POST y GET </h3>
        <h3>/restdoc</h3>
        <p> Recuerda utilizar un restclient para las peticiones POST </p>
"""


@app.route('/restdoc')
def docRESTAPI():
    return redirect("https://documenter.getpostman.com/view/18771793/VUjSENtP")


@app.route('/all', methods=['GET'])
def allPokemonGET():
    """Retorna todos los pokemon"""
    data = []
    name_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    while True:
        resp = requests.get(name_url)
        json = resp.json()
        data.extend(json.get('results', []))
        name_url = json.get('next')
        if not name_url:
            break
    return jsonify(data)


@app.route('/pokedex', methods=['POST'])
def pokedex():
    """Generar respuesta JSON mediante envio de solicitud mediante postman por el body"""
    if request.method == 'POST':
        name = request.json['name']
        name_url = f"https://pokeapi.co/api/v2/pokedex/{name}"
        result = requests.get(name_url)
        resultJson = result.json()
        return jsonify(resultJson)


@app.route('/pokedex/<string:name>', methods=['GET'])
def pokedexGET(name):
    """Generar respuesta JSON mediante envio de parametros"""
    if request.method == 'GET':
        name_url = f"https://pokeapi.co/api/v2/pokedex/{name}"
        result = requests.get(name_url)
        resultJson = result.json()
        return jsonify(resultJson)


@app.route('/pokemon', methods=['POST'])
def pokemonName():
    """Generar respuesta JSON mediante envio de solicitud mediante postman por el body"""
    if request.method == 'POST':
        name = request.json['name']
        name_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        result = requests.get(name_url)
        resultJson = result.json()
        return jsonify({
            "id": resultJson['id'],
            "name": resultJson['name'],
            "types": resultJson['types'],
            "stats": resultJson['stats'],
            "game_indices": resultJson['game_indices']})


@app.route('/pokemon/<string:name>', methods=['GET'])
def pokemonNameGET(name):
    """Para buscar un pokemon en especifico"""
    name_url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    result = requests.get(name_url)
    resultJson = result.json()
    return jsonify({
        "id": resultJson['id'],
        "name": resultJson['name'],
        "types": resultJson['types'],
        "stats": resultJson['stats'],
        "game_indices": resultJson['game_indices']
    })


@app.route('/type', methods=['POST'])
def pokemonType():
    """Para buscar un typo pokemon en especifico"""
    if request.method == 'POST':
        type = request.json['type']
        name_url = f"https://pokeapi.co/api/v2/type/{type}"
        result = requests.get(name_url)
        resultJson = result.json()
        return jsonify({
            "id": resultJson['id'],
            "name": resultJson['name'],
            "game_indices": resultJson['game_indices']
        })


@app.route('/type/<string:nametype>', methods=['GET'])
def pokemonTypeGET(nametype):
    """Para buscar un pokemon en especifico"""
    name_url = f"https://pokeapi.co/api/v2/type/{nametype}"
    result = requests.get(name_url)
    resultJson = result.json()
    return jsonify({
        "id": resultJson['id'],
        "name": resultJson['name'],
        "game_indices": resultJson['game_indices']
    })


if __name__ == '__main__':
    app.run(debug=True)
