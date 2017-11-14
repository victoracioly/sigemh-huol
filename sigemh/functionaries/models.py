from django.db import models
from sigemh.core.models import ModelBase


class Functionary(ModelBase):

    class Meta:
        verbose_name = 'Funcinário'
        verbose_name_plural = 'Funcionários'

    name = models.CharField(verbose_name='Nome', max_length=75)


    def __str__(self):
        return self.name
