<?php
session_start();

$servername = "localhost"; 
$username = "tu_usuario"; 
$password = "tu_contraseña"; 
$dbname = "nombre_de_tu_base_de_datos"; 

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtener datos del formulario de inicio de sesión
$username = $_POST['username'];
$password = $_POST['password'];

// Consulta SQL para verificar las credenciales del usuario
$sql = "SELECT * FROM usuarios WHERE username = '$username' AND password = '$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Inicio de sesión exitoso
    $_SESSION['loggedin'] = true;
    $_SESSION['username'] = $username;
    header("Location: pagina_principal.php"); // Redirigir a la página principal
} else {
    // Inicio de sesión fallido
    header("Location: index.php?error=1"); // Redirigir de nuevo al formulario de inicio de sesión con mensaje de error
}

$conn->close();
?>
