from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name='blog-home'),
    path("post/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("about/", views.about, name='blog-about'),
]


#<app>/<model>_<viewtype>.html
#blog/post_list.html


#int=integer
#pk = primary key -- that's what detailview expects to be in order to grab specific object