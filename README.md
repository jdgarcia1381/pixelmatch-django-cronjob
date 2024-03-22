# pixelmatch-django-cronjob

## Develop environment setup

To deploy the backend project on a local environment, please follow these instructions:

### Requirements

- Git
- Python3
- PostgreSQL >= 10

### Clone project

Clone the project from GitHub:

`git clone https://github.com/jdgarcia1381/pixelmatch-django-cronjob`

Go to root folder:

`cd pixelmatch-django-cronjob`

### Virtual environment

Create a python virtual environment for this project:

| Linux                       | Windows 10                     | Windows 10 second option |
| --------------------------- | ------------------------------ | ------------------------ |
| `python3 -m virtualenv env` | `python.exe -m virtualenv env` | `py -m virtualenv env`   |

If you don't have virtualenv, install it:

`python3 -m pip install virtualenv` | `python.exe -m pip install virtualenv` | `py -m pip install virtualenv` |

After installation is complete, activate the virtual environment:

| Linux                     | Windows 10               |
| ------------------------- | ------------------------ |
| `source env/bin/activate` | `.\env\Scripts\activate` |

### Environment variables

Make a copy of `.env.example`, rename it to `.env`, and change it according to you local configuration.

#### Linux

Import the variables in your `.env` file to your virtual environment:

`source .env`

#### Windows

Delete the `export` keyword from all the enviroment variables in your `.env` file.

> e.g. `export DB_DATABASE=pixelmatch` &#8594; `DB_DATABASE=pixelmatch`

### Database

If you haven't done so already, create an empty database on PostgreSQL.

Its name needs to match the one on the `DB_DATABASE` environment variable.

### Dependencies

Download project dependencies using pip:

`python -m pip install -r requirements.txt`

### Server configuration

After installing dependencies, run the following commands to set up the database and superuser:

`python pixelmatch/manage.py migrate`

`python pixelmatch/manage.py createsuperuser`

### Start server

Finally, run the Django local server:

`python pixelmatch/manage.py runserver`

### Create app users

Go to Django admin and create an app user. IMPORTANT: Assign the created user to the desired Django group.

`http://localhost:8000/admin`

## Development considerations

### Create new Django app

Django apps are located in `pixelmatch` folder. To create a new app, you can use the following command:

`cd pixelmatch && python manage.py startapp <app_name>`

### Start server on local network

To start server on local network and be able to connect from a different device, you can use:

`python pixelmatch/manage.py runserver 0.0.0.0:8000`

Then, you have to connect using your private IP address (e.g. http://192.168.1.6:8000/admin).

Note: make sure to add your private IP address into `DJANGO_ALLOWED_HOSTS` env var (`.env` file).

