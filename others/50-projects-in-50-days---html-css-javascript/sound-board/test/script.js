let audio = new Audio();
let soundName = document.getElementById('sound-name');

async function fetchRandomSound() {
    const sounds = [
        { name: 'Applause', url: '../sounds/applause.mp3' },
        { name: 'Boo', url: '../sounds/boo.mp3' },
        { name: 'Gasp', url: '../sounds/gasp.mp3' },
        { name: 'Tada', url: '../sounds/tada.mp3' },
        { name: 'Victory', url: '../sounds/victory.mp3' },
        { name: 'Wrong', url: '../sounds/wrong.mp3' },
    ];
    return sounds[Math.floor(Math.random() * sounds.length)];
}

async function playRandomSound() {
    const btn = document.querySelector('.btn');
    btn.disabled = true;
    
    const sound = await fetchRandomSound();
    audio.src = sound.url;
    soundName.textContent = sound.name;
    
    try {
        await audio.play();
    } catch (error) {
        soundName.textContent = 'Error playing sound';
    }
    btn.disabled = false;
}

const btn = document.createElement('button');
btn.classList.add('btn');
btn.innerHTML = '<i class="fas fa-play"></i>';
btn.addEventListener('click', playRandomSound);

document.getElementById('buttons').appendChild(btn);