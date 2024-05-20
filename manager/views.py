from django.http import HttpResponse
from django.shortcuts import render

from manager.models import Position, TaskType, Worker, Task


def home(request) -> HttpResponse:
    """View function for the home page of the site."""

    return render(
        request,
        "manager/home.html",
        {
            "num_workers": Worker.objects.count(),
            "num_positions": Position.objects.count(),
            "num_tasks": Task.objects.count(),
            "num_task_types": TaskType.objects.count(),
        },
    )
