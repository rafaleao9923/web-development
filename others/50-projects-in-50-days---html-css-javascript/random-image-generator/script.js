const container = document.querySelector('.container')
const picsumURL = 'https://picsum.photos/'

function addImages() {
    for(let i = 0; i < 3; i++) {
        const img = document.createElement('img')
        img.src = `${picsumURL}${getRandomNr()}/${getRandomNr()}`
        container.appendChild(img)
    }
}

function getRandomNr() {
    return Math.floor(Math.random() * 10) + 300
}

window.addEventListener('scroll', () => {
    if(window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 100) {
        addImages()
    }
})

for(let i = 0; i < 4; i++) {
    addImages()
}