from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from . import views

urlpatterns = [
    path('profile/', views.profile_action),
    path('post/',views.post_action),
    path('login/', views.login_action),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("images/favicon.ico")))
]

 