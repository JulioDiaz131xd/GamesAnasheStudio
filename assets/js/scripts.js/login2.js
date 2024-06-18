document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('loginForm').addEventListener('submit', (event) => {
        event.preventDefault();
        alert('Inicio de sesión exitoso');
        window.location.href = 'Login.html';
    });
});
