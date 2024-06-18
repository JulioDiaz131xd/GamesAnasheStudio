from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Datos de ejemplo (simulando una base de datos)
usuarios = [
    { "id": 1, "nombre": "Juan", "edad": 30 },
    { "id": 2, "nombre": "María", "edad": 25 },
    { "id": 3, "nombre": "Pedro", "edad": 35 }
]
next_id = 4

# Ruta para obtener todos los usuarios
@app.route('/api/users', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

# Ruta para obtener un usuario por su ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_usuario(user_id):
    usuario = next((usuario for usuario in usuarios if usuario['id'] == user_id), None)
    if usuario:
        return jsonify(usuario)
    else:
        abort(404, f"No se encontró un usuario con ID {user_id}")

# Ruta para crear un nuevo usuario
@app.route('/api/users', methods=['POST'])
def crear_usuario():
    global next_id
    nuevo_usuario = {
        "id": next_id,
        "nombre": request.json.get('nombre', ''),
        "edad": request.json.get('edad', 0)
    }
    usuarios.append(nuevo_usuario)
    next_id += 1
    return jsonify(nuevo_usuario), 201

# Ruta para actualizar un usuario por su ID
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def actualizar_usuario(user_id):
    usuario = next((usuario for usuario in usuarios if usuario['id'] == user_id), None)
    if not usuario:
        abort(404, f"No se encontró un usuario con ID {user_id}")

    usuario['nombre'] = request.json.get('nombre', usuario['nombre'])
    usuario['edad'] = request.json.get('edad', usuario['edad'])
    return jsonify(usuario)

# Ruta para eliminar un usuario por su ID
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def eliminar_usuario(user_id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['id'] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
