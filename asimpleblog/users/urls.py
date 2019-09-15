from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('detail/<username>/', views.user_detail, name='user_detail'),
    # path('update/', views.user_update, name='user_update'),
    path('settings/profile/', views.settings_profile, name='settings_profile'),
    path('settings/picture/', views.settings_picture, name='settings_picture'),
    path('settings/upload_picture/', views.upload_picture,
         name='settings_upload_picture'),
]
