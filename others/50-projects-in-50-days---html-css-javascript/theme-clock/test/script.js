const hourEl = document.querySelector('.hour')
const minuteEl = document.querySelector('.minute')
const secondEl = document.querySelector('.second')
const dateEl = document.querySelector('.date')
const ampmEl = document.querySelector('.ampm')

function setTime() {
    const time = new Date()
    const hours = time.getHours()
    const hoursForClock = hours % 12
    const minutes = time.getMinutes()
    const seconds = time.getSeconds()
    const date = time.getDate()
    const ampm = hours >= 12 ? 180 : 0

    hourEl.style.transform = `translate(-50%, -100%) rotate(${scale(hoursForClock, 0, 12, 0, 360)}deg)`
    minuteEl.style.transform = `translate(-50%, -100%) rotate(${scale(minutes, 0, 60, 0, 360)}deg)`
    secondEl.style.transform = `translate(-50%, -100%) rotate(${scale(seconds, 0, 60, 0, 360)}deg)`
    dateEl.style.transform = `translate(-50%, -50%) rotate(${scale(date, 1, 31, 0, 360)}deg)`
    ampmEl.style.transform = `translate(-50%, -50%) rotate(${ampm}deg)`
}

const scale = (num, in_min, in_max, out_min, out_max) => {
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
}

setTime()
setInterval(setTime, 1000)