from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/agregar', views.agregar),
    path('shows/<int:id>/editar', views.editar),
    path('shows/<int:id>', views.mostrar),
    path('shows/<int:id>/borrar', views.borrar),
]
