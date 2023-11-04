from django.db import models


class Realisation(models.Model):
    titre = models.CharField(max_length=100)
    image_url = models.CharField(max_length=1000)
    description = models.TextField()
