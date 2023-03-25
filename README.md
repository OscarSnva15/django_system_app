# Django

Django es un framework web que te permite desarrollar aplicaciones web, de forma rapida e intituiva, pues esta diseñado para crear flujos o aplicaciones dentro del ramo desarollo web, evitando reinventar la rueda de aquellos flujos repetitivos en una aplicacion web.

## First step wiht django

So, The first step is install django in our system, so we need type in python line comand:

```python
pip install Django==4.1.7
```

Second step, next go to validate the instalation

```python
python -m django --version

#we obtain output : 4.1.7
```

After create a project whit command

```python
django-admin startproject mysite
```

- Consideracion1: Evitar poner codigo python en el directorio de siempre var/ww

- Consideracion2: Evitar nombrar el prjecto como "django" or "test" because this causes conflic with Django self o python packages

Once created project, we can show how seeing the directory project, as such as:

```python
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

These files are:

- The outer `mysite/` root directory is a container for your project. Its
  name doesn’t matter to Django; you can rename it to anything you like.
- `manage.py`: A command-line utility that lets you interact with this
  Django project in various ways. You can read all the details about `manage.py` in [django-admin and manage.py](https://docs.djangoproject.com/en/4.1/ref/django-admin/).
- The inner `mysite/` directory is the actual Python package for your
  project. Its name is the Python package name you’ll need to use to import
  anything inside it (e.g. `mysite.urls`).
- `mysite/__init__.py`: An empty file that tells Python that this
  directory should be considered a Python package. If you’re a Python beginner,
  read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages "(in Python v3.11)") in the official Python docs.
- `mysite/settings.py`: Settings/configuration for this Django
  project. [Django settings](https://docs.djangoproject.com/en/4.1/topics/settings/) will tell you all about how settings
  work.
- `mysite/urls.py`: The URL declarations for this Django project; a
  “table of contents” of your Django-powered site. You can read more about
  URLs in [URL dispatcher](https://docs.djangoproject.com/en/4.1/topics/http/urls/).
- `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to
  serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/) for more details.
- `mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to
  serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/) for more details.

# The server developer for Django

Let's verify your Django project works. Change into the outer `mysite` directory, if
you haven’t already, and run the following commands:

```shell
python manage.py runserver
```

Now we can go to direcction [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to show the page where can load our project

# Create a first aplication with django

Create a folder container of the project, it can be create in a location preferent, in this case our folder names must be Django_system_app

```shell
mkadir location/documents/django_system_app
```

So, next we goint to create a virtual environtment with python

```python
#instalamos modulo virtualenv
pip install venvironment
#verificamos la version
virtualenv --version
#we'll seeing the next ouput:
#-> virtualenv 20.15.1 from /usr/lib/python3.11/site-packages/virtualenv/__init__.py
```

Now, we goint to create a virtaul environment into folder name Django_system_app

```python
python -m venv Django_system_app/venv(name_environtment)
```

Activate the virtual env

```python
source venv/bin/activate
```

verify that django is installed into environment

```shell
django-admin --version

#output shell: 4.1.7
```

else we need install django into folder, with helps environement create

```shell
#1 upgrade pip
pip install --upgrade pip
#2 install django-admin
pip install django
#3 check django version
django-admin --version
#output : 4.1.7
```

Once time that we have installed django into project, we goint to init with our first project

## Creating project Dashboard for project Django_System_App. . .

                                                                    :)

Hola mi nombre es oscar, if you wants to watch the documentation abouth <u>"Creating project Dashboard for project Django_System_App"</u> please send me email. because for moment the documentation is wrritting in my One Note on line, from Notion account :D

Grettings, Oscar snva15

[oscarsnva15@gmail.com](mailto:oscarsnva15@gmail.com)
