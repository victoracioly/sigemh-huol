from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from sigemh.core.views import BaseView
from sigemh.equipments import models

from django.db.models import Count


# Este método lista todos os objetos que eu tenho no banco que foram passados pelo modelo EquipmentType
# Iniciamos com a listagem em texto, depois criamos as classes.
class EquipmentTypeListView(BaseView, ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['new'] = True
        return context

    model = models.EquipmentType
    template_name = 'equipments/list.html'

class EquipmentTypeTransportListView(EquipmentTypeListView):

    #Tirando botão 'Adicionar' de Transporte
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['new'] = True
        return context

    def get_queryset(self):
        from django.db.models import Count
        return self.model.objects.filter(equipments__function='transport').distinct()#.aggregate(Count('quantity'))


class EquipmentTypeLoanListView(EquipmentTypeListView):

    #Tirando botão 'Adicionar' de Empreśtimo
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['new'] = True
        return context

    def get_queryset(self):
        from django.db.models import Count
        return self.model.objects.filter(equipments__function='loan').distinct()#.aggregate(Count('quantity'))


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


# Criando a modificação dos nomes.
class EquipmentTypeUpdateView(EquipmentTypeBaseView, UpdateView):
    pass


equipment_type_update = EquipmentTypeUpdateView.as_view()

class EquipmentTypeDeleteView(EquipmentTypeBaseView,DeleteView):
    model = models.EquipmentType
    template_name = 'equipments/delete.html'
    success_url = reverse_lazy('equipments:list')

equipment_type_delete = EquipmentTypeDeleteView.as_view()


#--------------------------------Criando os equipamentos
# Classe que mostra os atributos do equipamento
class EquipmentBaseView(BaseView,DetailView):

    model = models.Equipment
    fields = ['manufacturer','equipment_model','equipment_type', 'patrimony', 'serial_number','year_of_manufacture','function', 'sector']
    template_name = 'equipments/form_equipment.html'

    def get_success_url(self):
        return reverse_lazy('equipments:detail',args=[self.object.equipment_type.slug])


class EquipmentCreateView(EquipmentBaseView,CreateView):
    def get_object(self, *args, **kwargs):
        from django.shortcuts import get_object_or_404
        return get_object_or_404(models.EquipmentType.objects.all(), pk=self.kwargs['pk'])

    def get_form(self, form_class=None):
        from django import forms

        form_class = super(EquipmentCreateView, self).get_form()
        form_class.fields['equipment_type'].initial = self.object
        form_class.fields['equipment_type'].widget = forms.HiddenInput()

        return form_class

equipment_create = EquipmentCreateView.as_view()


class EquipmentUpdateView(EquipmentBaseView, UpdateView):
    #Permite editar somente os campos abaixo:
    #fields = ['patrimony', 'serial_number','function']
    fields = ['manufacturer', 'equipment_model', 'equipment_type', 'patrimony', 'serial_number', 'year_of_manufacture',
              'function', 'sector']
equipment_update = EquipmentUpdateView.as_view()


class EquipmentChangeSectorView(BaseView,UpdateView):

    model = models.Equipment
    fields = ['sector','order_of_service']
    template_name = 'equipments/change_sector.html'

    def form_valid(self, form):
        from datetime import datetime

        last_history = self.object.history.last()

        if last_history:
            last_history.checkout = datetime.now()
            last_history.save()

        self.object.history.create(sector=self.object.sector, checkin=datetime.now())

        return super(EquipmentChangeSectorView,self).form_valid(form)

    #Como a gente precisa passar o slug como parâmetro o sucess_url não funciona.
    def get_success_url(self):
        return reverse_lazy('equipments:detail',args=[self.object.equipment_type.slug])


equipment_change_sector = EquipmentChangeSectorView.as_view()

# Histórico dos equipamentos:
class EquipmentHistoryView(BaseView, DetailView):
    model = models.Equipment
    template_name = 'equipments/history.html'


equipment_history = EquipmentHistoryView.as_view()
