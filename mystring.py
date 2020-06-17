#!/usr/bin/python
# mystring.py
# list of strings html scripts and other python strings or templates
# William C. Gunnells
# http://www.rapidpythonprogramming


bootstrap = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">


    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>

<nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Project name</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="/signup/">Signup</a></li>
            <li><a href="/accounts/login/">Login</a></li>
            <li><a href="/blog/">Blog</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

<!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
        <h1>Hello, world!</h1>
        <p>This is a template for a simple marketing or informational website. It includes a large callout called a jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.</p>
        <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more &raquo;</a></p>
      </div>
    </div>

    <div class="container">
      <div class="starter-template">
	{% block content %}
	{% endblock %}
      </div>
    </div><!-- /.container -->

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

  </body>
</html>
"""

indexdata = """
{% extends 'base.html' %}
{% block content %}
<h2>Body Content</h2>
<p>Here is your basic page. Above you have Navigation bar, Jumbotron in the Header which contains 
'Hello, world!',<br> and additional space for marketing.</p> 
{% endblock %}
"""

logindata = """
{% extends 'base.html' %}
{% block title %}Login{% endblock %}
{% block content %}
<h2>Login</h2>
<form method="post">
{% csrf_token %}
{{ form.as_p }}
<button type="submit">Login</button>
</form>
{% endblock %}
"""

basicview = """
from django.shortcuts import render


def index(request):
    return render(None, "index.html")
"""

zclean = """
import os
import shutil


def clean():	
    my_clean = input("Enter name of project to erase: ")
    if os.path.exists(my_clean):
        print("erasing directory")
        shutil.rmtree(my_clean)


clean()
"""

rooturlimport = """from django.contrib.auth import views as auth_views
from django.conf.urls import include
import basicapp.views 
import signup.views
"""

rooturl = """
    path('accounts/login/', auth_views.LoginView.as_view()), 
    # url('logout/', auth_views.logout, name = 'logout'),# builtin 
    # url('logout/', auth_views.logout, {'template_name': 'logged_out.html'}, name = 'logout'),# page redirect 
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('', basicapp.views.index), 
    path('signup/', signup.views.Signup), 
    path('thanks/', signup.views.thanks), 
    path('blog/', include('blog.urls')), 

"""	

setpath = """
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')
MEDIA_DIR=os.path.join(BASE_DIR,'media')
LOGIN_REDIRECT_URL='/'
"""

seturl = """
STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIR=[STATIC_DIR,]
MEDIA_ROOT=MEDIA_DIR
MEDIA_URL='/media/'
"""

setapp = """
    'django.contrib.staticfiles',
    'basicapp',
    'signup',
    'blog',
"""

blogmodel = """

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # author-models.ForeignKey('user.User') 
    author = models.CharField(default='author', max_length=60)
    slug = models.CharField(default='author', max_length=60)
    
    # def approve_comments(self):
    #   return self.comments.filer(approved_comment=True)
    # from django.core.urlresolvers import reverse
    #
    # def get_absolute_url(self):
    #   return reverse("post_detail",kwargs={'pk':self.pk})
    
    def __uniode__(self):
        return self.title
    
    def __str__(self):  # this needed for display in foreign fields like comment
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # author=models.CharField(default='author',max_length=60)
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    body = models.TextField()
    # post=models.ForeignKey(Post)
    # post=models.ForeignKey(Post, related_name='comments')
    post = models.ForeignKey('blog.post', related_name='comments', on_delete=models.DO_NOTHING)
    approved_comment = models.BooleanField(default=False)
    
    # def approve(self):
    #     self.approved_comment=True
    #     self.save()
    # def get_absolute_url(self):
    #     return reverse('postcomment',kwargs={'pk':self.pk})
    def __unicode__(self):
        return unicode("%s: %s" % (self.post,self.body[:60]))
"""

blogforms = """
from django import forms
from blog.models import Comment


class PostComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]
"""

blogviews = """
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Post
from django.shortcuts import get_object_or_404, redirect
from blog.forms import PostComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from signup.models import Profile

class PostListView(ListView):
    model=Post
    paginate_by=3
    queryset=Post.objects.order_by('-created')
    # if you don't want queryset you ca add the following to model.
    # and it only works on date field
    # nested: class Meta:
    #     ordering = ['-created']
    
class PostDetailView(DetailView):
    model=Post


@login_required
def PostCommentView(request,pk):
    user=User.objects.get(pk=pk)
    myedit=Profile.objects.get(user=user)
    # print myedit.editor
    # print myedit.user_id
    # print user.last_name
    # print user.approved_comment
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author=user
            comment.save()
            return redirect('/thanks/')
            #return redirect('asdf.html',pk=post.pk)
    else:
        form = PostComment()
    return render(request, 'postcomment.html',{'form':form})

# def comment_approve(request,pk):
#     comment = get_object_or_404(Comment,pk=pk)
#     # comment.approve()
#     return redirect('post_detail', pk=post.pk)

"""

blogadmin = """
from blog.models import Comment

# Register your models here.

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display=["title"]

class CommentAdmin(admin.ModelAdmin):
    def post_name(self,instance):
        return instance.post.title
    list_display=["author","post_name" ]
    search_fields=["post_name"]


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
"""

blogurls = """
from django.conf.urls import url, include

from blog.views import PostListView
from blog.views import PostDetailView
from blog.views import PostCommentView

urlpatterns = [
    url(r'^$',PostListView.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$',PostDetailView.as_view(), name='post-detail'),
    url(r'^(?P<pk>\d+)/comment/$',PostCommentView,name='postcomment'),
]
"""

post_list = """
{% extends 'base.html' %}
{% block content %}
<h2>News</h2>
{% if user.is_staff %}
<a href="{% url 'admin:index' %}">Admin</a>
<a href="{% url 'admin:blog_post_add' %}">Add post</a>
{% endif %}

<p></p>

<ul>
{% for bpost in object_list %}
<li><p>Title: {{ bpost.title }}<br>Slug: {{ bpost.slug }}
<br><a href="/blog/{{ bpost.id }}/">Body</a></li>
{% empty %}
        <li>No articles yet.</li>
{% endfor %}
</ul>

{% endblock %}
"""

post_detail = """
{% extends 'base.html' %}
{% block content %}

<h2>News</h2>
<p><b>Title:{{ post.title }}</b></p>
<p>Slug:{{ post.slug}}</p>
<p>Author:<u> {{ post.author}}</u>
<br>Date:{{ post.created}}</p>
<p></p>
<p>{{ post.body}}</p>

<h2>Comments:</h2>

{% for comment in post.comments.all %}
	{% if comment.approved_comment %}
        <p>Author: <u>{{ comment.author }}</u>
        <br>Comment: {{ comment.body}}</p>
	{% endif %}
        <p></p>
{% endfor %}

<p><a href="/blog/{{ post.id }}/comment/">Add comment</a>

{% endblock %}
"""

post_comment = """
{% extends 'base.html' %}
{% block content %}


<form action="" method="post">{% csrf_token %}
        {{ form.as_p }}

    <input type="submit" value="Send message" />
</form>

{% endblock %}
"""

if __name__ == "__main__":
    pass
