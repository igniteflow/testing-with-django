from .settings import *

MIGRATION_MODULES = {
    'myapp': None,
}

INSTALLED_APPS += [
    'django_nose',
]

# django-nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# see `./manage.py test --help` for all options 
NOSE_ARGS = [
    '--failed',  # Run the tests that failed in the last test run
    
    # coverage
    '--with-coverage',
    '--cover-package=myapp',
    '--cover-html',
]
