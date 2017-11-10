from django.contrib import admin
from sigemh.sectors.models import Sector


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):

    pass
