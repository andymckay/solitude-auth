from .base import *  # noqa
try:
    from .local import *  # noqa
except ImportError:
    print 'No local.py imported, skipping.'
