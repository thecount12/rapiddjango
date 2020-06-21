# Missing items

These are obvious features that should be added. Such as Allowed hosts and site id. Whih will 
allow you to log into remotely or work with static files or pages. WhiteNoise is mostly for 
heroku environment. 

Heroku demands the usage of postgres

1. `ALLOWED_HOSTS = ['*']` add to settings.py
2. `SITE_ID = 1` add to settings.py
3. `'whitenoise.middleware.WhiteNoiseMiddleware',` add to settings.py
4. look at another example with psql stuff and add below
5. in root of the project create static/ directory
6. python manage.py collectstatic -> this command will migrate admin stuff to static and staticfiles
7. add `{% load static %}` add this to base.html
8. get current bootstrap maxcdn. Go to getbootstrap and get latest maxcdn url 
9. runtime.txt add python-3.8.3 as the first line in the file

```
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
whitenoise.middleware.WhiteNoiseMiddleware for python3.8.3 for django 3.0.7 ?  i think. 
```

Missing items Heroku for AWS 
```
USE_S3 = os.getenv('USE_S3') == 'TRUE'

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3-website-us-west-2.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
```

Posgress connection: TODO

Follow Heroku instructions for point Gandi, Godaddy or whatever DNS you would like to point to heroku.

django-simple-captcha

1. pip install django-simple-captcha
2. add captcha to INSTALLED_APPS in settings.py
3. python manage.py migrate
4. Add entry to your urls.py `path('captcha/', include('captcha.urls')),`
5. add two lines to the forms.pp. The import `from captcha.fields import CaptchaField`
and `captcha = CaptchaField() just above class Meta:`

```
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
```
For more info about this: https://django-simple-captcha.readthedocs.io/en/latest/usage.html




