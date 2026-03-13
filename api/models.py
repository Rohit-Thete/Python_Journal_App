from django.db import models
from django.contrib.auth.models import User


class Journal(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='journals'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title