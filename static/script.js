let timer;
let isRunning = false;
let elapsedTime = 0;
let totalTime = 0;
const basePrice = 5; // Base price in Rs
const costPerSecond = 0.01; // Cost per second in Rs

document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');
    const stopBtn = document.getElementById('stopBtn');
    const totalTimeDisplay = document.getElementById('totalTime');
    const priceDisplay = document.getElementById('priceDisplay');
    const continueBtn = document.getElementById('continueBtn');
    const thankYouMessage = document.getElementById('thankYouMessage');
    const deductedAmount = document.getElementById('deductedAmount');

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
        const price = calculatePrice(totalTime).toFixed(2);
        priceDisplay.textContent = `Total price: ${price} Rs`;
        deductedAmount.textContent = price; // Set the amount for thank you message
        totalTimeDisplay.style.display = 'block';
        priceDisplay.style.display = 'block';
        continueBtn.style.display = 'inline-block'; // Show continue button
    }

    function hideTotalTimeAndPrice() {
        totalTimeDisplay.style.display = 'none';
        priceDisplay.style.display = 'none';
        continueBtn.style.display = 'none'; // Hide continue button
    }

    function startTimer() {
        timer = setInterval(() => {
            elapsedTime++;
            totalTime++;
            updateDisplay();
        }, 1000);
        isRunning = true;
        hideTotalTimeAndPrice();
    }

    function stopTimer() {
        clearInterval(timer);
        isRunning = false;
        showTotalTimeAndPrice();
    }

    function continueProcess() {
        thankYouMessage.style.display = 'block';
        document.querySelector('.stopwatch').style.display = 'none'; // Hide stopwatch after continue
    }

    if (stopBtn) {
        stopBtn.addEventListener('click', stopTimer);
    }
    if (continueBtn) {
        continueBtn.addEventListener('click', continueProcess);
    }
    // Automatically start the timer if the stopwatch element exists
    if (document.querySelector('.stopwatch')) {
        startTimer(); // Automatically start the timer if the number plate exists
    }

    // Initial display update
    updateDisplay();
    hideTotalTimeAndPrice();
});
