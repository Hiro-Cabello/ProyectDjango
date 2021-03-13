from django.urls import path 
from django.views.generic import TemplateView

from posts import views 

urlpatterns = [
    #path('posts/', posts_views.list_posts),
    path(
        route='',
        view= views.PostsFeedView.as_view(),
        name='feed'),
    path(
        route='posts/', 
        view=views.PostsFeedView.as_view(),
        name='feed'),
    path(
        route= 'posts/new/',
        view=views.create_post,
        name='create_post'),

    path(
        route='posts/<int:pk>',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    path(
        route='posts/featured/',
        view=TemplateView.as_view(template_name='posts/featured.html'),
        name='featured'
    )

]

"""
http://ccbv.co.uk/
https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#templateview
https://docs.djangoproject.com/en/3.0/topics/class-based-views/

"""