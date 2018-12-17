from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<pk>/detail/', views.post_detail, name='post_detail'),
]
