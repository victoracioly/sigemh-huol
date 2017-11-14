from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from sigemh.core.views import BaseView
from sigemh.functionaries.models import Functionary
from django.urls import reverse_lazy


class FunctionaryListView(BaseView, ListView):

    model = Functionary
    template_name = 'functionaries/list.html'


functionary_list = FunctionaryListView.as_view()


class FunctionaryBaseView(BaseView):

    model = Functionary
    fields = ['name']
    template_name = 'functionaries/form.html'
    success_url = reverse_lazy('functionaries:list')


class FunctionaryCreateView(FunctionaryBaseView, CreateView):
    pass


functionary_create = FunctionaryCreateView.as_view()


class FunctionaryUpdateView(FunctionaryBaseView,UpdateView):
    pass


functionary_update = FunctionaryUpdateView.as_view()


class FunctionaryDeleteView(BaseView, DeleteView):

    model = Functionary
    template_name = 'functionaries/delete.html'
    success_url = reverse_lazy('functionaries:list')

    # def delete(self, request, *args, **kwargs):
    #     sector = Sector.objects.get(pk=self.kwargs['pk'])
    #     sector.delete()

    #     return super(SectorDeleteView, self).delete(request, *args, **kwargs)


functionary_delete = FunctionaryDeleteView.as_view()
