from django.db import models
from sigemh.core.models import ModelBase


class Sector(ModelBase):

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    name = models.CharField(verbose_name='Nome', max_length=75, unique=True)

    def __str__(self):
        return self.name

