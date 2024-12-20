const quizData = [
    {
        question: "Which language runs in a web browser?",
        a: "Java",
        b: "C",
        c: "Python",
        d: "JavaScript",
        correct: "d",
    },
    {
        question: "What does CSS stand for?",
        a: "Central Style Sheets",
        b: "Cascading Style Sheets",
        c: "Cascading Simple Sheets",
        d: "Cars SUVs Sailboats",
        correct: "b",
    },
    {
        question: "What does HTML stand for?",
        a: "Hypertext Markup Language",
        b: "Hypertext Markdown Language",
        c: "Hyperloop Machine Language",
        d: "Helicopters Terminals Motorboats Lamborginis",
        correct: "a",
    },
    {
        question: "What year was JavaScript launched?",
        a: "1996",
        b: "1995",
        c: "1994",
        d: "none of the above",
        correct: "b",
    }
];

const quiz = document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const c_text = document.getElementById('c_text')
const d_text = document.getElementById('d_text')
const submitBtn = document.getElementById('submit')

let currentQuiz = 0
let score = 0
let userAnswers = []
let quizHistory = []

loadQuiz()

function loadQuiz() {
    deselectAnswers()
    const currentQuizData = quizData[currentQuiz]
    questionEl.innerText = currentQuizData.question
    a_text.innerText = currentQuizData.a
    b_text.innerText = currentQuizData.b
    c_text.innerText = currentQuizData.c
    d_text.innerText = currentQuizData.d
}

function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}

function getSelected() {
    let answer
    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = answerEl.id
        }
    })
    return answer
}

function saveQuizState() {
    const answers = document.querySelectorAll('label')
    const state = {
        question: questionEl.innerText,
        answers: Array.from(answers).map(label => ({
            text: label.innerText,
            option: label.getAttribute('data-option')
        })),
        userAnswer: getSelected(),
        correctAnswer: quizData[currentQuiz].correct
    }
    quizHistory.push(state)
}

submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    if(answer) {
        saveQuizState()
        userAnswers.push(answer)
        if(answer === quizData[currentQuiz].correct) {
            score++
        }
        currentQuiz++

        if(currentQuiz < quizData.length) {
            loadQuiz()
        } else {
            quiz.innerHTML = `
                <div class="result-text">
                    <h2>You answered ${score}/${quizData.length} questions correctly</h2>
                </div>
                <div class="button-container">
                    <button id="view-result">View Results</button>
                    <button id="reload">Reload</button>
                </div>
            `
            document.getElementById('view-result').addEventListener('click', showResults)
            document.getElementById('reload').addEventListener('click', () => location.reload())
        }
    }
})

function showResults() {
    let resultsHTML = '<div class="quiz-header">'
    quizHistory.forEach((state, index) => {
        resultsHTML += `
            <div class="question-review">
                <h2>${state.question}</h2>
                <div class="answer-grid">
                    ${state.answers.map(answer => `
                        <div class="answer-option ${
                            answer.option === state.correctAnswer && answer.option === state.userAnswer ? 'correct' :
                            answer.option === state.correctAnswer ? 'correct-answer' :
                            answer.option === state.userAnswer ? 'wrong' : ''
                        }">
                            ${answer.text}
                        </div>
                    `).join('')}
                </div>
            </div>
        `
    })
    resultsHTML += `
        </div>
        <div class="button-container">
            <button id="reload">Reload Quiz</button>
        </div>
    `
    quiz.innerHTML = resultsHTML
    document.getElementById('reload').addEventListener('click', () => location.reload())
}