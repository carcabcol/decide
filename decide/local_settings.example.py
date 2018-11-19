ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'http://localhost:80',
    'base': 'http://localhost:80',
    'booth': 'http://localhost:80',
    'census': 'http://localhost:80',
    'mixnet': 'http://localhost:80',
    'postproc': 'http://localhost:80',
    'store': 'http://localhost:80',
    'visualizer': 'http://localhost:80',
    'voting': 'http://localhost:80',
}

BASEURL = 'http://localhost:80'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
