from flask import Flask, jsonify, request, abort
import hashlib

app = Flask(__name__)

# Datos de ejemplo (simulando una base de datos)
contraseñas = [
    { "id": 1, "usuario": "juan", "contraseña": hashlib.sha256("123456".encode()).hexdigest() },
    { "id": 2, "usuario": "maria", "contraseña": hashlib.sha256("password".encode()).hexdigest() },
    { "id": 3, "usuario": "pedro", "contraseña": hashlib.sha256("abc123".encode()).hexdigest() }
]
next_id = 4

# Función para hashear contraseñas
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Ruta para obtener todas las contraseñas
@app.route('/api/contraseñas', methods=['GET'])
def get_contraseñas():
    return jsonify(contraseñas)

# Ruta para obtener una contraseña por su ID
@app.route('/api/contraseñas/<int:contraseña_id>', methods=['GET'])
def get_contraseña(contraseña_id):
    contraseña = next((contraseña for contraseña in contraseñas if contraseña['id'] == contraseña_id), None)
    if contraseña:
        return jsonify(contraseña)
    else:
        abort(404, f"No se encontró una contraseña con ID {contraseña_id}")

# Ruta para crear una nueva contraseña
@app.route('/api/contraseñas', methods=['POST'])
def crear_contraseña():
    global next_id
    usuario = request.json.get('usuario', '')
    password = request.json.get('contraseña', '')
    nueva_contraseña = {
        "id": next_id,
        "usuario": usuario,
        "contraseña": hash_password(password)
    }
    contraseñas.append(nueva_contraseña)
    next_id += 1
    return jsonify(nueva_contraseña), 201

# Ruta para actualizar una contraseña por su ID
@app.route('/api/contraseñas/<int:contraseña_id>', methods=['PUT'])
def actualizar_contraseña(contraseña_id):
    contraseña = next((contraseña for contraseña in contraseñas if contraseña['id'] == contraseña_id), None)
    if not contraseña:
        abort(404, f"No se encontró una contraseña con ID {contraseña_id}")

    contraseña['usuario'] = request.json.get('usuario', contraseña['usuario'])
    contraseña['contraseña'] = hash_password(request.json.get('contraseña', contraseña['contraseña']))
    return jsonify(contraseña)

# Ruta para eliminar una contraseña por su ID
@app.route('/api/contraseñas/<int:contraseña_id>', methods=['DELETE'])
def eliminar_contraseña(contraseña_id):
    global contraseñas
    contraseñas = [contraseña for contraseña in contraseñas if contraseña['id'] != contraseña_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
