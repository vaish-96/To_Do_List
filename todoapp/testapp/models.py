from django.db import models

# Create your models here.
class Add(models.Model):
    title = models.CharField(max_length=255)

    