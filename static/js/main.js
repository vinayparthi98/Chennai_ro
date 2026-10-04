/* =========================================================
   CHENNAI RO INNOVATION
   MAIN JAVASCRIPT
========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    console.log("Chennai RO Innovation JavaScript loaded.");

    /* =====================================================
       PRODUCT SEARCH
    ===================================================== */

    const searchInput = document.querySelector("#product-search");

    if (searchInput) {

        searchInput.addEventListener("input", function () {

            const searchText =
                searchInput.value.trim().toLowerCase();

            const cards =
                document.querySelectorAll(".product-card");

            cards.forEach(function (card) {

                const text =
                    card.textContent.toLowerCase();

                if (text.includes(searchText)) {

                    card.style.display = "";

                } else {

                    card.style.display = "none";

                }

            });

        });

    }


    /* =====================================================
       MOBILE MENU
    ===================================================== */

    const menuButton =
        document.querySelector("#menu-toggle");

    const navLinks =
        document.querySelector(".nav-links");

    if (menuButton && navLinks) {

        menuButton.addEventListener("click", function () {

            navLinks.classList.toggle("show");

        });

    }


    /* =====================================================
       CART COUNT
       
       This reads the number supplied by Flask.
       It does NOT create a separate localStorage cart.
    ===================================================== */

    const cartCount =
        document.querySelector(".cart-count");

    if (cartCount) {

        const currentCount =
            Number(cartCount.textContent) || 0;

        cartCount.textContent = currentCount;

    }


    /* =====================================================
       CLOSE MOBILE MENU WHEN LINK IS CLICKED
    ===================================================== */

    if (navLinks) {

        const links =
            navLinks.querySelectorAll("a");

        links.forEach(function (link) {

            link.addEventListener("click", function () {

                navLinks.classList.remove("show");

            });

        });

    }

});