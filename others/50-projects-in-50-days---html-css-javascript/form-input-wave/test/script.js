const labels = document.querySelectorAll('.form-control label')
const registerLink = document.querySelector('.register-link')
const container = document.querySelector('.container')
const form = document.querySelector('form')

labels.forEach(label => {
    label.innerHTML = label.innerText
        .split('')
        .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
        .join('')
})

function createFirework(x, y, color) {
    const firework = document.createElement('div')
    firework.className = 'firework'
    firework.style.left = `${x}px`
    firework.style.top = `${y}px`
    firework.style.backgroundColor = color
    document.body.appendChild(firework)
    
    setTimeout(() => firework.remove(), 1000)
}

function launchFireworks() {
    const colors = ['#00ff88', '#00b4d8', '#ff0088', '#ffe600', '#ff3300']
    for(let i = 0; i < 20; i++) {
        setTimeout(() => {
            const x = Math.random() * window.innerWidth
            const y = Math.random() * window.innerHeight
            const color = colors[Math.floor(Math.random() * colors.length)]
            createFirework(x, y, color)
        }, i * 100)
    }
}

function switchToRegister(e) {
    e.preventDefault()
    container.innerHTML = `
        <h1>Create Account</h1>
        <form>
            <div class="form-control">
                <input type="text" required>
                <label>Username</label>
            </div>
            <div class="form-control">
                <input type="email" required>
                <label>Email</label>
            </div>
            <div class="form-control">
                <input type="password" required>
                <label>Password</label>
            </div>
            <button class="btn register-btn">Register</button>
            <p class="text">Already have an account? <a href="#" class="login-link">Login</a></p>
        </form>
    `
    
    const newLabels = document.querySelectorAll('.form-control label')
    newLabels.forEach(label => {
        label.innerHTML = label.innerText
            .split('')
            .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms">${letter}</span>`)
            .join('')
    })
    
    document.querySelector('.register-btn').addEventListener('click', (e) => {
        e.preventDefault()
        launchFireworks()
    })
    
    document.querySelector('.login-link').addEventListener('click', (e) => {
        e.preventDefault()
        window.location.reload()
    })
}

document.addEventListener('click', (e) => {
    if (e.target.matches('.register-link, .register-link *')) {
        switchToRegister(e)
    }
})