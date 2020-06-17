"""
rapidsetup.py
setup script to install fresh blog, poll, protected page, signup, and extended registration
William C. Gunnells
http://www.rapidpythonprogramming
"""

import subprocess
import os
import shutil
from mystring import *


class Rapid(object):
    """
    class to install blog, poll, protected pages, signup etc...
    """

    def __init__(self, bootstrap, indexdata,
                 logindata, basicview, zclean,
                 project, rooturl, setpath,
                 seturl, setapp, rooturlimport):
        self.boot_strap = bootstrap
        self.index_data = indexdata
        self.login_data = logindata
        self.basic_view = basicview
        self.z_clean = zclean
        self.project = project
        self.root_url = rooturl
        self.setpath = setpath
        self.set_url = seturl
        self.set_app = setapp
        self.root_url_import = rooturlimport

    def write_data(self, type, data_file, data_object):
        """
        File Handler
        :param type: str() a append or w write
        :param data_file: str() of file to write
        :param data_object:
        :return: None
        """
        with open(data_file, type) as file:
            file.write(data_object)

    def project_create(self):
        """
        start project
        :return: None
        """
        subprocess.call(['django-admin', 'startproject', self.project])

    def basic_app(self):
        """
        Create Django Main root page
        :return: None
        """
        subprocess.call(['django-admin', 'startapp', 'basicapp'], cwd=self.project)
        my_path = self.project+"/"+"basicapp/templates"
        if not os.path.exists(my_path):
            os.makedirs(my_path)
        view = self.project+"/basicapp/views.py"
        self.write_data('a', view, self.basic_view)
        index = self.project+"/basicapp/templates/index.html"
        self.write_data('w', index, self.index_data)
        base = self.project+"/basicapp/templates/base.html"
        self.write_data('w', base, self.boot_strap)

    def signup(self):
        """
        Create signup app
        :return: None
        """
        subprocess.call(['django-admin', 'startapp', 'signup'], cwd=self.project)
        my_path = self.project+"/"+"signup/templates"
        if not os.path.exists(my_path):
            os.makedirs(my_path)
        view = self.project+"/signup/views.py"
        signup_view = """
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, render_to_response
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
            return redirect('/thanks/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def thanks(request):
    return render(None, "thanks.html")
        """
        self.write_data('a', view, signup_view)
        my_form = self.project+"/signup/forms.py"
        sign_form = """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )
        """
        self.write_data('a', my_form, sign_form)

        my_index = self.project+"/signup/templates/signup.html"
        sign_index = """
{% extends 'base.html' %}
{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign up</button>
  </form>
{% endblock %}
        """
        self.write_data('w', my_index, sign_index)
        my_thanks = self.project+"/signup/templates/thanks.html"
        thanks_index = """
{% extends 'base.html' %}
{% block content %}
<p>Thanks. Your information has been added.</p>
{% endblock %}
        """
        self.write_data('w', my_thanks, thanks_index)
        my_model = self.project+"/signup/models.py"
        sign_model = """
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    editor = models.NullBooleanField(blank=True)
    subscriber= models.NullBooleanField(blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
        """
        self.write_data('a', my_model, sign_model)
        base = self.project+"/signup/templates/base.html"
        self.write_data('w', base, self.boot_strap)
        admin_stuff = self.project+"/signup/admin.py"
        admin_data = """
from signup.models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfInline(admin.StackedInline):
    model=Profile

class ProfAdmin(admin.ModelAdmin):
    inlines = (ProfInline,)


admin.site.unregister(User)
admin.site.register(User,ProfAdmin)
        """
        self.write_data('a', admin_stuff, admin_data)

    def blog(self):
        """
        Creates blog views, forms, model, admin and html files
        :return: None
        """
        # Create Django Blog
        subprocess.call(['django-admin', 'startapp', 'blog'], cwd=self.project)
        my_path = self.project+"/"+"blog/templates/blog"
        if not os.path.exists(my_path):
            os.makedirs(my_path)
        view = self.project+"/blog/views.py"
        self.write_data('a', view, blogviews)
        model = self.project+"/blog/models.py"
        self.write_data('a', model, blogmodel)
        admin = self.project+"/blog/admin.py"
        self.write_data('a', admin, blogadmin)
        forms = self.project+"/blog/forms.py"
        self.write_data('w', forms, blogforms)
        urls = self.project+"/blog/urls.py"
        self.write_data('a', urls, blogurls)
        my_post_list = self.project+"/blog/templates/blog/post_list.html"
        self.write_data('w', my_post_list, post_list)
        my_post_detail = self.project+"/blog/templates/blog/post_detail.html"
        self.write_data('w', my_post_detail, post_detail)
        my_post_comment = self.project+"/templates/postcomment.html"
        self.write_data('w', my_post_comment, post_comment)

    def clean(self):
        """
        Script to create clean.py for maintenance push
        :return: None
        """
        self.write_data('w', 'clean.py', self.z_clean)

    def url(self):
        """
        Login and Logout function
        :return: None
        """
        ar = []
        my_path = self.project + "/" + self.project + "/" + "urls.py"
        new_path = self.project + "/" + self.project + "/" + "test.dat"
        shutil.move(my_path, new_path)
        with open(new_path, 'r') as f:
            for i in f:
                ar.append(i)
                if 'import admin' in i:
                    ar.append(self.root_url_import)
                if 'urlpatterns =' in i:
                    ar.append(self.root_url)
        print("Adjusted URLS for login Apps: %s" % my_path)
        with open(my_path, 'a') as w:
            for z in ar:
                if z[:4] == '    ':
                    w.write("\t" + z[4:])
                else:
                    w.write(z)

    def settings(self):
        """
        Modify settings.py
        :return: None
        """
        ar = []
        my_path = self.project + "/" + self.project + "/" + "settings.py"
        new_path = self.project + "/" + self.project + "/" + "test.set"
        shutil.move(my_path, new_path)
        with open(new_path, 'r') as f:
            for i in f:
                if 'os.path.abspath' in i:
                    ar.append(self.setpath)
                elif 'DIRS' in i:
                    fix = i.replace("'DIRS': [],", "'DIRS': [TEMPLATE_DIR],")
                    ar.append(fix)
                elif 'STATIC_URL =' in i:
                    ar.append(self.set_url)
                elif 'django.contrib.staticfiles' in i:  # create apps before adding
                    ar.append(self.set_app)
                else:
                    ar.append(i)
        with open(my_path, 'a') as w:
            for z in ar:
                w.write(z)

        b_path = self.project+"/"+"templates"
        if not os.path.exists(b_path):
            os.makedirs(b_path)
            os.makedirs(b_path+"/registration")
        login_file = self.project+"/templates/registration/login.html"
        self.write_data('w', login_file, self.login_data)
        boot_file = self.project+"/templates/base.html"
        self.write_data('w', boot_file, self.boot_strap)
        print("Adjusted features for settings: %s" % my_path)

    def run(self):
        """
        Main
        :return: None
        """
        self.clean()
        self.project_create()
        self.signup()
        self.basic_app()
        self.url()
        self.settings()
        self.blog()


if __name__ == "__main__":
    project = input("Enter your Django Project Name: ")
    new_site = Rapid(bootstrap,
                     indexdata,
                     logindata,
                     basicview,
                     zclean,
                     project,
                     rooturl,
                     setpath,
                     seturl,
                     setapp,
                     rooturlimport)
    new_site.run()


