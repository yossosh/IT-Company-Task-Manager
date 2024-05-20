from django.contrib import admin
from .models import Position, TaskType, Worker, Task


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "position")
    search_fields = (
        "username", "first_name", "last_name", "email", "position__name"
    )
    list_filter = ("position",)
    ordering = ("username",)
    list_select_related = ("position",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name", "deadline", "is_completed", "priority", "task_type"
    )
    search_fields = (
        "name", "description", "task_type__name", "assignees__username"
    )
    list_filter = ("is_completed", "priority", "task_type")
    ordering = ("deadline", "priority")
    filter_horizontal = ("assignees",)
    date_hierarchy = "deadline"
