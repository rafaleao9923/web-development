// Intersection Observer for scroll animations
const observerOptions = {
    threshold: 0.25,
    rootMargin: "0px"
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', () => {
    // Animate elements on scroll
    document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));

    // Dynamic trading statistics
    updateTradingStats();
    setInterval(updateTradingStats, 5000);

    // Cryptocurrency price ticker
    initPriceTicker();

    // Typed.js effect for hero text
    new Typed('#typed-text', {
        strings: [
            'Smarter Trading Decisions',
            'AI-Powered Insights',
            'Real-time Market Analysis'
        ],
        typeSpeed: 50,
        backSpeed: 30,
        backDelay: 2000,
        loop: true
    });

    // Particle background
    particlesJS('particles-js', {
        particles: {
            number: { value: 80 },
            color: { value: '#a599e9' },
            opacity: { value: 0.5 },
            size: { value: 3 },
            line_linked: {
                enable: true,
                distance: 150,
                color: '#a599e9',
                opacity: 0.4,
                width: 1
            },
            move: {
                enable: true,
                speed: 2
            }
        }
    });
});

// Dynamic trading statistics update
function updateTradingStats() {
    const stats = [
        { id: 'accuracy', min: 87, max: 92, suffix: '%' },
        { id: 'volume', min: 1.1, max: 1.4, prefix: '$', suffix: 'B' },
        { id: 'traders', min: 9800, max: 10200, suffix: '+' }
    ];

    stats.forEach(stat => {
        const value = generateRandomStat(stat.min, stat.max);
        const element = document.getElementById(stat.id);

        if (element) {
            animateValue(element,
                parseFloat(element.textContent.replace(/[^0-9.]/g, '')),
                value,
                1000,
                stat.prefix,
                stat.suffix
            );
        }
    });
}

// Generate random statistics within range
function generateRandomStat(min, max) {
    return Math.random() * (max - min) + min;
}

// Price ticker initialization
async function initPriceTicker() {
    const coins = ['BTC', 'ETH', 'BNB', 'SOL', 'ADA'];
    const ticker = document.getElementById('price-ticker');

    try {
        const response = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin,solana,cardano&vs_currencies=usd&include_24hr_change=true');
        const data = await response.json();

        updateTicker(data);
    } catch (error) {
        console.error('Error fetching prices:', error);
    }
}

// Handle smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Header scroll behavior
let lastScroll = 0;
const header = document.querySelector('.header');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll <= 0) {
        header.classList.remove('scroll-up');
        return;
    }
    
    if (currentScroll > lastScroll && !header.classList.contains('scroll-down')) {
        // Scrolling down
        header.classList.remove('scroll-up');
        header.classList.add('scroll-down');
    } else if (currentScroll < lastScroll && header.classList.contains('scroll-down')) {
        // Scrolling up
        header.classList.remove('scroll-down');
        header.classList.add('scroll-up');
    }
    
    lastScroll = currentScroll;
});

// Mobile menu functionality
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navList = document.querySelector('.nav-list');

if (mobileMenuBtn && navList) {
    mobileMenuBtn.addEventListener('click', () => {
        mobileMenuBtn.classList.toggle('active');
        navList.classList.toggle('active');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!mobileMenuBtn.contains(e.target) && !navList.contains(e.target)) {
            mobileMenuBtn.classList.remove('active');
            navList.classList.remove('active');
        }
    });

    // Close mobile menu when clicking on a link
    navList.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenuBtn.classList.remove('active');
            navList.classList.remove('active');
        });
    });
}

// Form validation
const trialForm = document.getElementById('trial-form');
if (trialForm) {
    trialForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = trialForm.querySelector('input[type="email"]').value;
        if (validateEmail(email)) {
            showNotification('Success! Check your email to get started.', 'success');
        } else {
            showNotification('Please enter a valid email address.', 'error');
        }
    });
}

function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function showNotification(message, type) {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 3000);
}

function animateCounter(element, start, end, duration, prefix = '', suffix = '') {
    const startTime = performance.now();
    const range = end - start;

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        const value = start + (range * progress);
        element.textContent = `${prefix}${Math.round(value)}${suffix}`;

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    requestAnimationFrame(update);
}

function initCounters() {
    const counters = document.querySelectorAll('.counter');
    
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const prefix = counter.getAttribute('data-prefix') || '';
        const suffix = counter.getAttribute('data-suffix') || '';
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(counter, 0, target, 2000, prefix, suffix);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        observer.observe(counter);
    });
}

document.addEventListener('DOMContentLoaded', initCounters);