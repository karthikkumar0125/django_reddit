from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:pk>', views.posts_retrieve, name='posts_retrieve'),
    path('create', views.create, name='create'),
    path('create_post', views.create_post, name='create_post')
]