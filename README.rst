REST Logger for Django
=======================

|Travis|

.. |Travis| image:: https://travis-ci.org/pedrorodriguesgomes/django-rest-logger.svg
   :target: https://travis-ci.org/pedrorodriguesgomes/django-rest-logger


**REST logger for Django**

Overview
--------

This package provides a logger specifically designed to REST APIs using Django.

Requirements
------------

-  Python (2.7, 3.3, 3.4, 3.5, 3.6)
-  Django (1.8, 1.11)
-  Django REST Framework (3.8)

Installation
------------

Install using ``pip``\ ...

.. code:: bash

    $ pip install django-rest-logger

Usage
------------

Add default exception handler to your Django REST Framework settings:

.. code:: python

    REST_FRAMEWORK = {
        'EXCEPTION_HANDLER': 'django_rest_logger.handlers.rest_exception_handler',
    }


Add logger configuration to your development settings.py:

.. code:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'DEBUG',
            'handlers': ['django_rest_logger_handler'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'django_rest_logger_handler': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['django_rest_logger_handler'],
                'propagate': False,
            },
            'django_rest_logger': {
                'level': 'DEBUG',
                'handlers': ['django_rest_logger_handler'],
                'propagate': False,
            },
        },
    }

    DEFAULT_LOGGER = 'django_rest_logger'

    LOGGER_EXCEPTION = DEFAULT_LOGGER
    LOGGER_ERROR = DEFAULT_LOGGER
    LOGGER_WARNING = DEFAULT_LOGGER


Example for logger configuration using Sentry to be used in your production settings.py:

.. code:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.request': {
                'level': 'DEBUG',
                'handlers': ['sentry'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['sentry'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['sentry'],
                'propagate': False,
            },
        },
    }

    DEFAULT_LOGGER = 'raven'

    LOGGER_EXCEPTION = DEFAULT_LOGGER
    LOGGER_ERROR = DEFAULT_LOGGER
    LOGGER_WARNING = DEFAULT_LOGGER

