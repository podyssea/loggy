from django.db import models

# Create your models here.
class Workout(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)