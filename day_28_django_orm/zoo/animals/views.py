from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpRequest

from .models import Animal


def index(request: HttpRequest):
    animals = Animal.objects.order_by("-id").all()
    context = {
        "animals": animals,
    }
    return render(request, "animals/index.html", context=context)


def details(request: HttpRequest, pk: int):
    animal = get_object_or_404(Animal, pk=pk)
    context = {"animal": animal}
    return render(request, "animals/details.html", context=context)
