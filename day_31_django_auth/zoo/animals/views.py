from celery.result import AsyncResult
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from zoo import celery_app
from .models import Animal, AnimalKind
from .forms import AnimalCreateForm


def task_status(request: HttpRequest, task_id: str):
    task: AsyncResult = celery_app.AsyncResult(task_id)
    status = task.status

    context = {
        "task_id": task_id,
        "status": status,
    }

    return render(request, "animals/task_status.html", context=context)


class AnimalListView(ListView):
    # model = Animal
    queryset = Animal.objects.select_related("kind").order_by("-id").all()
    # template_name = "animals/animal_list.html"  # by default
    # context_object_name = "animals"


class AnimalsKindListView(ListView):
    model = Animal
    queryset = Animal.objects.select_related("kind")

    def get_queryset(self):
        qs = super().get_queryset()
        kind: AnimalKind = get_object_or_404(AnimalKind, name=self.kwargs["kind_name"])
        return qs.filter(kind__name=kind.name)


class AnimalDetailView(DetailView):
    # model = Animal
    queryset = Animal.objects.select_related("kind", "details").prefetch_related("food")
    template_name = "animals/details.html"


class AnimalDeleteView(PermissionRequiredMixin, DeleteView):
    model = Animal
    success_url = reverse_lazy("animals:list")
    permission_required = ("animals.delete_animal",)

    def has_permission(self):
        prms = self.request.user.get_all_permissions()
        print("User perms: ", prms)
        return super().has_permission()


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    # fields = ["name", "age", "kind", "description"]
    success_url = reverse_lazy("animals:details")
    form_class = AnimalCreateForm

    def get_success_url(self):
        return reverse("animals:details", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        self.object: Animal = form.save(commit=False)
        self.object.created_at = timezone.now()
        self.object.save()
        return super().form_valid(form)


class AnimalKindsListView(ListView):
    model = AnimalKind
    template_name = "animals/animal_kinds.html"
    queryset = AnimalKind.objects.filter(deleted=False)


class AnimalKindDeleteView(DeleteView):
    model = AnimalKind
    template_name = "animals/animal_kind_confirm_delete.html"
    success_url = reverse_lazy("animals:animal-kinds")
    context_object_name = "kind"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object: AnimalKind
        self.object.deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)
