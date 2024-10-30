from django.db import models

class Lens(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    focal_length = models.IntegerField()
    #     "name": "24-70mm F2.8 DG DN II | Art",
    #     "manufacturer": "Sigma",
    #     "focal_length": [24, 70],
    #     "aperture": 2.8,
    aperture = models.FloatField()
    #     "weight": 745,
    weight = models.IntegerField()
    #     "length": 120.2,
    length = models.FloatField()
    #     "diameter": 87.8,
    diameter = models.FloatField()
    #     "filter_size": 82
    filter_size = models.IntegerField()

    def __str__(self):
        return f"{self.manufacturer} {self.name}"
