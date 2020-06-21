
from django.conf.urls import url, include

from blog.views import PostListView
from blog.views import PostDetailView
from blog.views import PostCommentView

urlpatterns = [
    url(r'^$',PostListView.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$',PostDetailView.as_view(), name='post-detail'),
    url(r'^(?P<pk>\d+)/comment/$',PostCommentView,name='postcomment'),
]
