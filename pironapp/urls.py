from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from . import views

urlpatterns = [
    path('profile/', views.profile_action, name='profile'),
    path('post/',views.post_action),
    path('', views.home_action, name='home'),
    path('login/', views.login_action, name='login'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("images/favicon.ico"))),
    path('register/', views.register_action),
    path('register-2/', views.register2_action),
    path('register-3/', views.register3_action),
    path('logout/', views.logout_action),
    path('create/', views.create_action, name='create'),
    path('create/post', views.create_post_action, name='create'),
    path('create/live', views.create_live_action, name='create')
]

 