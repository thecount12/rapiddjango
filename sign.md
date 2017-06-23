# first add signup to settings.py 


## root urls.py 

```
import signup.views
 url(r'^signup/',signup.views.Signup),
```

## models.py

```
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
```

## forms.py

```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

	class Meta:
		model = User
		fields = ('username', 'birth_date', 'password1', 'password2', )
```

## views.py

```
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from signup.forms import SignUpForm

def Signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
```

## signup.html

```
{% extends 'base.html' %}
{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign up</button>
  </form>
{% endblock %}
```

## admin.py

```
from signup.models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfInline(admin.StackedInline):
	model=Profile
class ProfAdmin(admin.ModelAdmin):
	inlines = (ProfInline,)

admin.site.unregister(User)
admin.site.register(User,ProfAdmin)
```

