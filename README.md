django-quick-start
==================

This is a Django project template to help you get up and running quick. It includes jquery and bootstrap, but does not depend on any other Django apps. This means all of the code that makes your site is contained in your project directory (unlike pinax where even the core code is hidden across multiple apps.)


This project is build on Django 1.5, jQuery 1.10, and Bootstrap 3.0. Django 1.5 is most happy with Python >= 2.7. If you'd like, you can set up a virtual environment. Otherwise, skip those steps.

    sudo apt-get install python-pip
    pip install virtualenv
    virtualenv djangoenv
    source djangoenv/bin/activate
    pip install Django==1.5

Setup your new project by running the following command (replace site_name with the name of your new website):

    django-admin.py startproject --template=https://github.com/joshvillbrandt/django-quick-start/zipball/master site_name

Run your server:

    cd site_name
    python manage.py syncdb
    python manage.py runserver 0.0.0.0:8080
