from django.conf import settings

LOGGING = {
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['rest_logger_handler'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'rest_logger_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['rest_logger_handler'],
            'propagate': False,
        },
        'django_rest_logger': {
            'level': 'DEBUG',
            'handlers': ['rest_logger_handler'],
            'propagate': False,
        },
    },
}

LOGGING_SETTINGS = getattr(settings, 'LOGGING', LOGGING)
DEFAULT_LOGGER = getattr(settings, 'DEFAULT_LOGGER', 'django_rest_logger')

LOGGER_EXCEPTION = DEFAULT_LOGGER
LOGGER_ERROR = DEFAULT_LOGGER
LOGGER_WARNING = DEFAULT_LOGGER
LOGGER_INFO = DEFAULT_LOGGER
