from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from productos.forms import CategoriaForm, ProductoForm
from productos.models import Categoria

# Create your views here.


def index(request):
    categorias = Categoria.objects.all().values()
    print(categorias)
    return render(
        request,
        'index_categorias.html',
        context={'categorias': categorias}
    )

# agregar producto


def formulario(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/categorias")
    else:
        form = CategoriaForm()

    return render(
        request,
        'formulario_categoria.html',
        {'form': form}
    )

# get


def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, "detalle_categoria.html", context={'categoria': categoria})


# editar producto


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/categorias")
    else:
        form = CategoriaForm(instance=categoria)
    return render(
        request,
        'editar_categoria.html',
        {'form': form}
    )

# eliminar producto


def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return HttpResponseRedirect("/categorias")
    return render(request, 'eliminar_categoria.html', {'categoria': categoria})
