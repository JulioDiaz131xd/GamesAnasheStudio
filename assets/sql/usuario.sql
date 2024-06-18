-- Tabla de Usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Perfiles
CREATE TABLE perfiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    nombre_completo VARCHAR(150),
    fecha_nacimiento DATE,
    foto_perfil VARCHAR(255),
    bio TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
