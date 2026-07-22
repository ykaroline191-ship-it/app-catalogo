from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detalhes, name="detalhes"),
  path("cadastro/", views.cadastrar_obra, name="cadastro"),
]