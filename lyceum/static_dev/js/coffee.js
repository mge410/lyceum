document.addEventListener("DOMContentLoaded", function() {
    const coffeeBtn = document.getElementById("coffee_count")
    const coffeeCountElem = document.getElementById("id_coffee_count")

    coffeeBtn.addEventListener('click', function () {
        coffeeCountElem.value ++
    });

})