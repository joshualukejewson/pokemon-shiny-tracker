const encounterButton = document.getElementById("encounter-button");
const decrementButton = document.getElementById("decrement-button");
const encounterCount = document.getElementById("encounters-count");
const resetButton = document.getElementById("reset-button");
let count = 0;

encounterButton.addEventListener("click", function() {
    encounterCount.innerHTML = ++count;
});
decrementButton.addEventListener("click", function() {
    if (count > 0) {
    encounterCount.innerHTML = --count;
    }
});

resetButton.addEventListener("click", function () {
    encounterCount.innerHTML = count = 0;
})