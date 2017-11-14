from django.contrib import admin
from sigemh.functionaries.models import Functionary


@admin.register(Functionary)
class FunctionaryAdmin(admin.ModelAdmin):

    pass
