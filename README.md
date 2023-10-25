![Lyfetree Logo](./static/img/logo.png)
# Lyfetree
This is the "Lyfetree" repository - an app that allows you to document personal achievements and "skills" - so-called "milestones" - in a family tree-like structure.
this project is a free time activity of me and my colleagues, which is why CI/CD is not planned for the time being.

Note: The latest version of the project can be found under the branch "dev/v1" - in main no pulls will be done before finishing development on the first version.
## UX
No user experience requirements have been set yet.
### User Stories
No user stories have been created.
### Design
No design requirements have been set.
## Features
No explicit features have been requested/deployed.
## Technologies Used
- [django](https://www.djangoproject.com)
    - The project uses the **django** web framework as a base.

- [Python](https://www.python.org)
    - The project uses **Python** based on the django framework to serve functionality of the app.

- [SQLite](https://www.sqlite.org/index.html)
    - The project uses **SQLite** for databases.

- [HTML](https://www.w3.org/)
    - The project uses **HTML** to create pages inside the django project.

- [CSS](https://www.w3.org/)
    - The project uses **CSS** to style the application.
## Testing
No tests have been applied.
## Deployment
To be done.
## Installation
For this installation guide it is assumed you have already installed Python and the packaging tool ```pipenv``` on your local machine.
You can install the tool via ```pip install pipenv``` in your command line after installing the latest Python version.

How to install and run the "Lyfetree" app on a local server/machine via a repository:
1. Fork/clone the repository.
2. Open the terminal and cd into the local repository folder.
3. In the repository, create a file called ".env" in the root folder of the repository for enviromental variables and generate a secret key (you can use whatever generator you like or type in any prefered combination of letters, numbers and symbols - but keep it strong, safe and secret)
4. Crate local variables by pasting the following lines in your .env file (where everything in quotation marks hast to be replaced with the actual value):
```bash
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.sqlite3
DB_NAME="yourdatabasename".db # database name does not matter
DB_USER="yourusername" # value doesn't matter in local development environment
DB_PASSWORD="yourpassword" # value doesn't matter in local development environment
DB_HOST=localhost
DB_PORT="yourport" # can be left out for default port
SECRET_KEY="yoursecretkeygoeshere" # value doesn't matter in local development environment
```
5. Now that security is set up, you can create the local enviroment. Type ```pipenv install``` 
to install the enviroment and all dependencies.
6. Now that the local enviroment is set up, the database can be migrated via 
```bash
pipenv run python manage.py makemigrations
``` 
and 
```bash
pipenv run python manage.py migrate
```
8. Run the local server enviroment via 
```bash
pipenv run python manage.py runserver
```
9. Click on the local server IP given in the terminal to open the app.
8. Have fun playing around!
## Credits
Credits to @CevikKubat and @JapahaPapaya for actively contributing to this project and working things out together.