from django.urls import path

from . import views

urlpatterns = [
    path("", views.dash, name="dashboard"),
]
