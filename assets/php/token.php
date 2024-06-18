<?php
function generarCodigoAleatorio($longitud) {
    $caracteres = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $longitud_caracteres = strlen($caracteres);
    $codigo = '';
    for ($i = 0; $i < $longitud; $i++) {
        $codigo .= $caracteres[rand(0, $longitud_caracteres - 1)];
    }
    return $codigo;
}

// Generar un código aleatorio de longitud 10
$codigo_aleatorio = generarCodigoAleatorio(10);
echo "Código Aleatorio: $codigo_aleatorio";
?>
