from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path('busquedaPosts/',views.busquedaPosts),
    path('postRead/',views.postRead),
    path('verPosts/',views.verPosts),
    path('crearPost/',views.crearPost),
    path('editarPost/',views.crearPost),
    path('eliminarPost/',views.eliminarPost)
]
