# Stocksgram - Product Stocks Management System

**This application is originally created by MD INZAMUL HAQUE for INFORTECH Solutions.** It is then futher modifiy by Tom Mong for stocksgram. <br>

##### Framework: Django 3.1.7 (Updated to 3.1.8, 5 May 2021)
##### Language : Python 3.8

## Usage

1. Git the current repository `git https://github.com/asd65241/stocksgram-django.git`
2. Go to the folder `cd stocksgram-django`
3. Initiate the Python VirtualEnv by `pipenv shell`
4. Install Python required packages `pip -r requirements.txt`
5. Run Django Server `python manage.py runserver 0.0.0.0:8000`
6. View the Website `http://localhost:8000/`

The app will automatically reload if you change any of the source files.

## Deploy

Follow these links: 
1. https://aws.amazon.com/getting-started/hands-on/deploy-python-application/
2. https://docs.bitnami.com/ibm/infrastructure/django/get-started/deploy-django-project/#approach-b-self-contained-bitnami-installations

Plus this command
`sudo pip install --target=/opt/bitnami/python/lib/python3.8/site-packages/ -r requirements.txt`

## Features
- [x] Add order
- [x] Edit / Delete Order
- [x] Search Order
- [x] Print Invoice
- [x] Easy interface
- [x] Mobile view
- [x] WRM Function (New Features)
- [x] CRM Function (New Features)
- [x] Batch Update Function (New Features)
- [ ] Export Order Info by pdf
- [ ] Edit Company Info
- [ ] Access Control for different Role
