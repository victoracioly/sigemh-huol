from django.db import models
from sigemh.core.models import ModelBase
from sigemh.sectors.models import Sector
from sigemh.equipments import signals


class EquipmentType(ModelBase):

    class Meta:
        verbose_name = 'Tipo de equipamento'
        verbose_name_plural = 'Tipos de equipamentos'

    name = models.CharField(verbose_name='Nome', max_length=75, unique=True)
    slug = models.SlugField(verbose_name='Slug', max_length=75, unique=True)

    @property
    def quantity(self):
        return self.equipments.count()

    def __str__(self):
        return self.name


models.signals.pre_save.connect(signals.pre_save_equipment_type, sender=EquipmentType)


class Equipment(ModelBase):

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    equipment_type = models.ForeignKey(EquipmentType, verbose_name='Tipo de equipamento', related_name='equipments')
    patrimony = models.CharField(verbose_name='Número de patrimônio', max_length=75, unique=True)
    serial_number = models.CharField(verbose_name='Número de série', max_length=75, unique=True)
    sector = models.ForeignKey(Sector, verbose_name='Setor', null=True, blank=True)

    #Ordenando de forma correta:
    def get_history(self):
        return self.history.all().order_by('-id')

    def __str__(self):
        return '{} - {}'.format(self.equipment_type.name, self.patrimony)

class EquipmentHistory(ModelBase):
    equipment = models.ForeignKey(Equipment,verbose_name='Equipamento',related_name='history')
    sector = models.ForeignKey(Sector, verbose_name='Setor')
    checkin = models.DateTimeField(verbose_name='Dia/Hora - Chegada',auto_now_add=True)
    checkout = models.DateTimeField(verbose_name='Dia/Hora - Saída', null=True, blank=True)


