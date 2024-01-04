# Python-Django-CSVReader

This is an independent project. This program will read two csv files, users.csv and vehicles.csv. After reading the files it will then save the data into the database. The project also includes an admin site where the data can be viewed and edited. The database has constrains on the vehicle -> user association, meaning there is a foreign key in the vehicle data model.

After donwloading the project open it in an IDE such as, IntelliJ, VS Code, Ecliplse, or anything you prefer.
After the project is opened follow the instructions below:
    Create a virtual environment 
	    - python -m venv venv

  Once in the project terminal run the following commands
    - to activate the virtual environment
    	- .venv\Scripts\activate
    ------------------------------------------------------
    - create database tables and apply any changes
    	- python manage.py makemigrations
    	- python manage.py migrate 	
    ------------------------------------------------------
    - import the csv files with custom management commands
    	- python manage.py import_users
    	- python manage.py import_vehicles  
    ------------------------------------------------------
    - create a superuser for an admin page login
      - python manage.py createsuperuser
    ------------------------------------------------------
    - run a server
    	- python manage.py runserver
        - Once you open the server side in the URL on top,
            add /admin, and login with the superuser created.
