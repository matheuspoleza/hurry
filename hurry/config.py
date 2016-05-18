# -*- coding: utf-8 -*-
class DefaultConfig(object):
    DEBUG = True
    TESTING = False

    SECRET_KEY = ''
    SESSION_COOKIE_NAME = 'hsessionid'
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_PATH = '/'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)

    STATIC_ROOT = ''
    STATIC_PATH = ''

    HANDLER_FOR_404 = 'hurry.http.NotFoundHandler'
    HANDLER_FOR_500 = 'hurry.http.ErrorHandler'
