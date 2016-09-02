# -*- coding: utf-8 -*-
"""
This module is a central location for all Morelia exceptions
"""


class MoreliaException(Exception):
    """
    Base exception class; all Morelia-specific exceptions should subclass this
    """
    strerror = None

    def __init__(self, message=''):
        super(MoreliaException, self).__init__(message)
        self.strerror = message


class InvalidOperationException(MoreliaException):
    def __init__(self, *args, **kwargs):
        super(InvalidOperationException, self).__init__(*args, **kwargs)
