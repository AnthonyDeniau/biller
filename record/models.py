from django.db import models

from user.models import User
from resource.models import Resource


class Records(models.Model):
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resources = models.ManyToManyField(Resource, through='ResourceUsed')


class ResourceUsed(models.Model):
    record = models.ForeignKey(Records, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    number = models.IntegerField()
