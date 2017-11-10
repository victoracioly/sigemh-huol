from django.db import models


class ModelBase(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')
