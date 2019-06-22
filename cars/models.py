import uuid

from django.db import models


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mark = models.CharField(max_length=24)
    model_car = models.ForeignKey('ModelCar', default='',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.mark


class ModelCar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.CharField(max_length=24)

    def __str__(self):
        return self.model
