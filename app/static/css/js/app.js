document.addEventListener("DOMContentLoaded", function () {

    console.log("PocketSmart AI loaded successfully.");

    // Mobile menu
    const menuButton = document.querySelector(".menu-button");
    const navLinks = document.querySelector(".nav-links");

    if (menuButton && navLinks) {
        menuButton.addEventListener("click", function () {
            navLinks.classList.toggle("active");
        });
    }

    // Form submit loading
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function () {

            const button = form.querySelector(
                "button[type='submit']"
            );

            if (button) {
                button.disabled = true;
                button.textContent = "Processing...";
            }
        });
    });

    // Hide alerts automatically
    const messages = document.querySelectorAll(".alert");

    messages.forEach(function (message) {
        setTimeout(function () {
            message.style.display = "none";
        }, 5000);
    });

});






