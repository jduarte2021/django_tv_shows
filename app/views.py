
from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):

    return redirect("/shows")


def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)


def agregar(request):
    print(request.POST)
    context = {}
            
    return render(request, 'agregar.html', context)




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
        messages.success(request,"Edicion satisfactoria")
        return redirect(f"/shows/{id}")
    else:
        
        context = {
                'datos' : Show.objects.get(id=id),
        }

        return render(request, 'editar.html', context)


def borrar(request,id):
    borrar = Show.objects.filter(id=id).delete()
    messages.error(request, "SHOW eliminado")

    return redirect("/shows")



def crear_show(request):
    print(request.POST)

    errores = Show.objects.validador(request.POST)

    if len(errores) > 0:
        for key, value in errores.items():
            messages.error(request,value)
        
        request.session['show_title'] = request.POST['title']
        request.session['show_network'] = request.POST['network']
        request.session['show_fecha'] = request.POST['fecha']
        request.session['show_descripcion'] = request.POST['descripcion']

        return redirect("/shows/agregar")

    else:
        request.session['show_title'] = ""
        request.session['show_network'] = ""
        request.session['show_fecha'] = ""
        request.session['show_descripcion'] = ""


        programa = Show.objects.create(
                            title=request.POST['title'],
                            network=request.POST['network'],
                            fecha=request.POST['fecha'],
                            descripcion=request.POST['descripcion'],
                            )

        messages.success(request, "Titulo agregado con exito" + programa.title)
        return redirect(f"/shows/{programa.id}")