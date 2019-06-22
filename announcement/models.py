import uuid

from django.db import models

from cars.models import Car, ModelCar

import datetime

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mark = models.ForeignKey(Car, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelCar, default=None, on_delete=models.CASCADE)
    year_of_issue = models.IntegerField('year_of_issue',
                                        choices=YEAR_CHOICES,
                                        default=datetime.datetime.now().year)
    color = models.CharField(max_length=24)
    number = models.IntegerField()
    date_theft = models.DateTimeField()
    description = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    # def __str__(self):
    #     return self.mark
