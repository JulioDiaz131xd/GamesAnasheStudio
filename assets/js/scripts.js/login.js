document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('loginForm').addEventListener('submit', (event) => {
        event.preventDefault();
        
        // Simulación de inicio de sesión
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Verificar las credenciales
        if (username === 'julio' && password === '123') {
            // Redireccionar a la página deseada
            window.location.href = 'Homepage2.html';
        } else {
            // Mostrar mensaje de error si las credenciales son incorrectas
            document.getElementById('loginMessage').textContent = 'Usuario o contraseña incorrectos';
        }
    });
});
