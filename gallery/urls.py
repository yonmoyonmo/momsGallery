from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_single, name='post_single'),
    path('post/upload/', views.post_upload, name='post_upload'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    path('login/', views.login, name='login'),
    url(r'^post/(?P<pk>\d+)/comment/$',
        views.add_comment_to_post, name='add_comment_to_post'),
]
