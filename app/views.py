
from django.shortcuts import render, redirect
from .models import Show


def index(request):

    return redirect("/shows")


def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)


def agregar(request):
    if request.method == 'POST':
        programa = Show.objects.create(
                    title=request.POST['title'],
                    network=request.POST['network'],
                    fecha=request.POST['fecha'],
                    descripcion=request.POST['descripcion'],
                    )
        return redirect("/shows")

    else:
        
        return render(request, 'agregar.html')




def mostrar(request,id):
    context = {
        'program': Show.objects.filter(id=id),
    }
    return render(request, 'mostrar.html', context)


def editar(request,id):
    print(request.POST)
    if request.method == 'POST':
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.fecha = request.POST['fecha']
        show.descripcion = request.POST['descripcion']
        show.save()

        return redirect(f"/shows/{id}")
    else:
        
        context = {
                'datos' : Show.objects.get(id=id),
        }

        return render(request, 'editar.html', context)


def borrar(request,id):
    borrar = Show.objects.filter(id=id).delete()

    return redirect("/shows")

