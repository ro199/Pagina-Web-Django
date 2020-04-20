from django.shortcuts import render, redirect
from .forms import HeroeForm
from .models import Heroe

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
