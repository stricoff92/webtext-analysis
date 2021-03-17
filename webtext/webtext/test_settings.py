
import os.path

from .settings import *


ENV = "TESTING"
DEBUG = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
AUTH_PASSWORD_VALIDATORS = []


# Faster insecure hashing for testing only
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# File Based DB for Faster setup and teardown
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'testdb.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
