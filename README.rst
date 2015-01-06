.. image:: https://cdn2.iconfinder.com/data/icons/indeepop_iconspack_/256/yammi_banana.png

django_banana - Delicious split testing for Django
==================================================

.. image:: https://travis-ci.org/iconfinder/django-banana.png?branch=master
        :target: https://travis-ci.org/iconfinder/django-banana

Django Banana is a pure backend split testing addition to Django, which exposes experiment selections in the template context to be handled by frontend data collection frameworks. Actual experiment option selection is stored using the built-in Django sessions.


Installation
------------

To install ``django_banana``, do yourself a favor and don't use anything other than `pip <http://www.pip-installer.org/>`_:

.. code-block:: bash

   $ pip install django-banana

Add ``django_banana`` to the list of installed apps and add the ``ExperimentsMiddleware`` class to the list of middleware in your settings file:

.. code-block:: python

   INSTALLED_APPS = (
       'django_banana',
       ..
   )

   MIDDLEWARE_CLASSES = (
       'django_banana.middleware.ExperimentsMiddleware',
       ..
   )


Usage
-----

To set up an experiment with Django Banana, simply register the experiment with the request at some point in the view flow:

.. code-block:: python

   from django_banana.option import Option

   experiment = request.experiments.add(identifier='my_experiment',
                                        generation=1,
                                        options=[
                                            Option('a', weight=1, extra={
                                                'detail': 'A',
                                            }),
                                            Option('b', weight=2, extra={
                                                'detail': 'A',
                                            }),
                                        ])

This will create an experiment with the request and automatically select one of the provided options. The ``generation`` argument allows your to create multiple generations of the same experiment as you refine it, rather than having to come up with new identifiers.

The selected option can be accessed from the returned experiment object:

.. code-block:: python

   option_detail = experiment.get_selected().extra['detail']
