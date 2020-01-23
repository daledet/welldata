from django.db import models


class Well(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Survey(models.Model):
    survey = models.CharField(max_length=50)
    measured_depth = models.FloatField(max_length=10)
    inclination = models.FloatField(max_length=10)
    azimuth = models.FloatField(max_length=10)
    well = models.ForeignKey(Well, on_delete=models.DO_NOTHING)
