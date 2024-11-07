from django.db import models
from django.urls import reverse

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

    

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})

