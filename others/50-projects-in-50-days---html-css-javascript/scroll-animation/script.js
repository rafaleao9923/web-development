const container = document.body;
let isLoading = false;
let imageCounter = 0;

function createBox() {
    const box = document.createElement('div');
    box.classList.add('box');
    const img = document.createElement('img');
    img.src = `https://picsum.photos/400/300?random=${imageCounter++}`;
    box.appendChild(img);
    return box;
}

function addBoxes(count = 5) {
    for (let i = 0; i < count; i++) {
        container.insertBefore(createBox(), container.lastElementChild);
    }
    checkBoxes();
}

function checkBoxes() {
    const triggerBottom = window.innerHeight / 5 * 4;
    const boxes = document.querySelectorAll('.box');

    boxes.forEach(box => {
        const boxTop = box.getBoundingClientRect().top;
        if (boxTop < triggerBottom) {
            box.classList.add('show');
        } else {
            box.classList.remove('show');
        }
    });
}

function handleScroll() {
    const { scrollTop, clientHeight, scrollHeight } = document.documentElement;
    
    if (!isLoading && scrollTop + clientHeight >= scrollHeight - 20) {
        isLoading = true;
        
        // Show loading spinner
        document.querySelector('.loading').style.display = 'flex';
        
        // Simulate loading delay
        setTimeout(() => {
            addBoxes(5);
            isLoading = false;
            document.querySelector('.loading').style.display = 'none';
        }, 500);
    }
    
    checkBoxes();
}

// Create loading spinner
const loadingDiv = document.createElement('div');
loadingDiv.className = 'loading';
loadingDiv.style.display = 'none';
loadingDiv.innerHTML = '<div class="loading-spinner"></div>';
document.body.appendChild(loadingDiv);

// Initial load
addBoxes(15);

// Event listeners
window.addEventListener('scroll', handleScroll);
window.addEventListener('resize', checkBoxes);