$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();

    // JS for sticky Navbar adapted from example here: https://www.w3schools.com/howto/howto_js_navbar_sticky.asp
    // When the user scrolls the page, execute myFunction
    window.onscroll = function () {
        stickyNav();
    };

    // Get the navbar & H2 element below it
    var navbar = document.getElementById("nav_bar");
    var pageHeader = document.getElementById("page-header");
    var flashMessage = document.getElementById("flash-section");

    // Get the offset position of the navbar
    var sticky = navbar.offsetTop;

    // Add the "sticky" class to the navbar & "content" class to the header when you reach nav scroll position.
    // Remove "sticky" & "content" when you leave the nav scroll position
    function stickyNav() {
        if (window.pageYOffset >= sticky) {
            navbar.classList.add("sticky");
            if (flashMessage) {
                flashMessage.classList.add("content");
            }
            else {
                pageHeader.classList.add("content");
            }
        } else {
            navbar.classList.remove("sticky");
            pageHeader.classList.remove("content");
            flashMessage.classList.remove("content");
        }
    }
});

function sendMail(contactForm) {
    // Validate that the message value is not only whitespace
    var x = document.forms.contactForm.contactMessage.value;
    if (x.trim() == null || x.trim() == "" || x === " ") {
        M.toast({html: "Message must contain letters or numbers", classes: 'search-toast'});
        return false;
    }
    else if (userName) {
        emailjs.send("service_6i30xfe","brew_8gvdejr", {
            "from_user": userName,
            "from_email": contactForm.contactEmail.value,
            "message": contactForm.contactMessage.value
        })
        .then(
            function(response) {
                console.log("SUCCESS", response);
                M.toast({html: "Your message has been sent! We'll get back to you as soon as possible.", classes: 'contact-toasts'});
            },
            function(error) {
                console.log("FAILED", error);
                M.toast({html: "Message failed to send. Please try again later", classes: "contact-toasts"});
            }
        );
    }
    else {
        emailjs.send("service_6i30xfe","brew_8gvdejr", {
            "from_name": contactForm.contactName.value,
            "from_email": contactForm.contactEmail.value,
            "message": contactForm.contactMessage.value
        })
        .then(
            function(response) {
                console.log("SUCCESS", response);
                M.toast({html: "Your message has been sent! We'll get back to you as soon as possible.", classes: 'contact-toasts'});
            },
            function(error) {
                console.log("FAILED", error);
                M.toast({html: "Message failed to send. Please try again later", classes: 'contact-toasts'});
            }
        );
    }

    document.contactForm.reset(); // clears the form data when submitted
    return false; // prevents page reload
}

// Function for whitespace validation adapted from: https://stackoverflow.com/questions/27543671/javascript-form-validation-not-empty-or-no-whitespaces
// Whitespace validation for Search
function validateFormSearch() {
    var x = document.forms.searchForm.query.value;
    if (x.trim() == null || x.trim() == "" || x === " ") {
        M.toast({html: "Search must contain letters or numbers", classes: 'search-toast'});
        return false;
    }
}

// Whitespace validation for Add/Edit Recipe Forms
function validateFormRecipe() {
    var x = document.forms.recipeForm.description.value;
    if (x.trim() == null || x.trim() == "" || x === " ") {
        M.toast({html: "Description must contain letters or numbers", classes: 'search-toast'});
        return false;
    }
}

// Whitespace validation for Add Brew Method Form
function validateFormBrewMethod() {
    var x = document.forms.brewMethodForm.brew_method.value;
    if (x.trim() == null || x.trim() == "" || x === " ") {
        M.toast({html: "Brew Method name must contain letters or numbers", classes: 'search-toast'});
        return false;
    }
}