from django.views import generic
from django.shortcuts import render

from manager.models import Position, TaskType, Worker, Task


def home(request):
    """View function for the home page of the site."""

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    return render(
        request,
        "manager/home.html",
        {
            "num_workers": Worker.objects.count(),
            "num_positions": Position.objects.count(),
            "num_tasks": Task.objects.count(),
            "num_task_types": TaskType.objects.count(),
            "num_visits": num_visits,
        },
    )


class PositionListView(generic.ListView):
    model = Position
    queryset = Position.objects.order_by("id")
    paginate_by = 5
    context_object_name = "positions"


class TaskTypeListView(generic.ListView):
    model = TaskType
    queryset = TaskType.objects.order_by("id")
    paginate_by = 5
    context_object_name = "task_types"


class WorkerListView(generic.ListView):
    model = Worker
    queryset = Worker.objects.order_by("id", "position")
    paginate_by = 5
    context_object_name = "workers"


class WorkerDetailView(generic.DetailView):
    model = Worker
    context_object_name = "worker"


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.order_by("deadline")
    paginate_by = 5
    context_object_name = "tasks"


class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = "task"
