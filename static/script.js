const encounterButton = document.getElementById("encounter-button");
const encounterCount = document.getElementById("encounters-count");
let count = 0;

encounterButton.addEventListener("click", function() {
    encounterCount.innerHTML = ++count;
});

const resetButton = document.getElementById("reset-button");

resetButton.addEventListener("click", function () {
    encounterCount.innerHTML = count = 0;
})