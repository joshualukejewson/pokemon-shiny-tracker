const encounterButton = document.querySelector("[name='encounter-button']");
const encounterCount = document.getElementById("encounters-count");
let count = 0;

encounterButton.addEventListener("click", function() {
    encounterCount.innerHTML = ++count;
});
