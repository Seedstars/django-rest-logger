REST Logger for Django
=======================


**REST logger for Django**

Overview
--------

This package provides a logger specifically designed to REST APIs using Django.

Requirements
------------

-  Python (2.7, 3.3, 3.4)
-  Django (1.8)

Installation
------------

Install using ``pip``\ ...

.. code:: bash

    $ pip install django-rest-logger

Usage
------------

Add logger configuration to your settings.py::

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'DEBUG',
            'handlers': ['django_rest_logger_handler'],
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


