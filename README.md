# Rapid Django Web Services

Rapid Django Web Services is a custom script that you can run on Windows
Linux or Mac OSX. The script creates a fully functional website complete
with a graphical Front-end, and graphical Back-end. Contained within
the script are as follows:
 
1. Singup Form - username, email,password1, password2
2. Login Form - username, password, /logout.
3. News Blog - Basic functional blog with comments
4. Bootstrap - getbootstrap.com Basic Template with jumbotron 
5. Media Content - 'static', and 'media' already configured
6. Graphical Static Page - flatpage function turned on so you can begin creating static flat pages that rarely change but use a graphical interface.
6. Profile Model - An extended user model linked to a user profile model.

# Why Did I Create this

Django is relatively easy to setup and configure. However I was tired of 
creating the same features for each new website I create. Nearly everyone
needs the six items I listed above. This script saves several hours of work and gives me the opportunity to create a new model specific for the customer and allows me to begin working on a flexible front end that can be changed easily. 

# Prerequisites

The following needs to be installed:

1. Python2 or Python3
2. Pip - This can be done through python easy\_install.
3. Django. After pip is installed you can run the following:
	pip install Django

# Installation

Download newrapidsetup.py and mystring.py 

If you run Python3.x. You need to edit the file and change the following:

At the bottom of newrapidsetup.py

Change: ```project=raw_input("Enter your Django Project Name: ")```

To: ```project=input("Enter your Django Project Name: ")```

Near the top of mystring.py

Change: ```myclean=raw_input("Enter name of project to erease: ")```

To: ```myclean=input("Enter name of project to erase: ")```


# Running the Script

Open a terminal and type 'python newrapidsetup.py'. The script will ask you
the name of your project. Type in the new name and wait a minute for the
script to populate a directory with everything setup

# Starting Django Web Server

You need to run the following commands first before starting the server
for the first time. 

1. 'python manage.py makemigrations'
2. 'python manage.py migrate'
3. 'python manage.py createsuperuser'

# Run the Server

1. 'python manage.py runserver'

Now visit the website using your browser: http://127.0.0.1:8000

Explore the site. You can add users, add news, and add comments. Currently
you have to be 'staff' to add news. As an administrator you can specify if the 
user or can have access to the blog model. 

Only users can add comments. This forces new users to sign up. The administrator specifies if the post comment is authorized or not.

Currently Blog posts can be added only through the admin tool. And news 
comments can be added using the admin tool or the form. 

You can create the same form for the news blog that appears the same for 
the comments form. It's a matter of creating, a new url, a new view method,
a new form method, and a new template. 

# New Models

Creating new models (database content) rapidly is the power of Django's ORM (Object Relational Mapper). If you know python you can write python instead of
verbose SQL statements. 

Creating a view without a model is simple. The basicapp that comes with 
this script shows an example of a view: 

'''def index(request):<br>
&nbsp;&nbsp;	return render_to_response("index.html")
'''

This method uses render\_to\_response library to point to a template index.html

The model.py however is a simplified script that abstracts the creating of SQL statements. Example:

'''
class Post(models.Model):
	title=models.CharField(max_length=60)
	body=models.TextField()
'''

The SQL command for the method listed above is as follows:

'''
CREATE TABLE "blog_post" ("id", integer NOT NULL PRIMARY KEY AUTOCREMENT,"title" varchar(60) NOT NULL, "body" text NOT NULL,); 
''' 
