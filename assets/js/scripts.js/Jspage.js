document.addEventListener('DOMContentLoaded', () => {
    const hero = document.querySelector('.hero');
    const heroTitle = hero.querySelector('h1');
    const heroSubtitle = hero.querySelector('h2');
    const heroParagraph = hero.querySelector('p');
    const heroButton = document.querySelector('#hero-button');

    const contents = [
        {
            image: 'assets/img/logo1.jpg',
            title: 'ASTRO BOT',
            subtitle: '¡ASTRO está de regreso!',
            paragraph: 'Adéntrate en una aventura nueva de gran tamaño con ASTRO en 50 mundos emocionantes y diversos.',
            buttonText: 'Más información',
            buttonLink: 'link1.html'
        },
        {
            image: 'assets/img/logo2.jpg',
            title: 'ASTRO BOT 2',
            subtitle: '¡Nuevas aventuras!',
            paragraph: 'Descubre nuevos mundos y desafíos con ASTRO en su segunda entrega.',
            buttonText: 'Descubre más',
            buttonLink: 'link2.html'
        },
        {
            image: 'assets/img/logo3.jpg',
            title: 'ASTRO BOT 3',
            subtitle: '¡La saga continúa!',
            paragraph: 'Prepárate para la última aventura de ASTRO con nuevas sorpresas y diversión garantizada.',
            buttonText: 'Ver detalles',
            buttonLink: 'link3.html'
        }
    ];

    let currentIndex = 0;

    function changeHeroContent() {
        const { image, title, subtitle, paragraph, buttonText, buttonLink } = contents[currentIndex];
        currentIndex = (currentIndex + 1) % contents.length;
        hero.style.backgroundImage = `url(${image})`;
        heroTitle.textContent = title;
        heroSubtitle.textContent = subtitle;
        heroParagraph.textContent = paragraph;
        heroButton.textContent = buttonText;
        heroButton.href = buttonLink;
    }

    setInterval(changeHeroContent, 3000);
});