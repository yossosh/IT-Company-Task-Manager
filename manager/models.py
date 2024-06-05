from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
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


class Tag(models.Model):
    """
    Represents a tag that can be used to categorize and filter tasks.
    """

    name = models.CharField(max_length=255, verbose_name="Tag Name")

    class Meta:
        ordering = ["name"]
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    """
    Extends the AbstractUser model to include a foreign key to Position.
    """

    default_position = Position.objects.get_or_create(
        name="Default Position"
    )[0].id
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name="Position",
        related_name="workers",
        default=default_position,
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
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ["deadline", "priority"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name

    def clean(self):
        # Ensure the deadline is not in the past
        if self.deadline < timezone.now().date():
            raise ValidationError("The deadline cannot be in the past.")
