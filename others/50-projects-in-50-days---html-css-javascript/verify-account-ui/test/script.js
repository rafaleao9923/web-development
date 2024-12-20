const codes = document.querySelectorAll('.code')
const verifyBtn = document.querySelector('.verify-btn')
const loading = document.querySelector('.loading')
const message = document.querySelector('.message')
const retryBtn = document.querySelector('.retry-btn')
const container = document.querySelector('.container')

let secretCode = generateCode()
let currentEnteredCode = ''

const correctSound = new Audio('https://assets.mixkit.co/active_storage/sfx/2000/2000.wav')
const wrongSound = new Audio('https://assets.mixkit.co/active_storage/sfx/2003/2003.wav')

function generateCode() {
    return Math.floor(100000 + Math.random() * 900000).toString()
}

function saveState() {
    const codeState = Array.from(codes).map(input => input.value)
    sessionStorage.setItem('verificationState', JSON.stringify({
        codeState,
        secretCode,
        completed: false
    }))
}

function clearState() {
    sessionStorage.removeItem('verificationState')
    codes.forEach(input => {
        input.value = ''
        input.style.transform = 'none'
    })
    codes[0].focus()
    message.style.display = 'none'
    retryBtn.style.display = 'none'
    verifyBtn.disabled = false
    container.style.boxShadow = '0 15px 35px rgba(0, 0, 0, 0.2)'
}

window.addEventListener('beforeunload', () => {
    clearState()
})

window.addEventListener('load', () => {
    clearState()
})

function createFirework(x, y) {
    const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff']
    const firework = document.createElement('div')
    firework.className = 'firework'
    firework.style.left = x + 'px'
    firework.style.top = y + 'px'
    firework.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)]
    document.body.appendChild(firework)

    const animation = firework.animate([
        { transform: 'scale(1)', opacity: 1 },
        { transform: 'scale(50)', opacity: 0 }
    ], {
        duration: 1000,
        easing: 'ease-out'
    })

    animation.onfinish = () => firework.remove()
}

function launchFireworks() {
    for(let i = 0; i < 20; i++) {
        setTimeout(() => {
            const x = Math.random() * window.innerWidth
            const y = Math.random() * window.innerHeight
            createFirework(x, y)
        }, i * 100)
    }
}

function handlePaste(e) {
    e.preventDefault()
    const pastedData = e.clipboardData.getData('text')
    if (/^\d{6}$/.test(pastedData)) {
        Array.from(pastedData).forEach((digit, index) => {
            codes[index].value = digit
            if (index === codes.length - 1) {
                codes[index].blur()
                verifyBtn.focus()
            }
        })
        currentEnteredCode = pastedData
        saveState()
    }
}

codes[0].focus()

codes.forEach((code, idx) => {
    code.addEventListener('paste', handlePaste)
    
    code.addEventListener('keydown', (e) => {
        if(e.key >= 0 && e.key <= 9) {
            codes[idx].value = ''
            setTimeout(() => {
                if (idx < codes.length - 1) {
                    codes[idx + 1].focus()
                } else {
                    codes[idx].blur()
                    verifyBtn.focus()
                }
                currentEnteredCode = Array.from(codes).map(input => input.value).join('')
                saveState()
            }, 10)
        } else if(e.key === 'Backspace') {
            setTimeout(() => {
                if (idx > 0) {
                    codes[idx - 1].focus()
                }
                currentEnteredCode = Array.from(codes).map(input => input.value).join('')
                saveState()
            }, 10)
        }
    })

    code.addEventListener('input', (e) => {
        if(code.value.length === 6 && /^\d{6}$/.test(code.value)) {
            const digits = code.value.split('')
            digits.forEach((digit, index) => {
                codes[index].value = digit
            })
            codes[idx].blur()
            verifyBtn.focus()
            currentEnteredCode = code.value
            saveState()
        } else if(code.value.length === 1 && idx < codes.length - 1) {
            codes[idx + 1].focus()
            currentEnteredCode = Array.from(codes).map(input => input.value).join('')
            saveState()
        }
    })
})

verifyBtn.addEventListener('click', async () => {
    const enteredCode = Array.from(codes).map(input => input.value).join('')
    
    if(enteredCode.length !== 6) {
        showMessage('Please enter all digits', false)
        return
    }

    verifyBtn.disabled = true
    loading.style.display = 'block'
    message.style.display = 'none'

    await new Promise(resolve => setTimeout(resolve, 1000))
    
    loading.style.display = 'none'

    if(enteredCode === secretCode) {
        correctSound.play()
        launchFireworks()
        showMessage('✨ Verification successful! ✨', true)
        container.style.boxShadow = '0 0 50px rgba(46, 204, 113, 0.5)'
        sessionStorage.setItem('verificationState', JSON.stringify({ completed: true }))
    } else {
        wrongSound.play()
        container.classList.add('shake')
        showMessage('❌ Incorrect code. Please try again.', false)
        container.style.boxShadow = '0 0 50px rgba(231, 76, 60, 0.5)'
        retryBtn.style.display = 'inline-block'
        setTimeout(() => {
            container.classList.remove('shake')
        }, 500)
    }
})

retryBtn.addEventListener('click', () => {
    secretCode = generateCode()
    console.log(secretCode)
    clearState()
})

function showMessage(text, isSuccess) {
    message.textContent = text
    message.className = 'message ' + (isSuccess ? 'success' : 'error')
    message.style.display = 'block'
}

console.log('Secret code:', secretCode)