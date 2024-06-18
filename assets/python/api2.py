from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Datos de ejemplo (simulando una base de datos)
juegos = [
    { "id": 1, "titulo": "The Legend of Zelda: Breath of the Wild", "plataforma": "Nintendo Switch", "anio_lanzamiento": 2017 },
    { "id": 2, "titulo": "Red Dead Redemption 2", "plataforma": "PlayStation 4, Xbox One", "anio_lanzamiento": 2018 },
    { "id": 3, "titulo": "The Witcher 3: Wild Hunt", "plataforma": "PlayStation 4, Xbox One, PC", "anio_lanzamiento": 2015 },
    { "id": 4, "titulo": "Super Mario Odyssey", "plataforma": "Nintendo Switch", "anio_lanzamiento": 2017 }
]
next_id = 5

# Ruta para obtener todos los juegos
@app.route('/api/juegos', methods=['GET'])
def get_juegos():
    return jsonify(juegos)

# Ruta para obtener un juego por su ID
@app.route('/api/juegos/<int:juego_id>', methods=['GET'])
def get_juego(juego_id):
    juego = next((juego for juego in juegos if juego['id'] == juego_id), None)
    if juego:
        return jsonify(juego)
    else:
        abort(404, f"No se encontró un juego con ID {juego_id}")

# Ruta para crear un nuevo juego
@app.route('/api/juegos', methods=['POST'])
def crear_juego():
    global next_id
    nuevo_juego = {
        "id": next_id,
        "titulo": request.json.get('titulo', ''),
        "plataforma": request.json.get('plataforma', ''),
        "anio_lanzamiento": request.json.get('anio_lanzamiento', 0)
    }
    juegos.append(nuevo_juego)
    next_id += 1
    return jsonify(nuevo_juego), 201

# Ruta para actualizar un juego por su ID
@app.route('/api/juegos/<int:juego_id>', methods=['PUT'])
def actualizar_juego(juego_id):
    juego = next((juego for juego in juegos if juego['id'] == juego_id), None)
    if not juego:
        abort(404, f"No se encontró un juego con ID {juego_id}")

    juego['titulo'] = request.json.get('titulo', juego['titulo'])
    juego['plataforma'] = request.json.get('plataforma', juego['plataforma'])
    juego['anio_lanzamiento'] = request.json.get('anio_lanzamiento', juego['anio_lanzamiento'])
    return jsonify(juego)

# Ruta para eliminar un juego por su ID
@app.route('/api/juegos/<int:juego_id>', methods=['DELETE'])
def eliminar_juego(juego_id):
    global juegos
    juegos = [juego for juego in juegos if juego['id'] != juego_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
