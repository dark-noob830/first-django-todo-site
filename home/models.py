from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
# Create your models here.
