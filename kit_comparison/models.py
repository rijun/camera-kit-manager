from django.db import models


class Lens(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    focal_length = models.CharField(max_length=10)
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

    def get_total_weight(self):
        return sum([x.weight for x in self.lenses.all()])

    def get_focal_range_plot(self):
        full_names = [f"{x.manufacturer} {x.name}" for x in self.lenses.all()]
        focal_lengths = [[int(l) for l in x.focal_length.split('-')] for x in self.lenses.all()]
