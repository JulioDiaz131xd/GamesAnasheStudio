document.addEventListener('DOMContentLoaded', () => {
    fetch('http://localhost/project/api/get_juegos.php')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#juegosTable tbody');
            data.forEach(juego => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${juego.titulo}</td>
                    <td>${juego.plataforma}</td>
                    <td>${juego.anio_lanzamiento}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error al cargar los datos:', error));
});
