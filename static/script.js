let timer;
let isRunning = false;
let elapsedTime = 0;
let totalTime = 0;
const basePrice = 5; // Base price in Rs
const costPerSecond = 0.01; // Cost per second in Rs

const display = document.getElementById('display');
const startStopBtn = document.getElementById('startStopBtn');
const resetBtn = document.getElementById('resetBtn');
const totalTimeDisplay = document.getElementById('totalTime');
const priceDisplay = document.getElementById('priceDisplay');

function formatTime(time) {
    let hours = Math.floor(time / 3600);
    let minutes = Math.floor((time % 3600) / 60);
    let seconds = time % 60;

    if (hours < 10) hours = '0' + hours;
    if (minutes < 10) minutes = '0' + minutes;
    if (seconds < 10) seconds = '0' + seconds;

    return `${hours}:${minutes}:${seconds}`;
}

function calculatePrice(seconds) {
    return basePrice + (seconds * costPerSecond);
}

function updateDisplay() {
    display.textContent = formatTime(elapsedTime);
}

function showTotalTimeAndPrice() {
    totalTimeDisplay.textContent = totalTime;
    priceDisplay.textContent = `Total price: ${calculatePrice(totalTime).toFixed(2)} Rs`;
    totalTimeDisplay.style.display = 'block';
    priceDisplay.style.display = 'block';
}

function hideTotalTimeAndPrice() {
    totalTimeDisplay.style.display = 'none';
    priceDisplay.style.display = 'none';
}

function startStop() {
    if (isRunning) {
        clearInterval(timer);
        isRunning = false;
        startStopBtn.textContent = 'Start';
        showTotalTimeAndPrice();
    } else {
        timer = setInterval(() => {
            elapsedTime++;
            totalTime++;
            updateDisplay();
        }, 1000);
        isRunning = true;
        startStopBtn.textContent = 'Stop';
        hideTotalTimeAndPrice();
    }
}

function reset() {
    clearInterval(timer);
    isRunning = false;
    elapsedTime = 0;
    totalTime = 0;
    updateDisplay();
    hideTotalTimeAndPrice();
    startStopBtn.textContent = 'Start';
}

document.addEventListener('DOMContentLoaded', () => {
    if (startStopBtn) {
        startStopBtn.addEventListener('click', startStop);
    }
    if (resetBtn) {
        resetBtn.addEventListener('click', reset);
    }
    // Automatically start the timer if the element exists and number plate is detected
    if (document.querySelector('.stopwatch')) {
        startStop(); // Automatically start the timer if the number plate exists
    }
});

// Initial display update
updateDisplay();
hideTotalTimeAndPrice();
