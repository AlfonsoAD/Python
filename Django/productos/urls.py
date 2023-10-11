from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('', views.index, name="index"),
    path("formulario", views.formulario, name='formulario'),
    path('<int:producto_id>', views.detalle, name="detalle"),
    path('edit/<int:producto_id>', views.editar_producto, name="editar"),
    path('delete/<int:producto_id>', views.eliminar_producto, name="eliminar")
]
