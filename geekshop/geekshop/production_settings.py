DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'NAME': 'geekshop',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'django',
        'PASSWORD': 'geekbrains',
        'HOST': 'localhost'
    }
}
