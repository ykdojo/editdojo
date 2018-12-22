from django.db import models

class TodoItem(models.Model):
    content = models.TextField()
