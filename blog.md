# How to add a blog from scratch

Use this as a template to create other models. The example below will show you how to create a blog from scratch. 

Creating any model is a simple 5 step process 


1. Create the Model in models.py
2. Migrate the Model
3. Register the model in admin
4. Test the model in admin
5. Create the View to display the model

You will do this over and over again for every new model. 

# Model 

Change to the root directory of your project and run: python manage.py startapp blog

change directory again to blog/ and edit model.py add the following:

``` 
class Post(models.Model):
        title=models.CharField(max_length=60)
        body=models.TextField()
        created = models.DateTimeField(auto_now_add=True)
      	#author-models.ForeignKey('user.User') 
	author=models.CharField(default='author',max_length=60)
        slug=models.CharField(default='author',max_length=60)

        def __uniode__(self ):
                return self.title

        def __str__(self): # this needed for display in foreign fields like comment
                return self.title
```

Now add the blog in your projects settings.py file and add it as a last entry to INSTALLED_APPS. Dont forget 
the comma at the end. 

```
INSTALLED_APPS=[
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'blog',
]
```

# Migrate

Run the following in root project:

```
python manage.py makemigrations
python manage.py migrate
```

# Register 

Add the following to the admin.py file

```
from blog.models import Post
class PostAdmin(admin.ModelAdmin):
        list_display=["title"]

admin.site.register(Post,PostAdmin)
```

# Test

Visit the page located at http://127.0.0.1:/admin

You will need to run the server first: python manage.py runserver

After you log in click the blog and add new sample entries. 

# View 


## ListView
 
Change directory that contains the settings.py file and add the following to urls.py:

```
from django.conf.urls import url,include
urlpatterns=[ 
	url(r'^blog/', include('blog.urls')),
]
```

This will point to the urls file in the blog/ directory

Change to that directory now and create a new urls.py in that directory 

```
from django.conf.urls import url, include

from blog.views import PostListView
from blog.views import PostDetailView
from blog.views import PostCommentView

urlpatterns = [
        url(r'^$',PostListView.as_view(), name='post-list'),
]
```

Now that you have the corrected both url files, edit views.py with the following:

```
from django.views.generic.list import ListView
from blog.models import Post

class PostListView(ListView):
        model=Post
        paginate_by=3
        queryset=Post.objects.order_by('-created')
```


Now that you have the view created its time to create the template. 

Within the blog/ directory you will need to create /templates/blog/post_list.html

```
{% extends 'base.html' %}
{% block content %}
<h2>News</h2>

<ul>
{% for bpost in object_list %}
<li><p>Title: {{ bpost.title }}<br>Slug: {{ bpost.slug }}
<!-- uncomment line below after you create DetailView -->
<!-- <br><a href="/blog/{{ bpost.id }}/">Body</a></li> -->
{% empty %}
        <li>No articles yet.</li>
{% endfor %}
</ul>
```

{% endblock %}


You can also add the following below for pagination of articles. As long as its between block content and endblock.

```
{% if is_paginated %}
        {% if page_obj.has_previous %}
        <a href="/blog?page={{ page_obj.previous_page_number }}">prev</a>
        {% endif %}
        Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
        {% if page_obj.has_next %}
                <a href="/blog?page={{ page_obj.next_page_number }}">next</a>
        {% endif %}
{% endif %}
```
               
vist http://127.0.0.1/blog
 
## DetailView 

Add the following to views:

```
from django.views.generic.detail import DetailView
class PostDetailView(DetailView):
        model=Post
```

Add the following to blog/urls.py

```
from blog.views import PostDetailView
	url(r'^(?P<pk>\d+)/$',PostDetailView.as_view(), name='post-detail'),
```

Add the following to templates/blog/post_detail.html

```
{% extends 'base.html' %}
{% block content %}

<h2>News</h2>
<p><b>Title:{{ post.title }}</b></p>
<p>Slug:{{ post.slug}}</p>
<p>Author:<u> {{ post.author}}</u>
<br>Date:{{ post.created}}</p>
<p></p>
<p>{{ post.body}}</p>

{% endblock %}
```

You should now be able to visit the detail view of the blog

# Comments

```
class Comment(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        author=models.CharField(default='author',max_length=60)
        body=models.TextField()
        #post=models.ForeignKey(Post)
        #post=models.ForeignKey(Post, related_name='comments')
        post=models.ForeignKey('blog.post', related_name='comments')
        approved_comment=models.BooleanField(default=False)

        def __unicode__(self):
                return unicode("%s: %s" % (self.post,self.body[:60]))
```


## migrate comments
python manage.py makemigrations; python manage.py migrate

## admin.py

```
from blog.models import Comment

class CommentAdmin(admin.ModelAdmin):
        def post_name(self,instance):
                return instance.post.title
        list_display=["author","post_name" ]
        search_fields=["post_name"]
admin.site.register(Comment,CommentAdmin)
# test the form
```

Test the new model in admin

## forms.py

```
from django import forms
from blog.models import Comment
class PostComment(forms.ModelForm):
        class Meta:
                model=Comment
                fields = ['author','body',]
```                                                 

## views.py

```
from django.shortcuts import get_object_or_404, redirect
from blog.forms import PostComment

def PostCommentView(request,pk):
        post = get_object_or_404(Post,pk=pk)
        if request.method == 'POST':
                form = PostComment(request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.post = post
                        comment.save()
                        return redirect('/thanks/')
                        #return redirect('asdf.html',pk=post.pk)
        else:
                form = PostComment()
        return render(request, 'postcomment.html',{'form':form})
```


## urls.py

```
from blog.views import PostCommentView
url(r'^(?P<pk>\d+)/comment/$',PostCommentView,name='postcomment'),
```

## postcomment.html in root template not in blog directory

```
{% extends 'base.html' %}
{% block content %}

<form action="" method="post">{% csrf_token %}
        {{ form.as_p }}

    <input type="submit" value="Send message" />
</form>

{% endblock %}
```


## test the form

post-detail.html 

```
<h2>Comments:</h2>

{% for comment in post.comments.all %}
        <p>Author: <u>{{ comment.author }}</u>
        <br>Comment: {{ comment.body}}</p>
        <p></p>
{% endfor %}
```


# user integrations 

## views.py

Adjust PostCommentView and add the 3 statements below in the appropriate place

```
from django.contrib.auth.models import User
in PostCommentView()
	user=User.objects.get(pk=pk)
	print user.last_name
	comment.author=user
```
## models.py

You can adjust the model and change the ForeignKey to user. However this will alter the
table. You will need to run the migrate command again
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate blog 0001 or use the appropriate item in number 000x. You 
can find the results of the alter query in migrations directory /blog/migrations

if the table you created already exists you can fake the migration
ex: `python manage.py migrate --fake blog`

author.models.ForeignKey('author.User')

## forms.py

remove 'author' from the form
its possible you could also exclude=['author']


## control by relation of Profile

You might need to import Profile into the view. 

```
myedit=Profile.object.get(user=user)
print myedit.editor # this should be True or False
print myedit.user_id # this should be number value 1 or 2 for first 2 users
```

## control approved comments
```
 {% if user.is_authenticated or comment.approved_comment %}
```

