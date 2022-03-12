from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_action),
    path('post/',views.post_action),
    path('message/', views.message_action)
]
