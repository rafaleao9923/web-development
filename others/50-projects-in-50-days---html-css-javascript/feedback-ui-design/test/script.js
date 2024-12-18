const panel = document.querySelector('#panel')
let selectedRating = 'Satisfied'

function initializeRatings() {
    const ratings = document.querySelectorAll('.rating')
    ratings.forEach(rating => {
        rating.addEventListener('click', () => {
            ratings.forEach(r => r.classList.remove('active'))
            rating.classList.add('active')
            selectedRating = rating.querySelector('small').innerHTML
        })
    })
}

function showReviewForm() {
    panel.innerHTML = `
        <strong>How satisfied are you with our <br /> customer support performance?</strong>
        <div class="ratings-container">
            <div class="rating ${selectedRating === 'Unhappy' ? 'active' : ''}">
                <i class="fas fa-frown"></i>
                <small>Unhappy</small>
            </div>
            <div class="rating ${selectedRating === 'Neutral' ? 'active' : ''}">
                <i class="fas fa-meh"></i>
                <small>Neutral</small>
            </div>
            <div class="rating ${selectedRating === 'Satisfied' ? 'active' : ''}">
                <i class="fas fa-smile"></i>
                <small>Satisfied</small>
            </div>
        </div>
        <button class="btn" id="send">Send Review</button>
    `
    document.querySelector('#send').addEventListener('click', showThankYou)
    initializeRatings()
}

function showThankYou() {
    panel.innerHTML = `
        <i class="fas fa-heart"></i>
        <strong>Thank You!</strong>
        <br>
        <strong>Feedback: ${selectedRating}</strong>
        <p>We'll use your feedback to improve our customer support</p>
        <p>Do you want to review again?</p>
        <div class="button-group">
            <button class="btn" id="review-again">Review Again</button>
            <button class="btn" id="send-feedback">Send Feedback</button>
        </div>
    `
    document.querySelector('#review-again').addEventListener('click', showReviewForm)
    document.querySelector('#send-feedback').addEventListener('click', () => {
        panel.innerHTML = `
            <i class="fas fa-paper-plane"></i>
            <strong>Feedback Sent!</strong>
            <p>Thank you for helping us improve our service</p>
            <button class="btn" id="new-feedback" onclick="window.location.reload()">Submit New Feedback</button>
        `
    })
}

initializeRatings()
document.querySelector('#send').addEventListener('click', showThankYou)