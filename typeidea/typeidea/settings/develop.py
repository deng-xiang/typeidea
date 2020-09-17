from .base import * # NOQA

DEBUG=True
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
	    'USER':'type_user',
	    'PASSWORD':'123456',
	    'HOST':'127.0.0.1',
	    'PORT':'3306'
    }
}
