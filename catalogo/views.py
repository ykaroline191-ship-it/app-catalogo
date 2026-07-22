from django.shortcuts import render, get_object_or_404, redirect
from .models import Obra
from .forms import ObraForm


def index(request):
    obras = Obra.objects.all()
    context = {
        "obras": obras,
    }

    return render(
        request,
        "catalogo/index.html",
        context
    )


def detalhes(request, id):
    obra = get_object_or_404(Obra, id=id)

    context = {
        "obra": obra,
    }

    return render(
        request,
        "catalogo/detalhes.html",
        context
    )


def cadastrar_obra(request):
    if request.method == "POST":
        form = ObraForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("catalogo:index")
    else:
        form = ObraForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "catalogo/cadastro.html",
        context
    )
