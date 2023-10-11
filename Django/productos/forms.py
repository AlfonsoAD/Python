from . import models
from django.forms import ModelForm


class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'puntaje', 'categoria']


class CategoriaForm(ModelForm):
    class Meta:
        model = models.Categoria
        fields = ["nombre"]
