from django.http import HttpResponse
from django.shortcuts import render

from manager.models import Position, TaskType, Worker, Task


def home(request) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_positions = Position.objects.count()
    num_tasks = Task.objects.count()
    num_task_types = TaskType.objects.count()
    return render(
        request,
        "manager/home.html",
        {
            "num_workers": num_workers,
            "num_positions": num_positions,
            "num_tasks": num_tasks,
            "num_task_types": num_task_types,
        },
    )
