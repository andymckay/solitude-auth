import logging

import private_base as private

from solitude.settings import base
from django_sha2 import get_password_hashers

ALLOWED_HOSTS = ['payments-proxy.allizom.org']

DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False

HMAC_KEYS = private.HMAC_KEYS

PASSWORD_HASHERS = get_password_hashers(base.BASE_PASSWORD_HASHERS, HMAC_KEYS)

LOG_LEVEL = logging.DEBUG

SECRET_KEY = private.SECRET_KEY

SENTRY_DSN = private.SENTRY_DSN

STATSD_HOST = private.STATSD_HOST
STATSD_PORT = private.STATSD_PORT
STATSD_PREFIX = private.STATSD_PREFIX

SYSLOG_TAG = 'http_app_payments_stage'

NEWRELIC_INI = '/etc/newrelic.d/payments-proxy.allizom.org.ini'
NOSE_PLUGINS = []

BANGO_AUTH = private.BANGO_AUTH

ZIPPY_CONFIGURATION = {}
