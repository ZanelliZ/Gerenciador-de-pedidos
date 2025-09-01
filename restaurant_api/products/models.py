from django.db import models
from datetime import timedelta

class Category(models.Model):
    name = models.CharField(unique=True, max_length=100, default='', verbose_name="Nome do Item") 


class Product(models.Model):
    name = models.CharField(unique=True, max_length=100, default='', verbose_name="Nome do Item") 
    description = models.TextField(default='', verbose_name="Descrição")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço")
    average_prep_time = models.DurationField(default=timedelta(minutes=20), verbose_name="Tempo Médio de Preparo", help_text="Tempo estimado que o prato leva para ficar pronto.")
    serving_size = models.PositiveSmallIntegerField(default=1, verbose_name="Serve (pessoas)", help_text="Quantidade de pessoas que o prato serve."
)
    
    class Meta:
        verbose_name = "Item do Cardápio"
        verbose_name_plural = "Itens do Cardápio"
        ordering = ['name']

    def __str__(self):
        return f' {self.name} - R$ {self.price}'