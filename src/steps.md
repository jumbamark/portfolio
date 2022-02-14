## drawsql -way of wire framing databases
* After edit button on projects page
* Install django ck editor(pip install django-ckeditor, add to installed apps) - for the rich text editor
* ckeditor uploader field - we can upload files in our editor
* we need to modify the project field to that ckeditor
* Then go into project page and change how that body is being output
* Add ckeditor_uploader in settings - to enable photo uploading


## contact Form 
* adding a flash message - go to django flash messages (import in views)


## Deploying to Heroku
- In settings.py go to allowed hosts - it's a list of allowed hosts(domains that you're using,anything that you want to basically allow to work with the application)
- If you don't set this heroku can't deploy our application
- Open the app in heroku and copy the link, paste it into ALLOWED_HOSTS - ie ['portfolio-live.herokuapp.com', '127.0.0.1', 'localhost'] - now django knows allows this app to work with the application.
- You need requirements.txt - this is how we tell heroku what our application needs

## Procfile
* configure gunicorn - it automatically configures heroku
* Remebet to install gunicorn (pip install gunicorn)
* Heroku runs on dynos and we basically need to specify the dyno type, that's how heroku knows what to do with your application
* In procfile; web: gunicorn (the name of our project - where are we gonna connect this to(wsgi file))


- runtime.txt - we specify the vaersion of python we're using

- Creating a requirements.txt in our root folder 
- pip freeze > requirements.txt

## Application error on heroku 
after logging in through the cli ; heroku logs --tail a {app-name}

- If staticfiles fail to run(css maybe broken bec of that) > pip install whitenoise (whitenoise django documentation)
whitenoise - basically a way of serving up staticfiles, django on it's own doesn't serve staticfiles in production

### Creating a relationship with the Comments model
* many to one relationship - a comment can be applied to a single project but a project can have many comments
 on_delete=models.CASCADE - if a project is deleted all the comments will be deleted


 ## Django Rest API
 * using it to query the data from our model 
 * create an api folder 
 * create the following files;  init.py
 * urls.py- creating it's own system basically
 * views.py - we are gonna provide some data
 * seriaizers.py - we need to serilize the data

 - Make sure to connnect that view(mapped to urls.py/api) to our root urls file 

 - pip installl django rest framework and add it to installed apps(django rest framwework doc)
 - Now add some decorators and some serializers
 - serializer - converting data into json data,we're serializing it
 - A model serializer is kinda like a model form where we take a model from the database and we build out a serializer based on that model (not having to do everything by hand)


 - Remeber to add the django rest framework into the requirements.txt file


 # Hiding the secret key in django
 Django project has sensitive data such as secret key,data base credentials which requires securing from public websites such as github where they can be accesses by anyone who has access to the code
 securing the secret key using python decouple package;
 pip install python -decouple or you can use pip install python-dotenv
 to use it create a .env file inside the project
 Copy the secret key and remove quotations
 Go to settings .py and import the package that we installed (from decouple import config/ from dotenv import load_dotenv)
 If you used dotenv call fuction load_dotenv() below the import os...  SECRET_KEY = os.getenv('SECRET_KEY')
 We dont push the .env on the source control so that no one has access to it 


# Checking if everything is working
python manage.py check


## Git ignore - (code .gitignore) - creates a .gitignore file in vs code
- There are some things inside of your repository that you dont want put up with github; db, cashed python files and any sort of secret password 
- Before we attempt to run our server we wanna get that in place bec when we run the  server for the first time that's what creates those cashed files and database
- open up project and create a .gitignore file
- Inside of here, specify what files you don't want added to your git repo (i.e *.pyc - any file with a .pyc at the end will not be committed into our repo)
- You can also specify folders(ie /static - top level static folder, we dont wanna see that here)
- Webiste that gives defaults to our projects : gitignore.io
- Search for django and click create - it gives you a starting point
- Copy it and paste into your .gitignore file
* Add /static and modify media to /media
- Initialize the project as a git repo - git init; adds .git folder
- git status
- git add -A
- git commit -m "Our first"



## Pushing django project into github
- Create a repo - simply a project directory
- git init
- git status
- git add .
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/jumbamark/jumbamark.github.io.git
- git push -u origin main


## Using postgreql data base
- Go to command line
- sudo su postgres
- psql
- CREATE DATABASE portfolio;  ..
- pip install psycopg2-binary


## Modifying the database insettings.py (end at password = ok)
DATABASE = {
    'default':{
    'ENGINE': 'django.db.backends.postgresql',
    'NAME' : 'path',
    'USER' : 'postgres',
    'PASSWORD': 'fafagzo123',
    'HOST': 'localhost',
    'PORT': '5432',
    }

     'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

}

## If you are in production you're going to have to secure this and make sure you encapsulate them in a different way (use .env file, os.getenv())
- psql
- posgres=#
- create database base;
- CREATE DATABASE
- create user mark superuser;  #superuser bec I wanna have any kind of permission-ultimate authority
- CREATE ROLE
- alter user mark with password 'django123';
- ALTER ROLE

- psql -d base
