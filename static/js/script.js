$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();

    // JS for sticky Navbar adapted from example here: https://www.w3schools.com/howto/howto_js_navbar_sticky.asp
    // When the user scrolls the page, execute myFunction
    window.onscroll = function () {
        myFunction()
    };

    // Get the navbar & H2 element below it
    var navbar = document.getElementById("nav_bar");
    var searchHeader = document.getElementById("search-header");

    // Get the offset position of the navbar
    var sticky = navbar.offsetTop;

    // Add the "sticky" class to the navbar & "content" class to the header when you reach nav scroll position.
    // Remove "sticky" & "content" when you leave the nav scroll position
    function myFunction() {
        if (window.pageYOffset >= sticky) {
            navbar.classList.add("sticky")
            searchHeader.classList.add("content");
        } else {
            navbar.classList.remove("sticky");
            searchHeader.classList.remove("content");
        }
    }
});