<h1 align="center">Brew Exchange</h1>

[View the deployed site here.](https://ms3-brew-exchange.herokuapp.com/)

Brew Exchange is a website where users can share their coffee recipes with the specialty coffee community, and can access recipes from other members of the community. This website was created for submission as my Milestone Project 3 as part of the Diploma in Full Stack Software Development course with Code Institute.<br>

[<img src="readme-assets/images/brew-exchange-mockup.png" alt="responsive site mockups">](https://ms3-brew-exchange.herokuapp.com/)
 
## User Experience (UX)

With a large variety of brewing equipment, coffee varieties, and brewing methods, users can search for recipes that suit the coffee or brewing equipment that they have. This site advances the user's goals by providing CRUD functionality to the coffee recipes database. It advances the site owner's goals by being a regular user of the site themselves.

The User Experience for this site was planned & developed using the [5 Planes of UX Design](https://medium.com/designcentered/ux-design-5-planes-method-b1b1d6587c05): Strategy, Scope, Structure, Skeleton, Surface.

### Strategy
#### User Stories

- As a first-time visitor, I want to:
    - See coffee recipes that other users have added.
    - Search for recipes by keywords.
    - Register an account to add my own recipes.

- As a returning visitor, I want to:
    - See coffee recipes added by other users.
    - Search for recipes by keyword.
    - Login to my account to see recipes I have added.
    - Edit recipes that I have added.
    - Delete recipes that I have added.
    - Contact the site owner/admin to request the addition of new brew methods.

- As the site owner, I want to:
    - Log in to my admin/superuser account.
    - Add brew method categories for users to choose from when creating recipes.
    - Delete brew method categories.
    - Edit or delete all recipes that have been added by any user on the site, to moderate the site's content.

### Scope
#### Existing Features

- **Hero Image with Lead Text:**
    - The hero image serves the purpose of providing users with an immediate visual cue for the theme of the site - coffee. The Lead Text and call to action buttons concisely explain the site's purpose & demonstrate it's functionality.
- **Search Functionality:**
    - Allows users to search for specific types of recipes by keyword - available to both authenticated and unauthenticated users.
- **Register:**
    - Users can create an account on the site, in order to contribute to the site by adding their own coffee brewing recipes. The user input is validated, a new "user" document in the site's database is created, and hashing is used for password security.
- **Login/Logout:**
    - Adds authentication for registered users, allowing them to access, edit and delete their own recipes. Allows users to logout by clearing the "session" cookie.
- **Profile:**
    - Provides functionality for registered & logged in users to see the recipes that they've added (if any), add more recipes, edit or delete their existing recipes.
- **Add Recipe:**
    - Provides functionality for authenticated users to add their own recipes via a form.
- **Edit Recipe:**
    - Provides functionality for authenticated users to edit recipes that they've added. Extra checks are in place here to ensure the current user matches the username of the user who created the recipe.
- **Delete Recipe:**
    - Provides functionality for authenticated users to delete recipes that they've added. Extra authentication steps are also in place in this feature to ensure that the current username matches that of the recipe's creator.
- **Admin/Superuser Registration:**
    - This feature allows the site admin to register an account with the username "admin", granting access to edit and delete all recipes on the site for moderation purposes. The "admin" superuser is also granted access to additional site functionality to manage the brew methods that users can choose from when adding or editing recipes.
- **Manage Brew Methods (ADMIN):**
    - This section of the site allows the admin to view a list of the currently added brew methods, along with corresponding images of each brew method.
- **Add Brew Methods (ADMIN):**
    - Provides a form where the site admin can add new brew methods, and upload an image of the brew method.
    - It was decided to only allow images to be added in the form of an existing URL - due to the limitations for image support in the chosen database technology (MongoDB), and the additional development work that would be required to implement a third party image-to-URL solution. Because of these limitations, it was also decided to limit the use of images to the site admin only, to avoid misuse of the feature.
- **Delete Brew Methods (ADMIN):**
    - Provides functionality for the site admin to remove brew methods from the site.
- **Contact Page:**
    - Allows all users, authenticated or unauthenticated, to contact the site admin - for example, to ask the admin to add a new brew method to the list of options available in the "Add Recipe" form.

#### Future Planned Features
- **Affiliate Links:**
    - Would allow users to purchase brewing equipment of coffee beans used in specific recipes via affiliate links. Would additionally provide the admin/site owner with a means to generate income from the site via commissions.
- **"Like" Buttons:**
    - Would provide users with the option to "Like" recipes that they enjoy, and would save those recipes to a list that would be accessible from the user's Profile page.
- **Image Upload for All Users:**
    - Would provide an option for users to upload their own images to the site, to demonstrate how they would brew a particular recipe.

### Structure
#### Flowchart
- Flowchart created using [Lucidchart](https://www.lucidchart.com):<br>
    [Flowchart PNG](/readme-assets/images/brew-exchange-flowchart.png)

### Skeleton
#### Wireframes
- Wireframes created using [Balsamiq](https://balsamiq.com/):<br>
    [Wireframes PDF](/readme-assets/brew-exchange-wireframes.pdf)

### Surface

- Color Scheme:
    - Chosen using [coolors.co](https://coolors.co/). This palette was chosen to provide colors that tie in with the coffee theme of the site, and provide complimentary colors that offer sufficient contrasts to work with for accessibility purposes:<br>
    [<img src="readme-assets/images/brew-exchange-palette.png" alt="color palette" width="400"/>](https://coolors.co/eff2f1-880d1e-c4926e-57a773-3a3238)

- Typography:
    - The [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) font was chosen for the site's headers, and [Poppins](https://fonts.google.com/specimen/Poppins) was chosen for the site's main text.

- Images:
    - [Unsplash](https://unsplash.com/) was used to select the site's Hero Image<br>
    [<img src="static/images/hero-img.jpg" alt="coffee beans with cup" width="400"/>](https://unsplash.com/photos/Y6O6PHJRQms?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)

## Technologies Used

### Tools
- [GitPod](https://www.gitpod.io/)
    - Used as the preferred IDE for development.
- [Git](https://git-scm.com/)
    - Used via the Gitpod terminal for version control, with regular commits, and to push to GitHub & Heroku.
- [GitHub](https://github.com/)
    - Used to store the site's code repository.
- [Heroku](https://www.heroku.com/)
    - Used to host the deployed site.
- [Lucidchart](https://www.lucidchart.com)
    - To create the site's structural flowchart.
- [Balsamiq](https://balsamiq.com/)
    - To create the site's wireframes.
- [Google Fonts](https://fonts.google.com/)
    - Used to import the site's fonts.
- [TinyJPG](https://tinyjpg.com/)
    - Used to compress the site's hero image.

### Front-End Technologies
- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [JQuery 3.6.0](https://jquery.com/)
    - Used as the primary JavaScript library.
- [Materialize 1.0.0](https://materializecss.com/)
    - Used as a responsive front-end framework.
- [EmailJS](https://www.emailjs.com/)
    - Used to send emails to the site owner from the contact form.

### Back-End Technologies
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Used with Python as the primary web microframework.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - Used for creating templates with Flask.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
    - Used for password hashing & authentication on the site.
- [MongoDB Atlas](https://www.mongodb.com/)
    - Used to store the site's database.
- [PyMongo](https://pypi.org/project/pymongo/)
    - Used to interact with the MongoDB database from Python.

## Testing
Testing documentation can be found in a separate file [TESTING.md](https://github.com/adowlin/project-3-brew-exchange/blob/master/TESTING.md)

## Deployment
### Local Deployment

The following dependencies will need to be installed in order to run this application locally:
- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install app requirements.
- [GitPod](https://www.gitpod.io/) or any preferred IDE, such as [VSCode](https://code.visualstudio.com/).
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for cloning and version control.
- [MongoDB](https://www.mongodb.com/) to create a database using MongoDB Atlas.

Follow the below steps for local deployment:

1. Clone the GitHub repository by entering the following command into the Git terminal:
    - `git clone https://github.com/adowlin/project-3-brew-exchange.git`
2. After cloning the project, create an `env.py` file that includes the below code, replacing the `SECRET_KEY`, `MONGO_URI`, `MONGO_DBNAME` with your own credentials:
```
import os
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
os.environ.setdefault("MONGO_URI", "YOUR_MONGO_URI")
os.environ.setdefault("MONGO_DBNAME", "coffee_recipes")
```
3. Create a `.gitignore` file, and add the `env.py` file to the list of files.
4. Install all requirements from the [requirements.txt](https://github.com/adowlin/project-3-brew-exchange/blob/master/requirements.txt) file using this command:
    - `pip3 -r requirements.txt`
5. Sign up for a [MongoDB](https://www.mongodb.com) account, and create a new Database called `coffee_recipes`. The collections in that database should be structured as follows:

**brew_methods**
```
_id: <ObjectId>
method_name: <string>
image_url: <string>
```

**recipes**
```
_id: <ObjectId>
recipe_method: <string>
roast_level: <string>
grind_size: <string>
coffee_weight: <string>
water_weight: <string>
time_mins: <string>
time_secs: <string>
description: <string>
user: <string>
```

**users**
```
_id: <ObjectId>
username: <string>
password: <string>
```

6. Run the app using the following command in the terminal:
    - `python3 app.py`

### Remote Deployment

To deploy this app on Heroku, the following steps were taken:

1. Create a `requirements.txt` file so Heroku can install the required dependencies.
    - `pip3 freeze --local > requirements.txt`
    - This project's requirements.txt file can be seen [here](https://github.com/adowlin/project-3-brew-exchange/blob/master/requirements.txt).
2. Create a `Procfile` with information about the type of app that will be deployed.
    - `echo web: python app.py > Procfile`
    - This project's Procfile file can be seen [here](https://github.com/adowlin/project-3-brew-exchange/blob/master/Procfile).
    - Make sure to delete the blank line at the end of the Profile, as this can cause issues when deploying to Heroku later.
3. Create a Heroku account, create a project app, and click the "Deploy" tab. 
4. "Connect GitHub" as the Deployment Method, and select "Enable Automatic Deployment".
4. In the "Settings" tab, click the "Reveal Config Vars" button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **MONGO_DBNAME**: `coffee_recipes`
    - **MONGO_URI** : `<YOUR_MONGO_DB_URI>`
    - **PORT** : `5000`
    - **SECRET_KEY** : `<YOUR_SECRET_KEY>`
5. The app should now be deployed to Heroku - click the "Open App" button to view the deployed site.

## Credits

### Content
- CSS & JS for Sticky Navbar functionality adapted from [W3Schools Example](https://www.w3schools.com/howto/howto_js_navbar_sticky.asp).
- Search functionality adapted from Code Institute coursework mini project: https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/08-SearchingWithinTheDatabase/01-text_index_searching/static/js/script.js
- Authentication functionality for register, login functionality adapted from Code Institute coursework mini project: https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/08-SearchingWithinTheDatabase/01-text_index_searching/app.py
- Deployment section of README.md file adapted from: https://github.com/TravelTimN/ci-milestone04-dcd/blob/main/README.md#deployment

### Media
- [Techsini](http://techsini.com/multi-mockup/) was used to create the mockup image used in the README file.
- [favicon.io](https://favicon.io/) used to generate the site's favicon image.
- [Unsplash](https://unsplash.com/) was used for sourcing images of the site's brew methods:
    - Aeropress: https://unsplash.com/photos/kEfi-fySyoc
    - French Press: https://unsplash.com/photos/XItB_MGkUZw
    - Moka Pot: https://unsplash.com/photos/mn2tsPe6Oe8
    - V60: https://unsplash.com/photos/4LbLyYESbFE
    - Chemex: https://unsplash.com/photos/jE-27l7V3NU
    - Espresso: https://unsplash.com/photos/dvuHNTJxIsg
    - Kalita Wave: https://unsplash.com/photos/faS2GhY1fjE
    - Iced: https://unsplash.com/photos/BIeXZhg_7sw
    - Turkish: https://unsplash.com/photos/okZPXZmbokY

### Acknowledgements
- Spencer, my Code Institute mentor, for guidance and encouragement throughout the development of this project.
- Tim & Simen, Code Institute, for helpful tips and guidance in Masterclasses & group sessions.
- My family & friends, for their help in design choices & testing of the site.
