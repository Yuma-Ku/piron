from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_action),
    path('demo/edit', views.demo_action)
]
