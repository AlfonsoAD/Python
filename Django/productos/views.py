from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render

from productos.forms import ProductoForm
from .models import Producto

# Create your views here.

# productos


def index(request):
    productos = Producto.objects.all().values()
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    # Otra manera de manejar elemento inexsistente
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, "detalle.html", context={'producto': producto})

# agregar producto


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productos")
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )

# editar producto


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productos")
    else:
        form = ProductoForm(instance=producto)
    return render(
        request,
        'producto_editar.html',
        {'form': form}
    )

# eliminar producto


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return HttpResponseRedirect("/productos")
    return render(request, 'producto_eliminar.html', {'producto': producto})
    # Manejar error cuando no exista un elemento
    # try:
    #     producto = Producto.objects.get(id=producto_id)
    #     return render(request, "detalle.html", context={'producto': producto})
    # except Producto.DoesNotExist:
    #     raise Http404()

    # agregar values y usar la clase JsonResponse para devolver los datos en Json
    # convertir a lista los elementos y agregar safe=False

    # productos = Producto.objects.all().values()
    # return JsonResponse(list(productos), safe=False)

    # para mostrar los productos con puntaje igual o mayor "filter"
    # productos = Producto.objects.filter(puntaje=3)

    # para buscar elemenento en especifico se puede enviar el id o el pk (primary key)
    # productos = Producto.objects.get(id=1)
