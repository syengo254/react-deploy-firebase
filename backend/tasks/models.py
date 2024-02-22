from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.TextField(null=False)
    done = models.BooleanField(default=False)
    due_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title[:20]
