import os

ADMINS = ()
DATABASES = {}


database_implementation = os.getenv('DATABASE', 'sqlite3')

DATABASES['default'] = {
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_banana.db',
    },
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': os.getenv('DATABASE_USER', 'postgres'),
        'NAME': 'djts',
        'OPTIONS': {
            'autocommit': True,
        },
    },
}[database_implementation]

SECRET_KEY = '_uobce43e5osp8xgzle*yag2_16%y$sf*5(12vfg25hpnxik_*'

INSTALLED_APPS = (
    'django_banana',
    'tests',
    'django_nose',
)

MIDDLEWARE_CLASSES = []

DEBUG = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--verbosity=2', '--detailed-errors', '--rednose']
