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

    def __init__(self, bootstrap, indexdata, logindata, basicview, zclean, project, rooturl, setpath, seturl, setapp, rooturlimport):
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

    def project_create(self):
        # Create Django Project
        subprocess.call(['django-admin', 'startproject', self.project])

    def basic_app(self):
        # Create Django Main root page
        subprocess.call(['django-admin', 'startapp', 'basicapp'], cwd=self.project)
        mpath = self.project+"/"+"basicapp/templates"
        if not os.path.exists(mpath):
            os.makedirs(mpath)
        # write views.py for basicapp basicview
        myview = self.project+"/basicapp/views.py"
        with open(myview, 'a') as file:
            file.write(self.basic_view)
        # write index.html for basicapp indexdata
        myindex = self.project+"/basicapp/templates/index.html"
        with open(myindex, 'w') as f:
            f.write(self.index_data)
        # write base.html for basicapp bootstrap
        base = self.project+"/basicapp/templates/base.html"
        with open(base, 'w') as b:
            b.write(self.boot_strap)

    def signup(self):
        # Create signup app
        subprocess.call(['django-admin', 'startapp', 'signup'], cwd=self.project)
        mpath = self.project+"/"+"signup/templates"
        if not os.path.exists(mpath):
            os.makedirs(mpath)
        # write views.py for basic signup view
        myview = self.project+"/signup/views.py"
        signupview = """
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
    return render_to_response("thanks.html")
        """
        with open(myview, 'a') as file:
            file.write(signupview)
        # write forms.py for basic signup view
        myform = self.project+"/signup/forms.py"
        signform = """
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )
        """
        with open(myform, 'a') as sform:
            sform.write(signform)
 
        # write signup.html for basic signup view
        myindex = self.project+"/signup/templates/signup.html"
        signindex = """
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
        with open(myindex, 'w') as f:
            f.write(signindex)
        # write thanks.html for misc views
        mythanks = self.project+"/signup/templates/thanks.html"
        thanksindex = """
{% extends 'base.html' %}
{% block content %}
<p>Thanks. Your information has been added.</p>
{% endblock %}
        """
        with open(mythanks, 'w') as g:
            g.write(thanksindex)
        # model for signup
        mymodel = self.project+"/signup/models.py"
        signmodel = """
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
        with open(mymodel, 'a') as smodel:
            smodel.write(signmodel)
        # write base.html for signup view
        base = self.project+"/signup/templates/base.html"
        with open(base, 'w') as b:
            b.write(self.boot_strap)
        # write admin.py for signup view
        adminstuff = self.project+"/signup/admin.py"
        admindata = """
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
        with open(adminstuff, 'a') as adm:
            adm.write(admindata)

    def blog(self):
        # Create Django Blog
        subprocess.call(['django-admin', 'startapp', 'blog'], cwd=self.project)
        mpath = self.project+"/"+"blog/templates/blog"
        if not os.path.exists(mpath):
            os.makedirs(mpath)
        # write views.py for blog blogview
        myview = self.project+"/blog/views.py"
        with open(myview, 'a') as file:
            file.write(blogviews)
        # write models.py for blog blogmodel
        mymodel = self.project+"/blog/models.py"
        with open(mymodel, 'a') as file:
            file.write(blogmodel)
        # write admin.py for blog blogadmin
        myadmin = self.project+"/blog/admin.py"
        with open(myadmin, 'a') as file:
            file.write(blogadmin)
        # write forms.py for blog blogforms
        myforms = self.project+"/blog/forms.py"
        with open(myforms, 'w') as file:
            file.write(blogforms)
        # write urls.py for blog blogurls
        myurls = self.project+"/blog/urls.py"
        with open(myurls, 'a') as file:
            file.write(blogurls)
        # post_list.html for blog post_list
        mypostlist = self.project+"/blog/templates/blog/post_list.html"
        with open(mypostlist, 'w') as file:
            file.write(postlist)
        # post_detail.html for blog post_detail
        mypostdetail = self.project+"/blog/templates/blog/post_detail.html"
        with open(mypostdetail, 'w') as file:
            file.write(postdetail)
        # postcomment.html for blog in root templates
        mypostcomment = self.project+"/templates/postcomment.html"
        with open(mypostcomment, 'w') as file:
            file.write(postcomment)

    def clean(self):
        # create clean.py utility for cleanup all files
        with open('clean.py', 'w') as file:
            file.write(self.z_clean)

    def url(self):
        # Login / Logout function
        mpath = self.project + "/" + self.project + "/" + "urls.py"
        newpath = self.project + "/" + self.project + "/" + "test.dat"
        shutil.move(mpath, newpath)
        ar = []
        # newimport = "from django.contrib.auth import views as auth_views\nimport basicapp.views\n\n"
        # read urls.py
        with open(newpath, 'r') as f:
            for i in f:
                ar.append(i)
                if 'import admin' in i:
                    ar.append(self.root_url_import)
                if 'urlpatterns =' in i:
                    ar.append(self.root_url)
        # print ar # debug only
        print("Adjusted URLS for login Apps: %s" % mpath)
        # write rooturlimport and rooturls to the root urls.py
        with open(mpath, 'a') as w:
            for z in ar:
                if z[:4] == '    ':
                    w.write("\t" + z[4:])
                else:
                    w.write(z)

    def settings(self):
        # basic setup for settings
        mpath = self.project + "/" + self.project + "/" + "settings.py"
        newpath = self.project + "/" + self.project + "/" + "test.set"
        shutil.move(mpath, newpath)
        ar = []
        # read settings.py
        with open(newpath, 'r') as f:
            for i in f:
                if 'os.path.abspath' in i:
                    ar.append(self.setpath)
                elif 'DIRS' in i:
                    fix = i.replace("'DIRS': [],","'DIRS': [TEMPLATE_DIR],")
                    ar.append(fix)
                elif 'STATIC_URL =' in i:
                    ar.append(self.set_url)
                elif 'django.contrib.staticfiles' in i: # create apps before adding
                    ar.append(self.set_app)
                else:
                    ar.append(i)
        # write settings.py need setpath,seturl and setapp from global
        with open(mpath, 'a') as w:
            for z in ar:
                w.write(z)

        bpath = self.project+"/"+"templates"
        if not os.path.exists(bpath):
            os.makedirs(bpath)
            os.makedirs(bpath+"/registration")
        # write login.html in registration logindata
        loginFile = self.project+"/templates/registration/login.html"
        with open(loginFile,"w") as loginT:
            loginT.write(self.login_data)
        # write base.html below registration bootstrap
        bootFile = self.project+"/templates/base.html"
        with open(bootFile, "w") as bootT:
            bootT.write(self.boot_strap)
        print("Adjusted features for settings: %s" % mpath)

    def run(self):
        self.clean()
        self.project_create()
        self.signup()
        self.basic_app()
        self.url()
        self.settings()
        self.blog()


if __name__ == "__main__":
    project = input("Enter your Django Project Name: ")
    newsite = Rapid(bootstrap, indexdata, logindata, basicview, zclean, project, rooturl, setpath, seturl, setapp, rooturlimport)
    newsite.run()


