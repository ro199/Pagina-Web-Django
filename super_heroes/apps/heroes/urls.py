from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('nuevo', views.heroeCreate.as_view(), name="heroe_crear"),
    path('listar', views.heroeList.as_view(), name="heroe_lista"),
    path('editar/<int:pk>/', views.heroreUpdate.as_view(), name="heroe_editar"),
    path('eliminar/<int:pk>/', views.heroeDelete.as_view(), name="heroe_eliminar"),
]
