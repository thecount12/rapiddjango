# How to create static pages

```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

## Media files

Edit root urls.py and change the last line in urlpatterns

```
urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## flatpages
make sure staticfiles, sites, and flatpages are added

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',
]
```


## settings.py 

add site id anywhwere in settings.py 

```
SITE_ID = 1
```

## edit urls.py again

```
url(r'^pages/', include('django.contrib.flatpages.urls')),
```

python manage.py makemigrations
python manage.py migrate

create directory for flatpages under template

flatpages/default.html:

Add the following tag to default.html

 {{ flatpage.content }}

visit: http://127.0.0.1:8000/admin/flatpages/flatpage/add/

In the GUI add a new flatpage and change the following Fields

URL: /privacy/
Title: asdf
Content: whatever html code you want
Sites: example.com

## Load all templates

Load all templates in the template you need to load {{ flatpages }}

```
{% load flatpages %}
{% get_flatpages as flatpages %}
<ul>
  {% for page in flatpages %}
    <li><a href="{{ page.url }}">{{ page.title }}</a></li>
  {% endfor %}
</ul>
```

## file upload

Edit forms.py

```
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
```


## Handling uploaded files with a model

If you’re saving a file on a Model with a FileField, using a ModelForm makes this process much easier. The file object will be saved to the location specified by the upload_to argument of the corresponding FileField when calling form.save():


## Template Truncation

This is a handy feature to grab a snipit of the body for your comments. This 
truncates the template model by 9 characters. 


{{ value|truncatechars:9 }}



