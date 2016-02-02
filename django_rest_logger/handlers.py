from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.utils import six
from django.utils.translation import ugettext_lazy as _
from rest_framework import status, exceptions
from rest_framework.response import Response

from .log import exception as log_exception


def rest_exception_handler(exc, context):
    """
    Return the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `ValidationError`, `Http404` and `PermissionDenied`
    exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, dict):
            data = exc.detail
        elif isinstance(exc.detail, list):
            data = {'non_field_errors': exc.detail}
        else:
            data = {'non_field_errors': [exc.detail]}

        return Response(data, status=exc.status_code, headers=headers)

    elif isinstance(exc, Http404):
        msg = _('Not found.')
        data = {'non_field_errors': [six.text_type(msg)]}
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = _('Permission denied.')
        data = {'non_field_errors': [six.text_type(msg)]}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
    else:
        log_exception()
        msg = _('Server Error. Please try again later.')
        data = {'non_field_errors': [six.text_type(msg)]}
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
