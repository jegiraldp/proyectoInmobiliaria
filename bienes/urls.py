from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('personas/', views.personasForm, name='personas'),
    path('personas/listar', views.getpersonas, name='getpersonas'),
    path('personas/registrar', views.personasForm, name='personasForm'),
]