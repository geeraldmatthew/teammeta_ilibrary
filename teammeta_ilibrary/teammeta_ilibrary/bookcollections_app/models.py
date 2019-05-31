from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=250)
	author = models.CharField(max_length=250)
	publisher = models.CharField(max_length=250)
	publication_year = models.PositiveIntegerField()
	isbn = models.CharField(max_length=250, blank=True, null=True)
	notes = models.TextField(max_length=2500, blank=True, null=True)

# Create your models here.
