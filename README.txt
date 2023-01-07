python -m pip install --upgrade pip
pip install django
django-admin startproject blog_project
cd blog_project
python manage.py startapp blog
python manage.py migrate
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

#Работа с изображениями
pip install pillow

#python manage.py makemigrations - first, python manage.py migrate - second