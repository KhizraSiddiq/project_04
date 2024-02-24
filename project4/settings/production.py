import environ

from project4.settings.local import *

env = environ.Env(
    DEBUG=(bool, False)
)

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
DATABASES = {
    'default': env.db(),
}
