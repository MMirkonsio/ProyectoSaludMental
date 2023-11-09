document.addEventListener("DOMContentLoaded", function() {
    const navbarToggle = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navbarToggle.addEventListener("click", function() {
        navbarCollapse.classList.toggle("show");
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const searchMessage = document.getElementById("searchMessage");

    searchInput.addEventListener("input", function() {
        const searchTerm = searchInput.value.toLowerCase();

        if (searchTerm === "") {
            searchMessage.style.display = "none";
        } else {
            searchMessage.style.display = "block";
            searchMessage.textContent = "No se encontraron resultados";
        }
    });

    const profileLink = document.querySelector(".navbar-nav .dropdown-toggle");
    const profileMenu = document.querySelector(".dropdown-menu");

    profileLink.addEventListener("click", function(event) {
        event.preventDefault();
        profileMenu.classList.toggle("show");
    });

    window.addEventListener("click", function(event) {
        if (event.target !== profileLink && !profileMenu.contains(event.target)) {
            profileMenu.classList.remove("show");
        }
    });
});


document.addEventListener("DOMContentLoaded", function(){
    const nuevaPublicacionBtn = document.getElementById('nueva-publicacion-btn');
    const nuevaPublicacionModal = new mdb.Modal(document.getElementById('nueva-publicacion-modal'));

    nuevaPublicacionBtn.addEventListener('click', () => {
    nuevaPublicacionModal.show();
});

});

