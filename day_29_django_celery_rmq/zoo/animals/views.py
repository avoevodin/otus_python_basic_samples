from celery.result import AsyncResult
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from zoo import celery_app
from .models import Animal


def index(request: HttpRequest):
    animals = Animal.objects.select_related("kind").order_by("-id").all()
    context = {
        "animals": animals,
    }
    return render(request, "animals/index.html", context=context)


def details(request: HttpRequest, pk: int):
    animal = get_object_or_404(
        Animal.objects.select_related("kind", "details").prefetch_related("food"),
        pk=pk,
    )
    # print("animal.food_set", animal.food.all())
    context = {"animal": animal}
    return render(request, "animals/details.html", context=context)


def task_status(request: HttpRequest, task_id: str):
    task: AsyncResult = celery_app.AsyncResult(task_id)
    status = task.status

    context = {
        "task_id": task_id,
        "status": status,
    }

    return render(request, "animals/task_status.html", context=context)
