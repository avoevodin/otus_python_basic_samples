from django.urls import path

from .views import (
    index,
    details,
    task_status,
    AnimalListView,
    AnimalsKindListView,
    AnimalDetailView,
    AnimalDeleteView,
    AnimalCreateView,
    AnimalKindsListView,
    AnimalKindDeleteView,
)

app_name = "animals"

urlpatterns = [
    # path("", index, name="list"),
    path("", AnimalListView.as_view(), name="list"),
    path("kinds", AnimalKindsListView.as_view(), name="animal-kinds"),
    path(
        "kinds/<int:pk>/confirm-delete",
        AnimalKindDeleteView.as_view(),
        name="animal-kind-delete",
    ),
    path("create/", AnimalCreateView.as_view(), name="create"),
    path("<int:pk>/", AnimalDetailView.as_view(), name="details"),
    path("<int:pk>/delete/", AnimalDeleteView.as_view(), name="delete"),
    path("<str:kind_name>", AnimalsKindListView.as_view(), name="kind-list"),
    # path("<int:pk>/", details, name="details"),
    # path("status/<str:task_id>/", task_status, name="task-status"),
]
