from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('update/<pk>/', views.post_update, name='post_update'),
    path('delete/<pk>/', views.post_delete, name='post_delete'),
]
