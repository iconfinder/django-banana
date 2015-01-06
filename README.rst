django_banana - Delicious split testing for Django
==================================================

.. image:: https://travis-ci.org/iconfinder/django-banana.png?branch=master
        :target: https://travis-ci.org/iconfinder/django-banana

Banana is a pure backend split testing addition to Django, which exposes
experiment selections in the template context to be handled by frontend
data collection frameworks. Actual experiment option selection is stored using
the built-in Django sessions.


Installation
------------

To install ``django_banana``, do yourself a favor and don't use anything other than `pip <http://www.pip-installer.org/>`_:

.. code-block:: bash

   $ pip install django-banana

Add ``django_banana`` to the list of installed apps in your settings file:

.. code-block:: python

   INSTALLED_APPS = (
       'django_banana',
       ..
   )
