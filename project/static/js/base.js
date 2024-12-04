document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector(".nav_toggle");
    const navBottom = document.querySelector(".nav_bottom");

    toggleButton.addEventListener("click", function () {
        navBottom.classList.toggle("active");
    });
});
