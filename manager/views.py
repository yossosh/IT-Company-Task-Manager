from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from manager.models import Position, TaskType, Tag, Worker, Task


@login_required
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


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    queryset = Position.objects.order_by("id")
    paginate_by = 5
    context_object_name = "positions"


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")
    template_name = "manager/position_form.html"


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")
    template_name = "manager/position_form.html"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    template_name = "manager/position_confirm_delete.html"
    success_url = reverse_lazy("manager:position-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    queryset = TaskType.objects.order_by("id")
    paginate_by = 5
    context_object_name = "task_types"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:tasktype-list")
    template_name = "manager/tasktype_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:tasktype-list")
    template_name = "manager/tasktype_form.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "manager/tasktype_confirm_delete.html"
    success_url = reverse_lazy("manager:tasktype-list")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    queryset = Tag.objects.order_by("id")
    paginate_by = 5
    context_object_name = "tags"


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("manager:tag-list")
    template_name = "manager/tag_form.html"


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("manager:tag-list")
    template_name = "manager/tag_form.html"


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    template_name = "manager/tag_confirm_delete.html"
    success_url = reverse_lazy("manager:tag-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    queryset = Worker.objects.order_by("id", "position")
    paginate_by = 5
    context_object_name = "workers"


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    context_object_name = "worker"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        worker = self.get_object()
        context["completed_tasks"] = worker.tasks.filter(is_completed=True)
        context["not_completed_tasks"] = worker.tasks.filter(
            is_completed=False
        )
        return context


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("manager:worker-list")
    template_name = "manager/worker_form.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("manager:worker-list")
    template_name = "manager/worker_form.html"


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    template_name = "manager/worker_confirm_delete.html"
    success_url = reverse_lazy("manager:worker-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.order_by("deadline")
    paginate_by = 5
    context_object_name = "tasks"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "manager/task_confirm_delete.html"
    success_url = reverse_lazy("manager:task-list")


class TasksThisWeekView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "manager/tasks_this_week.html"
    context_object_name = "tasks"

    def get_queryset(self):
        today = timezone.now().date()
        start_of_week = today - timezone.timedelta(days=today.weekday())
        end_of_week = start_of_week + timezone.timedelta(days=6)
        return Task.objects.filter(
            deadline__range=[start_of_week, end_of_week]
        )


class SearchTasksByTagsView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "manager/search_tasks_by_tags.html"
    context_object_name = "tasks"

    def get_queryset(self):
        tags = self.request.GET.getlist("tags")
        if tags:
            return Task.objects.filter(tags__name__in=tags).distinct()
        return Task.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
