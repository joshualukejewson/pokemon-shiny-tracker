const encounterButton = document.getElementById("encounter-button");
const encounterCount = document.getElementById("encounters-count");
const resetButton = document.getElementById("reset-button");
let count = 0;

encounterButton.addEventListener("click", function() {
    encounterCount.innerHTML = ++count;
});

resetButton.addEventListener("click", function () {
    encounterCount.innerHTML = count = 0;
})