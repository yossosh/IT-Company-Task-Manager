from django.urls import path

from manager.views import (
    home,
    PositionListView,
    TaskTypeListView,
    WorkerListView,
    WorkerDetailView,
    TaskListView,
    TaskDetailView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    PositionCreateView,
    PositionDeleteView,
    PositionUpdateView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TasksThisWeekView,
    SearchTasksByTagsView,
)

app_name = "manager"

urlpatterns = [
    path("", home, name="home"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task_types/", TaskTypeListView.as_view(), name="tasktype-list"),
    path(
        "task_type/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create"
    ),
    path(
        "task_type/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "task_type/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "worker/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "worker/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks-this-week/",
        TasksThisWeekView.as_view(),
        name="tasks-this-week"
    ),
    path(
        "search-tasks-by-tags/",
        SearchTasksByTagsView.as_view(),
        name="search-tasks-by-tags",
    ),
]
