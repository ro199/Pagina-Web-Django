from django.shortcuts import render, redirect, get_object_or_404
from .forms import HeroeForm
from .models import Heroe
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    return render(request, "heroes/index.html")

def heroe_view(request):
    if request.method == "POST":
        form = HeroeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        form = HeroeForm()
    return render(request, "heroes/heroe_form.html", {"form": form})


def heroe_list(request):
    return render(request, "heroes/heroes_registrados.html", {"Heroes": Heroe.objects.all()})

def heroe_edit(request, id):
    heroe = Heroe.objects.get(pk=id)
    if request.method == 'GET':
        form = HeroeForm(instance=heroe)
    else:
        form = HeroeForm(request.POST, instance=heroe)
        if form.is_valid():
            form.save()
        return redirect("heroe_lista")
    return render(request, "heroes/heroe_form.html", {"form": form})

def heroe_delete(request, id):
    #heroe = Heroe.objects.get(id=id)
    heroe = get_object_or_404(Heroe, pk=id)
    if request.method == "POST":
        heroe.delete()
        return redirect("heroe_lista")
    return render(request, "heroes/heroe_delete.html", {"heroe": heroe})

class heroeList(ListView):
    model = Heroe
    template_name = 'heroes/heroes_registrados.html'

class heroeCreate(CreateView):
    model = Heroe
    form_class = HeroeForm
    template_name = "heroes/heroe_form.html"
    success_url = reverse_lazy("heroe_lista")

class heroreUpdate(UpdateView):
    model = Heroe
    form_class = HeroeForm
    template_name = "heroes/heroe_form.html"
    success_url = reverse_lazy("heroe_lista")

class heroeDelete(DeleteView):
    model = Heroe
    template_name = "heroes/heroe_delete.html"
    success_url = reverse_lazy("heroe_lista")