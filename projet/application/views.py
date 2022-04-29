from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AvionForm

from . import  models

# Create your views here.


def index(request):
    return render(request, "application/index.html")


def main(request):
    return render(request, "application/main.html")


def ajout(request):
    if request.method == "POST":
        form = AvionForm(request)
        if form.is_valid():
            avion = form.save()
            return HttpResponseRedirect("/application/")
        else:
            return render(request,"application/ajout.html",{"form": form})
    else :
        form = AvionForm()
        return render(request,"application/ajout.html",{"form" : form})


def traitement(request):
    lform = AvionForm(request.POST)
    if lform.is_valid():
        avion = lform.save()
        return HttpResponseRedirect("/application/")
    else:
        return render(request,"application/ajout.html",{"form": lform})


def affiche(request, id):
    avion = models.Avion.objects.get(pk=id)
    return render(request,"application/affiche.html",{"avion" : avion})


def delete(request, id):
    avion = models.Avion.objects.get(pk=id)
    avion.delete()
    return HttpResponseRedirect("/application/")


def update(request, id):
    avion = models.Avion.objects.get(pk=id)
    lform = AvionForm(avion.dico())
    return render(request, "application/update.html", {"form": lform, "id": id})


def traitementupdate(request, id):
    lform = AvionForm(request.POST)
    if lform.is_valid():
        avion = lform.save(commit=False)
        avion.id = id
        avion.save()
        return HttpResponseRedirect("/application/")
    else:
        return render(request, "application/update.html", {"form": lform, "id": id})


def showall(request):
    liste = list(models.Avion.object.all())
    return render(request, "showall.html", {"liste": liste})