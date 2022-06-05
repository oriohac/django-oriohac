from django.db import models

# Create your models here.
class Schools(models.Model):
    name = models.CharField(max_length=23)
    address = models.CharField(max_length=23)
    def __str__(self) -> str:
        return self.name
class Country(models.Model):
    name = models.CharField(max_length=23)
    def __str__(self) -> str:
        return self.name