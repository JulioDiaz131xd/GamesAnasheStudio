let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-item');
const track = document.querySelector('.carousel-track');

function showSlide(index) {
    const slideWidth = slides[0].clientWidth;
    const newTransform = -index * slideWidth;
    track.style.transform = `translateX(${newTransform}px)`;
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
}

function addToCart() {
    alert("Juego agregado al carrito.");
}

function toggleTrialDetails() {
    const details = document.getElementById('trial-details');
    if (details.style.display === 'none') {
        details.style.display = 'block';
    } else {
        details.style.display = 'none';
    }
}

window.addEventListener('resize', () => showSlide(currentSlide));
showSlide(currentSlide);