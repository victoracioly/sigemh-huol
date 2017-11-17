from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

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


class EquipmentChangeSectorView(BaseView,UpdateView):

    model = models.Equipment
    fields = ['sector']
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


def equipment_history(request,pk):
    context = {
        'object':models.Equipment.objects.get(pk=pk)
    }
    # context = {
    #     'object': {
    #         'name': 'Ventilador Mecânico',
    #         'patrimony': '12345',
    #         'history': [
    #             {
    #                 'sector': 'CENTRO CIRÚRGICO',
    #                 'checkin': '01/01/2017 00:01',
    #                 'checkout': '--/--/---- --:--'
    #             }, {
    #                 'sector': 'UTI',
    #                 'checkin': '02/01/2017 00:01',
    #                 'checkout': '05/01/2017 10:20'
    #             }, {
    #                 'sector': 'CARDIOLOGIA',
    #                 'checkin': '20/03/2017 00:01',
    #                 'checkout': '21/04/2017 10:20'
    #             },
    #         ]
    #     }
    # }
    return render(request,'equipments/history.html',context)

