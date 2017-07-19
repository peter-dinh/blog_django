# blog_django
blog_django

required begin: setup "django", setup "pip" and "psycopg2"

1, Setup library python in "/requirements/dev.txt":
$sudo pip install -r requirements/dev.txt

2, Setup database:
App blog using django-admin:

$python mysite/manage.py migrate

$python mysite/manage.py makemigrations blog

$python mysite/manage.py sqlmigrate blog 0001

$python mysite/manage.py migrate

Create account admin:

$python mysite/manage.py createsuperuser

3, Run app:

$python mysite/manage.py runserver

