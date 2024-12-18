let currentPage = 1;
let isLoading = false;
let reachedEnd = false;

async function getData(page) {
    const response = await fetch('info.json');
    const data = await response.json();
    const startIndex = (page - 1) * 6;
    const endIndex = startIndex + 6;
    
    let cards = [];
    for (let i = startIndex; i < endIndex; i++) {
        cards.push(data.cards[i % data.cards.length]);
    }
    // console.log(cards)
    return cards;
}

function loadCard(card, cardNum) {
    const cardsContainer = document.querySelector('.cards-container');
    const cardElement = document.createElement('div');
    cardElement.className = 'card';
    cardElement.innerHTML = `
        <div class="card-header animated-bg" id="header-${cardNum}">&nbsp;</div>
        <div class="card-content">
            <h3 class="card-title animated-bg animated-bg-text" id="title-${cardNum}">&nbsp;</h3>
            <p class="card-excerpt" id="excerpt-${cardNum}">
                &nbsp;
                <span class="animated-bg animated-bg-text">&nbsp;</span>
                <span class="animated-bg animated-bg-text">&nbsp;</span>
                <span class="animated-bg animated-bg-text">&nbsp;</span>
            </p>
            <div class="author">
                <div class="profile-img animated-bg" id="profile_img-${cardNum}">&nbsp;</div>
                <div class="author-info">
                    <strong class="animated-bg animated-bg-text" id="name-${cardNum}">&nbsp;</strong>
                    <small class="animated-bg animated-bg-text" id="date-${cardNum}">&nbsp;</small>
                </div>
            </div>
        </div>
    `;
    
    cardsContainer.appendChild(cardElement);

    setTimeout(() => {
        const header = document.getElementById(`header-${cardNum}`);
        const title = document.getElementById(`title-${cardNum}`);
        const excerpt = document.getElementById(`excerpt-${cardNum}`);
        const profile_img = document.getElementById(`profile_img-${cardNum}`);
        const name = document.getElementById(`name-${cardNum}`);
        const date = document.getElementById(`date-${cardNum}`);

        header.innerHTML = `<img src="${card.header_img}" alt="">`;
        title.innerHTML = card.title;
        excerpt.innerHTML = card.excerpt;
        profile_img.innerHTML = `<img src="${card.profile_img}" alt="">`;
        name.innerHTML = card.author_name;
        date.innerHTML = card.date;

        header.classList.remove('animated-bg');
        title.classList.remove('animated-bg', 'animated-bg-text');
        excerpt.classList.remove('animated-bg', 'animated-bg-text');
        profile_img.classList.remove('animated-bg');
        name.classList.remove('animated-bg', 'animated-bg-text');
        date.classList.remove('animated-bg', 'animated-bg-text');
    }, 500);
}

async function loadNextPage() {
    if (isLoading || reachedEnd) return;
    
    isLoading = true;
    const cards = await getData(currentPage);
    
    if (cards.length === 0) {
        reachedEnd = true;
        isLoading = false;
        return;
    }

    cards.forEach((card, index) => {
        const globalIndex = (currentPage - 1) * 6 + index;
        setTimeout(() => {
            loadCard(card, globalIndex + 1);
        }, 500 * index);
    });

    currentPage++;
    setTimeout(() => {
        isLoading = false;
    }, 500 * cards.length);
}

function handleScroll() {
    const { scrollTop, scrollHeight, clientHeight } = document.documentElement;
    
    if (scrollTop + clientHeight >= scrollHeight - 100) {
        loadNextPage();
    }
}

function init() {
    document.querySelector('.cards-container').innerHTML = '';
    window.addEventListener('scroll', handleScroll);
    loadNextPage();
}

init();