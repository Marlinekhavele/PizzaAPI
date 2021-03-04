# PizzaAPI
##### Built with
- Python version 3
- Django
- Djangorestframework
##### Running the project locally
- Clone the project using git clone
- Enter the project directory i.e
cd base
- create virtual environment
- virtualenv env -p python3.6
##### activate
source env/bin/activate
##### install deps
- pip install -r requirements.txt
- python manage.py createsuperuser
- python manage.py makemigrations
- python manage.py migrate
##### Start the project with the command
- python manage.py runserver
##### Endpoints documentation
- Visit http://localhost:8000/api/v1/docs to get started with the browsable api
##### Running Tests
- python manage.py test
