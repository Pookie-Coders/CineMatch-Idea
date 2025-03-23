document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".card").forEach(card => {
        card.addEventListener("click", function() {
            alert(`You clicked on "${this.querySelector(".card-text").textContent}"`);
        });
    });
});
