# Missing items

1. `ALLOWED_HOSTS = ['*']`
2. `SITE_ID = 1`
3. `'whitenoise.middleware.WhiteNoiseMiddleware',`
4. look at another example with psql stuff
5. create static 
6. static files/
7. add `{% load static %}`
8. get current bootstrap maxcdn


```
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```


