from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from sigemh.core.views import BaseView
from sigemh.sectors.models import Sector
from django.urls import reverse_lazy


class SectorListView(BaseView, ListView):

    model = Sector
    template_name = 'sectors/list.html'


sector_list = SectorListView.as_view()


class SectorBaseView(BaseView):

    model = Sector
    fields = ['name']
    template_name = 'sectors/form.html'
    success_url = reverse_lazy('sectors:list')


class SectorCreateView(SectorBaseView, CreateView):
    pass


sector_create = SectorCreateView.as_view()


class SectorUpdateView(SectorBaseView, UpdateView):
    pass


sector_update = SectorUpdateView.as_view()


class SectorDeleteView(BaseView, DeleteView):

    model = Sector
    template_name = 'sectors/delete.html'
    success_url = reverse_lazy('sectors:list')

    # def delete(self, request, *args, **kwargs):
    #     sector = Sector.objects.get(pk=self.kwargs['pk'])
    #     sector.delete()

    #     return super(SectorDeleteView, self).delete(request, *args, **kwargs)


sector_delete = SectorDeleteView.as_view()



