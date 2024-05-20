from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    """
    Represents a job position within the organization.
    """

    name = models.CharField(max_length=255, verbose_name="Position Name")

    class Meta:
        ordering = ["name"]
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.name


class TaskType(models.Model):
    """
    Represents different types of tasks that can be assigned to workers.
    """

    name = models.CharField(max_length=255, verbose_name="Task Type")

    class Meta:
        ordering = ["name"]
        verbose_name = "Task Type"
        verbose_name_plural = "Task Types"

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    """
    Extends the AbstractUser model to include a foreign key to Position.
    """

    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name="Position",
        related_name="workers",
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return f"{self.username}: {self.last_name} {self.first_name}"


class Task(models.Model):
    """
    Represents a task that can be assigned to workers.
    """

    PRIORITY_CHOICES = [
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
        ("Planning", "Planning"),
    ]

    name = models.CharField(max_length=255, verbose_name="Task Name")
    description = models.TextField(verbose_name="Task Description")
    deadline = models.DateField(verbose_name="Deadline")
    is_completed = models.BooleanField(
        default=False, verbose_name="Is Completed"
    )
    priority = models.CharField(
        max_length=255, choices=PRIORITY_CHOICES, verbose_name="Priority"
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        verbose_name="Task Type",
        related_name="tasks",
    )
    assignees = models.ManyToManyField(
        Worker, verbose_name="Assignees", related_name="tasks"
    )

    class Meta:
        ordering = ["deadline", "priority"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name
