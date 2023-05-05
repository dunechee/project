# EXOPLANET SHOPPING SITE
This site is a basic shopping website that sells exoplanets. The exoplanets dataset was gotten from [Kaggle](https://www.kaggle.com/datasets/eduardowoj/exoplanets-database)

## SETTING UP THE APPLICATION
### CREATING THE ENVIRONMENT
To set up the application run the following commands:
```
pyenv local 3.10.7 # this sets the local version of python to 3.10.7
python3 -m venv .venv # this creates the virtual environment for you
source .venv/bin/activate # this activates the virtual environment
pip install --upgrade pip # this installs pip, and upgrades it if required.
pip install django # installs the django frameworks
pip install faker # installs faker
python3 manage.py migrate #iniitializes the database
```

### SETTING UP THE DATABASE
The database used is Postgres. Render offers a Postgres database environment where you can create a database and use the parameters to set up your database
On your environment, run:
```
pip install dj-database-url # this package allows you to connect to the external DB
```
On mysite/settings.py, add `import dj_database_url` at the top of the file. The database part of the file should look like this:
```
DATABASES = {

    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
On the terminal, run:
```
export DATABASE_URL="your external url from postgres"
```
After initializing the database, run these commands to create the tables in the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### POPULATING THE DATABASE
The app uses Faker to generate random customers and orders and the products are parsed from the .csv file in '/data/exoplanets.csv' using the parameters specified in '/management/commands/parse_csv.py'. You populate the data using the command:
```
python3 manage.py parse_csv
```

### CREATING ADMIN
You can create an admin user to monitor the customers and orders made in the shop. There is also a dashboard that monitors the sales made by the customers. You can also add more admins or customers. Run this command:
```
python3 manage.py createsuperuser
```

### RUNNING THE SERVER
To run the server to display on the webpage, run:
```
python3 manage.py runserver # on local machine
python3 manage.py runserver 0.0.0.0:8000 # to run on codio
````
