$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();

    // JS for sticky Navbar adapted from example here: https://www.w3schools.com/howto/howto_js_navbar_sticky.asp
    // When the user scrolls the page, execute myFunction
    window.onscroll = function () {
        stickyNav()
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
    if (userName) {
        emailjs.send("service_6i30xfe","brew_8gvdejr", {
            "from_user": userName,
            "from_email": contactForm.contactEmail.value,
            "message": contactForm.contactMessage.value
        })
        .then(
            function(response) {
                console.log("SUCCESS", response);
                alert("Your message has been sent! We'll get back to you as soon as possible.");
            },
            function(error) {
                console.log("FAILED", error);
                alert("Message failed to send. Please try again later");
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
                alert("Your message has been sent! We'll get back to you as soon as possible.");
            },
            function(error) {
                console.log("FAILED", error);
                alert("Message failed to send. Please try again later");
            }
        );
    };

    document.contactForm.reset(); // clears the form data when submitted
    return false; // prevents page reload
}