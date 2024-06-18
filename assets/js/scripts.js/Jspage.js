document.addEventListener('DOMContentLoaded', () => {
    const hero = document.querySelector('.hero');
    const heroTitle = hero.querySelector('h1');
    const heroSubtitle = hero.querySelector('h2');
    const heroParagraph = hero.querySelector('p');
    const heroButton = document.querySelector('#hero-button');

    const contents = [
        {
            image: 'https://images.nintendolife.com/e82ba6a08b16e/nintendo-switch.original.jpg',
            title: 'Juegos compatible con Joycon',
            subtitle: 'Experiencia imersiva',
            paragraph: 'Adéntrate en una nueva aventura ahora con titulos compatibles Joycon!',
            buttonText: 'Más información',
            buttonLink: 'link1.html'
        },
        {
            image: 'https://static1.colliderimages.com/wordpress/wp-content/uploads/2021/05/PS5.jpg',
            title: 'Ahora Compatible con PS5',
            subtitle: 'Adentrate con las nuevos titulos con trazado de rayos',
            paragraph: 'Ahora con mas potencia!',
            buttonText: 'Descubre más',
            buttonLink: 'link2.html'
        },
        {
            image: 'https://i0.wp.com/xxboxnews.blob.core.windows.net/prod/sites/4/Consoles-eb36182249206cefa827-7bce25d8508235e4e317.jpg?fit=1920%2C1080&ssl=1',
            title: 'Ahora Compatible con Todas las Series De XBOX',
            subtitle: '¡La saga continúa!',
            paragraph: 'Prepárate para la última aventura de ASTRO con nuevas sorpresas y diversión garantizada.',
            buttonText: 'Ver detalles',
            buttonLink: 'link3.html'
        }
    ];

    let currentIndex = 0;

    function changeHeroContent() {
        const { image, title, subtitle, paragraph, buttonText, buttonLink } = contents[currentIndex];
        hero.style.backgroundImage = `url(${image})`;
        heroTitle.textContent = title;
        heroSubtitle.textContent = subtitle;
        heroParagraph.textContent = paragraph;
        heroButton.textContent = buttonText;
        heroButton.href = buttonLink;
        currentIndex = (currentIndex + 1) % contents.length;
    }

    setInterval(changeHeroContent, 5000);
});
