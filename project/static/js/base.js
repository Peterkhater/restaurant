document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.querySelector(".nav_toggle");
    const navBottom = document.querySelector(".nav_bottom");

    toggleButton.addEventListener("click", function () {
        navBottom.classList.toggle("active");
    });
});


document.addEventListener("DOMContentLoaded", () => {
    const preloader = document.querySelector('.pl'); 
    const navContainer = document.querySelector('.nav_container');
    const mainContentContainer = document.querySelector('.allContent');
    
    // Hide nav and content while loading
    navContainer.style.opacity = '0';
    mainContentContainer.style.opacity = '0';

    window.addEventListener('load', () => {
        
        preloader.style.transition = 'opacity 0.5s ease';
        preloader.style.opacity = '0';

        
        navContainer.style.transition = 'opacity 0.5s ease';
        mainContentContainer.style.transition = 'opacity 0.5s ease';
        
        navContainer.style.opacity = '1';
        mainContentContainer.style.opacity = '1';

        setTimeout(() => {
            preloader.style.display = 'none'; // Hide preloader after fade-out
        }, 500); // Duration matches the fade-out transition
    });
});

