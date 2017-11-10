from django.contrib import admin
from sigemh.equipments.models import Equipment
from sigemh.equipments.models import EquipmentType


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):

    fields = ['name']
    list_display = ['name', 'slug']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):

    pass
