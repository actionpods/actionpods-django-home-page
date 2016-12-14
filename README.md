=====
HomePage
=====

Homepage is a simple Django app that provides a simple structure for displaying a home landing page with introductory models and a newsletter

Quick start
-----------

1. Add "homepage" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'homepage',
    ]

2. Include the homepage URLconf in your project urls.py like this (assuming this will be the root page):

    url(r'^', include('homepage.urls')),

3. Run `python manage.py migrate` to create the homepage models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a homepage (you'll need the Admin app enabled).
