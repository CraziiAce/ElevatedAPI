from django.urls import path

from . import views

urlpatterns = [
    path('communism', views.communism, name='communism'),
]
