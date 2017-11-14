from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from sigemh.core.views import BaseView
from sigemh.equipments import models

# Este método lista todos os objetos que eu tenho no banco que foram passados pelo modelo EquipmentType
# Iniciamos com a listagem em texto, depois criamos as classes.
class EquipmentTypeListView(BaseView, ListView):

    model = models.EquipmentType
    template_name = 'equipments/list.html'


class EquipmentTypeDetailView(BaseView, DetailView):

    model = models.EquipmentType
    template_name = 'equipments/detail.html'

    def get_object(self, *args, **kwargs):
        from django.shortcuts import get_object_or_404
        return get_object_or_404(self.model.objects.all(), slug=self.kwargs['slug'])


equipment_type_detail = EquipmentTypeDetailView.as_view()

#------------------Criando e fazendo dos tipos de equipamentos

# Método que define a estrutura de view
class EquipmentTypeBaseView(BaseView):

    model = models.EquipmentType
    fields = ['name']
    template_name = 'equipments/form.html'
    success_url = reverse_lazy('equipments:list')

# Isso permite criar mais um tipo de equipamento. O primeiro argumento é a estrutura. O segundo é a função criar.
class EquipmentTypeCreateView(EquipmentTypeBaseView, CreateView):
    pass


equipment_type_create = EquipmentTypeCreateView.as_view()

# Isso cria a modificação dos nomes.
class EquipmentTypeUpdateView(EquipmentTypeBaseView, UpdateView):
    pass


equipment_type_update = EquipmentTypeUpdateView.as_view()

class EquipmentTypeDeleteView(EquipmentTypeBaseView,DeleteView):
    model = models.EquipmentType
    template_name = 'equipments/delete.html'
    success_url = reverse_lazy('equipments:list')
equipment_type_delete = EquipmentTypeDeleteView.as_view()


#--------------------------------Criando os equipamentos

class EquipmentCreateView(BaseView,CreateView,DetailView):

    model = models.Equipment
    fields = ['equipment_type','patrimony','serial_number','sector']
    template_name = 'equipments/form_equipment.html'
    success_url = reverse_lazy('equipments:list')

# Usamos este método da Class BaseView para relacionar foreingkey com PrimaryKey
    def get_object(self, *args, **kwargs):
        from django.shortcuts import get_object_or_404
        return get_object_or_404(models.EquipmentType.objects.all(), pk=self.kwargs['pk'])

equipment_create = EquipmentCreateView.as_view()


