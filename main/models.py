from django.db import models


class Book(models.Model):
    authors = models.JSONField()
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


