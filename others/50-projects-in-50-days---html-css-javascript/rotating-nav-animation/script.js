const open = document.getElementById('open')
const close = document.getElementById('close')
const container = document.querySelector('.container')
const content = document.querySelector('.content')

open.addEventListener('click', () => container.classList.add('show-nav'))
close.addEventListener('click', () => container.classList.remove('show-nav'))

function loadContent() {
    fetch('http://localhost:8005/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'param=generate'
    })
    .then(response => response.json())
    .then(data => {
        content.innerHTML = `
            <h1>${data.title}</h1>
            <small>${data.subtitle}</small>
            <img src="${data.image}?${new Date().getTime()}" alt="Article Image" />
            <p>${data.content}</p>
        `;
    })
    .catch(error => {
        content.innerHTML = `
            <h1>Error Loading Content</h1>
            <p>Make sure the Python server is running on port 8000</p>
            <p>Run: python content.py</p>
        `;
        console.error('Error:', error);
    });
}

document.addEventListener('DOMContentLoaded', loadContent);