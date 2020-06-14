# Dallas Food Nerd Deal Finder - Python/Django Api

# Description

DallasFoodNerd.com is a localized food blog focused on providing users insight into local restaurants and various other food related experiences. The Deal Finder application will expand the existing presence to offer users the ability to filter from a custom database of deals, special offers, and limited time events at local eateries to assist in choosing/planning their next outing.

# Deployed Applications

- Backend - https://dfndealfinderdjango.herokuapp.com/specials
- Frontend - https://dfndealfinderreact.herokuapp.com/specials

# Github Repositories

- Backend - https://github.com/roryellis/dfndealfinder_api
- Frontend - https://github.com/roryellis/dfndealfinder_react

# Technologies Used

- Python 3.8
- Django
- Django REST Framework
- AWS S3/boto3/django-storages - For file upload/storage
- Postgresql database

# Getting Started

- If you wish to run this application locally, or make edits to it, you can find instructions for forking and cloning the repository here. https://help.github.com/en/github/getting-started-with-github/fork-a-repo
- You will also need to run a local postgresql database
- Install dependencies in your cloned directory with `pipenv install`
- Create a .env file in the root directory with variables SECRET_KEY, DATABASE_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, MODE='dev'
- Create your superuser account with `$ python manage.py createsuperuser`
- Run the application with `$ python3 manage.py runserver`
- Record creation is handled through Django Admin console at /admin.

# Supported Endpoints

- Specials
  - /specials - Retrieve all special objects from database
    - '/:id' - Retrieve, Update, Delete special by id. 
- Restaurants
  - /restaurants - Retrieve all restaurant objects from database
  - '/:id' - Retrieve, Update, Delete restaurant by id. 

# Contribution

- This is a student project presented for evaluation and is not open for outside contributions at this time.