const joke1El = document.getElementById('joke1')
const joke2El = document.getElementById('joke2')
const jokeBtn = document.getElementById('jokeBtn')

let isGenerating = false
let jokeQueue = []
const QUEUE_SIZE = 6 // Keep 3 pairs of jokes ready

jokeBtn.addEventListener('click', handleJokeGeneration)
jokeBtn.addEventListener('click', function(e) {
  const x = e.clientX
  const y = e.clientY
  
  const buttonTop = e.target.offsetTop
  const buttonLeft = e.target.offsetLeft
  
  const xInside = x - buttonLeft
  const yInside = y - buttonTop
  
  const circle = document.createElement('span')
  circle.classList.add('circle')
  circle.style.top = yInside + 'px'
  circle.style.left = xInside + 'px'
  
  this.appendChild(circle)
  
  setTimeout(() => circle.remove(), 500)
})

let currentAnimation1 = null
let currentAnimation2 = null
let speed = 100

function writeText(element, text, index) {
    if (element === joke1El) {
        if (currentAnimation1) clearTimeout(currentAnimation1)
    } else {
        if (currentAnimation2) clearTimeout(currentAnimation2)
    }

    element.innerText = text.slice(0, index)

    if(index <= text.length) {
        const timeoutId = setTimeout(() => writeText(element, text, index + 1), speed)
        if (element === joke1El) {
            currentAnimation1 = timeoutId
        } else {
            currentAnimation2 = timeoutId
        }
    }
}

const fonts = [
  'Pacifico',
  'Press Start 2P',
  'Permanent Marker',
  'Comic Neue',
  'Bangers',
  'VT323',
  'Fredoka One',
  'Roboto'
]

function getRandomColor() {
  const letters = '0123456789ABCDEF'
  let color = '#'
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)]
  }
  return color
}

function getRandomFont() {
  return fonts[Math.floor(Math.random() * fonts.length)]
}

async function fetchJoke() {
  const config = {
    headers: {
      Accept: 'application/json',
    },
  }
  const response = await fetch('https://icanhazdadjoke.com', config)
  const data = await response.json()
  return data.joke
}

async function preloadJokes() {
  while (jokeQueue.length < QUEUE_SIZE) {
    try {
      const [joke1, joke2] = await Promise.all([fetchJoke(), fetchJoke()])
      jokeQueue.push({ joke1, joke2 })
    } catch (error) {
      console.error('Error preloading jokes:', error)
    }
  }
}

function displayJokes(jokes) {
  const color1 = getRandomColor()
  const color2 = getRandomColor()
  const font1 = getRandomFont()
  const font2 = getRandomFont()

  joke1El.style.color = color1
  joke2El.style.color = color2
  joke1El.style.fontFamily = font1
  joke2El.style.fontFamily = font2

  writeText(joke1El, jokes.joke1, 1)
  writeText(joke2El, jokes.joke2, 1)
}

async function handleJokeGeneration() {
  if (jokeQueue.length === 0) {
    joke1El.textContent = 'Loading...'
    joke2El.textContent = 'Loading...'
    await preloadJokes()
  }

  const jokes = jokeQueue.shift()
  displayJokes(jokes)
  
  // Preload more jokes when queue gets low
  if (jokeQueue.length < QUEUE_SIZE/2) {
    preloadJokes()
  }
}

// Initial load
async function initialize() {
  joke1El.textContent = 'Loading...'
  joke2El.textContent = 'Loading...'
  
  await preloadJokes()
  handleJokeGeneration()
}

initialize()