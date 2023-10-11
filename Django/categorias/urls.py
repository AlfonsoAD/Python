from django.urls import path
from . import views

app_name = "categorias"

urlpatterns = [
    path('', views.index, name="index"),
    path("formulario", views.formulario, name='formulario'),
    path('<int:categoria_id>', views.detalle_categoria, name="detalle"),
    path('edit/<int:categoria_id>', views.editar_categoria, name="editar"),
    path('delete/<int:categoria_id>', views.eliminar_categoria, name="eliminar")
]
