django-quick-start project
==================

This is a Django project template to help you get up and running quick.

The django-quick-start project builds on Django 1.5, jQuery 1.10, and Bootstrap 3.0. Unlike other Django templates like Pinax, django-quick-start is much more lightweight. A key design goal here was to have all of the templates that build the set present within the project (in contrast to Pinax.) This makes it easier to understand how your entire page is built and makes changing things easier.
It includes jquery and bootstrap, but does not depend on any other Django apps. This means all of the code that makes your site is contained in your project directory (unlike pinax where even the core code is hidden across multiple apps.)

# Setup

This setup sequence has been tested on Ubuntu 12.04. If you'd like, you can set up a virtual environment. Otherwise, skip those steps.

    sudo apt-get install python-pip
    pip install virtualenv
    virtualenv djangoenv
    source djangoenv/bin/activate
    pip install Django==1.5

Start your new project by running the following command (replace site_name with the name of your new website):

    django-admin startproject --template=https://github.com/joshvillbrandt/django-quick-start/project/zipball/master site_name

Start the development server:

    cd site_name
    python manage.py syncdb
    python manage.py runserver 0.0.0.0:8080

# Get to work

Now that you have a simple Django project installed, you probably want to create some models. The models.py file includes the basic poll model as described in the Django tutorials. 

# Development via repo

    django-admin.py startproject --template=/home/jvillbrandt/django-quick-start/django-quick-start testproject
    cd testproject
    rs