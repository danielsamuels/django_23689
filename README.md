# Django \#23689 repro

How to see the reproduction:

```shell
py -3.10 -m venv venv
. venv/Scripts/activate
python -m pip install -r requirements.txt
python manage.py test
```

How this repo was created:

```shell
echo 'Django==3.2.13' > requirements.txt
py -3.10 -m venv venv
. venv/Scripts/activate
python -m pip install -r requirements.txt
django-admin.py startproject django_23689 .
mkdir -p django_23689/templates/
touch django_23689/templates/example.html
```

Then:
* Added `views.py` and `tests.py` 
* Updated `urls.py` to have the new path
* Updated `settings.py` to add locale middleware and pt languages

