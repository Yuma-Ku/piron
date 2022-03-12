from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_action),
    path('postlive/', views.post_live_action)
]
