from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_nome_app, name='inicio_nome_app')
]