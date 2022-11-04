# Django session

## Project configuration

1) Create a repo using **use template** button
2) Clone the repo from your profile
3) ```bash 
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
    ```

## Basic Commands and uses

### Creating a new Django project

```bash
django-admin startproject project_name

```

### Create a new application in the Django project

```bash
python manage.py startapp app_name
```

### Running Django server

```bash
python manage.py runserver
```

### Database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating a superuser

```bash
python manage.py createsuperuser
```

## Basic Database filed names

| Usage                                   | Filed                                  |
|-----------------------------------------|----------------------------------------|
| A string with a maximum length of 100   | models.Charfiled(max_length=100)       |
| Text area (without limit)               | models.Textfield()                     |
| Integer (number without floating value) | models.IntegerField()                  |
| Floating point number                   | models.FloatField()                    |
| Date                                    | models.DateField()                     |
| Image                                   | models.ImageField(upload_to="images")  |
