from django.db import models
from datetime import timedelta


class Itens(models.Model):
    iten_name = models.CharField(unique=True,max_length=100, default='') 
    iten_description = models.TextField(default='')
    iten_price = models.DecimalField(max_digits=6, decimal_places=2)
    iten_average_prep_time = models.DurationField(default=timedelta(minutes=20))
    iten_serving_size = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'Name: {self.iten_name} | Price: {self.iten_price}'