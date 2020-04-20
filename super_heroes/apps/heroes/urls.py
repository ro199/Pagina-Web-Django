from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('nuevo', views.heroe_view, name="heroe_crear"),
    path('listar', views.heroe_list, name="heroe_lista"),
]
