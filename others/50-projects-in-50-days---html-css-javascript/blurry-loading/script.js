const loadText = document.querySelector('.loading-text')
const bg = document.querySelector('.bg')
const replayButton = document.getElementById('replay')

let load = 0

let int = setInterval(blurring, 30)

function blurring() {
  load++

  if (load > 99) {
    clearInterval(int)
  }

  loadText.innerText = `${load}%`
  loadText.style.opacity = scale(load, 0, 100, 1, 0)
  bg.style.filter = `blur(${scale(load, 0, 100, 30, 0)}px)`
}

// https://stackoverflow.com/questions/10756313/javascript-jquery-map-a-range-of-numbers-to-another-range-of-numbers
const scale = (num, in_min, in_max, out_min, out_max) => {
  return ((num - in_min) * (out_max - out_min)) / (in_max - in_min) + out_min
}

replayButton.addEventListener('click', () => {
  load = 0
  loadText.innerText = '0%'
  loadText.style.opacity = 1
  bg.style.filter = 'blur(30px)'
  int = setInterval(blurring, 30)
})
