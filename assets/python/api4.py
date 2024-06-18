from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Datos de ejemplo (simulando una base de datos)
consolas = [
    { "id": 1, "nombre": "PlayStation 5", "fabricante": "Sony", "anio_lanzamiento": 2020 },
    { "id": 2, "nombre": "Xbox Series X", "fabricante": "Microsoft", "anio_lanzamiento": 2020 },
    { "id": 3, "nombre": "Nintendo Switch", "fabricante": "Nintendo", "anio_lanzamiento": 2017 }
]
next_id = 4

# Ruta para obtener todas las consolas
@app.route('/api/consolas', methods=['GET'])
def get_consolas():
    return jsonify(consolas)

# Ruta para obtener una consola por su ID
@app.route('/api/consolas/<int:consola_id>', methods=['GET'])
def get_consola(consola_id):
    consola = next((consola for consola in consolas if consola['id'] == consola_id), None)
    if consola:
        return jsonify(consola)
    else:
        abort(404, f"No se encontró una consola con ID {consola_id}")

# Ruta para crear una nueva consola
@app.route('/api/consolas', methods=['POST'])
def crear_consola():
    global next_id
    nueva_consola = {
        "id": next_id,
        "nombre": request.json.get('nombre', ''),
        "fabricante": request.json.get('fabricante', ''),
        "anio_lanzamiento": request.json.get('anio_lanzamiento', 0)
    }
    consolas.append(nueva_consola)
    next_id += 1
    return jsonify(nueva_consola), 201

# Ruta para actualizar una consola por su ID
@app.route('/api/consolas/<int:consola_id>', methods=['PUT'])
def actualizar_consola(consola_id):
    consola = next((consola for consola in consolas if consola['id'] == consola_id), None)
    if not consola:
        abort(404, f"No se encontró una consola con ID {consola_id}")

    consola['nombre'] = request.json.get('nombre', consola['nombre'])
    consola['fabricante'] = request.json.get('fabricante', consola['fabricante'])
    consola['anio_lanzamiento'] = request.json.get('anio_lanzamiento', consola['anio_lanzamiento'])
    return jsonify(consola)

# Ruta para eliminar una consola por su ID
@app.route('/api/consolas/<int:consola_id>', methods=['DELETE'])
def eliminar_consola(consola_id):
    global consolas
    consolas = [consola for consola in consolas if consola['id'] != consola_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
