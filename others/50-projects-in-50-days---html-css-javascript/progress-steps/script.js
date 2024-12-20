const progress = document.getElementById('progress')
const prev = document.getElementById('prev')
const next = document.getElementById('next')
const circles = document.querySelectorAll('.circle')

let currentActive = 1

next.addEventListener('click', () => {
    currentActive++
    if(currentActive > circles.length) {
        currentActive = circles.length
    }
    update()
})

prev.addEventListener('click', () => {
    currentActive--
    if(currentActive < 1) {
        currentActive = 1
    }
    update()
})

function update() {
    circles.forEach((circle, idx) => {
        if(idx < currentActive) {
            circle.classList.add('active')
        } else {
            circle.classList.remove('active')
        }
    })

    const actives = document.querySelectorAll('.active')
    progress.style.width = (actives.length - 1) / (circles.length - 1) * 100 + '%'

    if(currentActive === 1) {
        prev.disabled = true
        prev.classList.remove('darken')
        next.classList.remove('fade')
        next.style.opacity = 1
    } else if(currentActive === circles.length) {
        next.disabled = true
        next.classList.remove('fade')
        prev.classList.add('darken')
        prev.style.opacity = 1
    } else {
        prev.disabled = false
        next.disabled = false
        const fadeLevel = currentActive / circles.length
        next.classList.add('fade')
        next.style.opacity = 1 - (fadeLevel * 0.3)
        prev.classList.add('darken')
        prev.style.opacity = fadeLevel
    }
}