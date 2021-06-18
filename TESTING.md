<h1 align="center">Brew Exchange</h1>
[View the deployed site here.](https://ms3-brew-exchange.herokuapp.com/)

[Main README.md file](https://github.com/adowlin/project-3-brew-exchange/blob/master/README.md)
[Project Repository](https://github.com/adowlin/project-3-brew-exchange)

## Testing
### Testing User Stories from User Experience (UX) Section

As a first-time visitor, I want to;
- See coffee recipes that other users have added:
    - On the landing page, the "Search Recipes" button is immediately visible.
    - After scrolling down the homepage, recipes added by other users are visible.
    - On all pages, the "All Recipes" button is visible in the Navbar.
    - Recipe cards on the "All Recipes" page cleanly display the recipe information.
- Search for recipes by keywords:
    - On the landing page, the "Search Recipes" button is immediately visible, and can be clicked to jump to the "Search" section of the page.
    - After scrolling down the landing page, the "Search" functionality is visible.
    - The search bar can be used to search for recipes via the input of a keyword & clicking the "Search" button.
    - Current search results can be cleared to re-populate all recipes by clicking the "Clear" button".
- Register an account to add my own recipes:
    - The "Register" button is immediately visible on the landing page.
    - On all pages, a "Register" button is visible in the Navbar.
    - On the "Register" page, users are prompted to register an account by creating a unique username and password via a registration form.
    - After registering an account, the user is logged in & redirected to their Profile, where the "Add Recipe" button is visible.

As a returning visitor, I want to:
- See coffee recipes added by other users:
    - On the landing page, the "Search Recipes" button is immediately visible.
    - After scrolling down the homepage, recipes added by other users are visible.
    - On all pages, the "All Recipes" button is visible in the Navbar.
    - Recipe cards on the "All Recipes" page cleanly display the recipe information.
- Search for recipes by keyword:
    - On the landing page, the "Search Recipes" button is immediately visible, and can be clicked to jump to the "Search" section of the page.
    - After scrolling down the landing page, the "Search" functionality is visible.
    - The search bar can be used to search for recipes via the input of a keyword & clicking the "Search" button.
    - Current search results can be cleared to re-populate all recipes by clicking the "Clear" button".
- Login to my account to see recipes I have added:
    - The "Log In" button is immediately visible on the landing page.
    - On all pages, a "Log In" button is visible in the Navbar.
    - On the Login page, users are prompted to log in to their account with their username and password.
    - After logging in, the user is redirected to their Profile, where all recipes that they have added are visible.
- Edit recipes that I have added:
    - On the user's Profile page, all recipes that they have added include an Edit icon, a button that opens the "Edit Recipe" page when clicked.
    - On the Edit Recipe page, a form is presented to the user, pre-filled with the current recipe information.
    - The user can edit the pre-filled information, and click the "Save" button. They are redirected to their profile, with a flash message confirming that the recipe has been updated.
    - On the All Recipes/Home page, a conditional check is implemented to populate the above described Edit button only on recipes that the current user has added.
- Delete recipes that I have added:
    - On the user's Profile page, all recipes that they have added include a Delete icon, a button that opens the "Delete Recipe" modal when clicked.
    - On the Delete Recipe modal, the user is presented with a message prompting them to confirm that they wish to delete the recipe.
    - The user can confirm that they want to delete the recipe by clicking the modal's "Delete" button. They are directed back to their Profile page, and a flash message is populated confirming that the recipe has been deleted.
    - On the All Recipes/Home page, a conditional check is implemented to populate the above described Delete button only on recipes that the current user has added.
- Contact the site owner/admin to request the addition of new brew methods:
    - On all site pages, the "Contact" link is visible in the site's Footer.
    - On the Add Recipe & Edit Recipe pages, a link to the Contact page is visible above the form elements. This prompts users to contact the site owner if they would like a brew method to be added to the list.

As the site owner, I want to:
- Login to my admin/superuser account:
    - On the Login page, if an admin account exists, the admin can log in to their admin/superuser account with the username "admin" & their existing password.
- Add brew method categories for users to choose from when creating recipes:
    - While logged in as the "admin" user, the "Manage Methods" button is visible on the landing page.
    - While logged in as the "admin" user, the "Manage Brew Methods" button is visible on all site pages in the Navbar.
    - On the Manage Brew Methods page, the admin is presented with a list of currently added brew methods from the MongoDB database. 
    - On the Manage Brew Methods page, the "Add Brew Method" button is immediately visible. When clicked, this button opens the "Add Brew Method" page.
    - On the Add Brew Method page, the admin is presented with a form which prompts them to enter the name of the brew method, and a URL for an image of the brew method.
    - After saving the brew method, the admin is redirected to the Manage Brew Methods page, with a flash message shown to confirm that the brew method has been added.
- Delete brew method categories:
    - On the Manage Brew Methods page, all brew method cards include a Delete icon, a button that opens the "Delete Brew Method" modal when clicked.
    - On the Delete Brew Method modal, the admin is presented with a message prompting them to confirm that they wish to delete the brew method.
    - The admin can confirm that they want to delete the brew method by clicking the modal's "Delete" button. They are directed back to the Manage Brew Methods page, with a flash message populated confirming that the brew method has been deleted.
- Edit or delete all recipes that have been added by any user on the site, to moderate the site's content:
    - On the All Recipes/Home page, a conditional check is in place to populate the edit and delete buttons on all recipes, if the current user is "admin".

### Manual Testing
#### All Pages
Manual testing was performed on the following elements that appear across all pages on the site, to ensure that all are working as expected;

- Navbar:
    - Clicking the site logo in the navbar correctly directs back to the site's home page.
    - All navigation links direct the user to the correct site page for each link.
    - Collapsible sidebar button opens the sidebar navigation element on mobile devices.
    - All navigation links within the collapsible sidebar correctly direct the user to the corresponding site page.
    - Hovering over the navigation links triggers the expected hover effect color.
    - Login & Register navigation links only appear when the user is unauthenticated, and correctly direct to their respective pages.
    - Profile and Logout navigation links correctly appear only when a user is already logged in, and correctly direct to the Profile page, and log the user out, respectively.
    - Manage Brew Methods navigation link appears only when the "admin" user is logged in, and correctly directs to the Brew Methods page.
- Footer:
    - External links open the correct external site in a new tab.
    - Contact link directs to the internal Contact page correctly.
    - Hovering over the footer links triggers the expected hover effect color.

#### Recipes Page (Home Page)
Manual testing was performed on the following elements that appear on the Recipes/Home page;

- Hero Section:
    - Hero image is appropriately responsive across all device sizes.
    - Search Recipes button triggers page scroll to search section when clicked.
    - Login & Register buttons only appear when the user is unauthenticated, and correctly direct to their respective pages.
    - Profile button correctly appears only when a user is already logged in, and correctly directs to the Profile page.
    - Manage Brew Methods button appears only when the "admin" user is logged in, and correctly directs to the Brew Methods page.
    - Hovering over the button in this section correctly triggers the expected hover effect background color.
- Search Section:
    - Search functionality validates whitespace and min/max input lengths.
    - An error message is surfaced when an incomplete search term is entered, or no database documents match the search term.
    - Page automatically scrolls back to search results after a search is performed.
    - Clear button reloads the page to clear search terms & re-populate all recipe cards.
- Recipe Cards:
    - Recipe info is correctly iterated over to create a card for each recipe.
    - Edit & Delete buttons only appear for authenticated users, and only on recipes that match the current user.
    - Edit & Delete buttons correctly appear on all recipes for the "admin" superuser, only when the current username is "admin", and the admin is logged in.

#### Register Page
Manual testing was performed on the following elements that appear on the Registration page:

- "Log In Here" link correctly directs to the login page for users who already have an account.
- Username input validates that the input value does not match an existing username.
- Username & password inputs validate whitespace, minlength, maxlength, and required patterns.
- Register button hover effect is applied as expected.
- The Register button correctly triggers a User document to be created in the MongoDB database.
- After successful registration, the user is automatically logged in and directed to their profile page, with a flash message populated to confirm that their registration was successful.
- Defensive programming works as expected - an authenticated user who tries to brute-force access the register page is redirected back to their profile page, with a flash message populated to let the user know that they already have an account.

#### Login Page
Manual testing was performed on the following elements that appear on the Login page:

- "Register Here" link correctly directs to the Register page for users who are not yet registered.
- Login form inputs validate whitespace, minlength, maxlength, and required patterns.
- Login functionality correctly performs validation checks to ensure that the username exists, and that the password is correct for that user.
- Register button hover effect is applied as expected.
- An error message is displayed if the username does not exist, or if the user's password is incorrect.
- After successfully logging in, the user is directed to their profile page, with a flash message to confirm that they are logged in.
- Defensive programming works as expected - an authenticated user who tries to brute-force access the login page is redirected back to their profile page, with a flash message populated to let the user know that they are already logged in.

#### Profile Page
Manual testing was performed on the following aspects of the Profile page:

- After logging in, a flash message displays the correct user name to confirm that the login was successful.
- The "Add Recipe" button appears as expected, and it's hover effect works as expected.
- The "Add Recipe" button correctly directs to the Add Recipe page.
- If a user has not yet added any recipes, a message is displayed to let them know that they have not added any recipes yet.
- If a user has added recipes, only the recipes where the user matches the current user's username are displayed.
- If an unauthenticated user tries to brute-force access a profile page, they are redirected to the login page, with a flash message stating that they cannot access that page.
- If an authenticated user tries to brute-force access another user's profile page, they are redirected back to their own profile page, with a flash message informing them of the error.

#### Add & Edit Recipe Pages
Manual testing was performed on the following aspects of the Add Recipe & Edit Recipe pages:

- When adding or editing a recipe, the form correctly populates lists for brew methods, roast levels, and grind sizes, in the dropdown menus.
- When adding or editing a recipe, the number input fields validate that a number has been entered.
- When adding or editing a recipe, the form validates whitespace values.
- When editing a recipe, the form correctly pre-populates the existing values for each field of the existing recipe.
- The "Contact Us" link directs to the Contact page correctly.
- The "Cancel" button correctly redirects back to the user's profile without submitting the form.
- If an unauthenticated user tries to brute-force access the Add or Edit recipe pages, they are redirected to the login page.
- If an authenticated user tries to brute-force access the Edit recipe page for a recipe that they did not create, they are redirected back to their own profile.
- If the "admin" superuser tries to brute-force access the Edit recipe page for any recipe regardless of the creator, they are correctly allowed to access the page & edit the recipe.

#### Deleting A Recipe

- When deleting a recipe, defensive programming works as expected - prompting the user to either confirm or cancel the deletion action via a modal.
- If an unauthenticated user tries to brute-force access to the delete recipe page, they are redirected to the login page.
- If a user tries to brute-force delete a recipe that was not created by them, they are redirected to their own profile.
- An admin can brute-force delete any recipe as expected.

#### Manage Brew Methods Page (ADMIN)

- "Add Brew Method" button is visible, correctly directs to the Add Brew Method page, and it's hover effect triggers as expected.
- Brew methods list is correctly iterated over to create a card for each brew method. 
- Brew method images display appropriately within the corresponding card.
- If an unauthenticated user tries to brute-force access to the Manage Brew Methods page, they are redirected to the login page.
- If a user with a username that is not "admin" tries to brute-force access to the page, they are redirected to their own profile.

#### Add Brew Method (ADMIN)

- Form validates whitespace in brew method name.
- Form validates that a URL has been input for the brew method image.
- Save button correctly triggers functionality to add brew method to database, and after successfully adding a brew method, directs the admin back to the Manage Brew Methods page with a success message populated.
- Cancel button directs back to Manage Brew Methods page as expected.
- Both the Save and Cancel buttons' hover effects trigger as expected.
- If an unauthenticated user tries to brute-force access to the Add Brew Method page, they are redirected to the login page.
- If a user with a username that is not "admin" tries to brute-force access to the page, they are redirected to their own profile.

#### Delete Brew Method (ADMIN)

- Defensive programming works as expected. When an admin tries to delete a recipe, they are prompted to confirm or cancel the deletion action via a modal.
- If an unauthenticated user tries to brute-force delete a brew method, they are redirected to the login page.
- If a user with a username that is not "admin" tries to brute-force delete a brew method, they are redirected to their own profile.

#### Contact Page

- Username value correctly pre-populates the current user's username if a user is in session.
- Form asks the user to input their name if the user is not currently logged in.
- Form inputs validate whitespace & email address format.
- Submit button correctly triggers the EmailJS function, and the hover effect triggers as expected.
- After successful form submission, a custom confirmation message is displayed.
- If the EmailJS functionality returns an error, a message to reflect this is displayed to the user.

### Compatibility & Responsiveness
The site was tested across multiple browsers and device types, with no cross-browser compatibility issues to note.

- Browsers tested:
    - Chrome (Windows, macOS, iOS, Android)
    - Safari (macOS, iOS)
    - Microsoft Edge (Windows, macOS)
    - Firefox (Windows, macOS)
    - Samsung Browser (Android)
- Devices tested:
    - iPhone XS
    - Samsung Galaxy Edge
    - Desktop PC
    - Laptop
    - Tablet

The site was found to be fully responsive on device sizes ranging from 320px X 480px to 1920px X 1080px.

### Validation
#### HTML
- [W3C HTML Validator](https://validator.w3.org/nu/) was used to validate the HTML on all pages of the site. This validator does not recognise Jinja templates & scripting, so returns errors for the lines of code where Jinja is used - this is to be expected. No errors are present in the HTML code otherwise.

#### CSS
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code in the style.css file. No errors are present.

#### JavaScript
- [JSHint](https://jshint.com/) was used to validate the JavaScript code in the script.js file. No errors are present.
- [Esprima](https://esprima.org/demo/validate.html) was also used to validate the JavaScript syntax. Returned result: "Code is syntactically valid".

#### Python
- [PEP8 Online](http://pep8online.com/) was used to validate that the Python code in app.py is PEP8 compliant. No errors are present.