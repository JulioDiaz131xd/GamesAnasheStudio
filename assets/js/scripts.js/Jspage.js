document.addEventListener('DOMContentLoaded', () => {
    const hero = document.querySelector('.hero');
    const heroTitle = hero.querySelector('h1');
    const heroSubtitle = hero.querySelector('h2');
    const heroParagraph = hero.querySelector('p');
    const heroButton = document.querySelector('#hero-button');

    const contents = [
        {
            image: 'assets/img/vr.png',
            title: 'Juegos compatible con realidad VR',
            subtitle: 'Experiencia imersiva',
            paragraph: 'Adéntrate en una nueva aventura ahora con titulos compatibles con VR y GeforceAnashe Cloud',
            buttonText: 'Más información',
            buttonLink: 'link1.html'
        },
        {
            image: 'assets/img/ps5gif.gif',
            title: 'Ahora Compatible con PS5',
            subtitle: 'Adentrate con las nuevas tecnologias ',
            paragraph: 'Ahora compatibles con PS5',
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

    setInterval(changeHeroContent, 7000);
});