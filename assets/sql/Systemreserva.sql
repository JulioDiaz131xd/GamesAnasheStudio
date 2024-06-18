-- Tabla de Vuelos
CREATE TABLE vuelos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_vuelo VARCHAR(20) NOT NULL,
    aerolinea VARCHAR(100) NOT NULL,
    origen VARCHAR(100) NOT NULL,
    destino VARCHAR(100) NOT NULL,
    fecha_salida DATE NOT NULL,
    hora_salida TIME NOT NULL,
    capacidad INT NOT NULL
);

-- Tabla de Pasajeros
CREATE TABLE pasajeros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    documento_identidad VARCHAR(50) NOT NULL
);

-- Tabla de Reservas
CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vuelo_id INT NOT NULL,
    pasajero_id INT NOT NULL,
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vuelo_id) REFERENCES vuelos(id),
    FOREIGN KEY (pasajero_id) REFERENCES pasajeros(id)
);
