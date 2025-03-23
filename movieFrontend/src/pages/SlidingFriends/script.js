document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".left-arrow").addEventListener("click", function() {
        alert("Previous movie clicked!");
    });

    document.querySelector(".right-arrow").addEventListener("click", function() {
        alert("Next movie clicked!");
    });
});
