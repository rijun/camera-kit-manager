from django.db import models

class Lens(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    focal_length = models.IntegerField()
    aperture = models.FloatField()
    weight = models.IntegerField()
    length = models.FloatField()
    diameter = models.FloatField()
    filter_size = models.IntegerField()

    def __str__(self):
        return f"{self.manufacturer} {self.name}"

    class Meta:
        verbose_name_plural = "Lenses"

class Kit(models.Model):
    lenses = models.ManyToManyField(Lens)
