from django.db import models


class Book(models.Model):
    authors = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.authors)} {str(self.title)} {str(self.year)}'
