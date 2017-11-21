from django.conf.urls import url
from sigemh.equipments.views import EquipmentTypeListView
from sigemh.equipments.views import EquipmentTypeTransportListView
from sigemh.equipments.views import EquipmentTypeLoanListView
from sigemh.equipments.views import equipment_create
from sigemh.equipments.views import equipment_update
from sigemh.equipments.views import equipment_type_create
from sigemh.equipments.views import equipment_type_detail
from sigemh.equipments.views import equipment_type_update
from sigemh.equipments.views import equipment_type_delete
from sigemh.equipments.views import equipment_change_sector
from sigemh.equipments.views import equipment_history





urlpatterns = [
    url(r'^(?P<pk>\d+)/novo/$', equipment_create, name='create_equipment'),
    url(r'^(?P<pk>\d+)/editar-equipamento/$', equipment_update, name='update_equipment'),
    url(r'^(?P<pk>\d+)/editar-setor/$', equipment_change_sector, name='change_sector'),
    url(r'^(?P<pk>\d+)/historico/$', equipment_history, name='history'),
    url(r'^$', EquipmentTypeListView.as_view(), name='list'),
    url(r'^transporte/$', EquipmentTypeTransportListView.as_view(), name='transport_list'),
    url(r'^emprestimo/$', EquipmentTypeLoanListView.as_view(), name='loan_list'),
    url(r'^novo/$', equipment_type_create, name='create'),
    url(r'^(?P<pk>\d+)/editar/$', equipment_type_update, name='update'),
    url(r'^(?P<pk>\d+)/deletar/$', equipment_type_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', equipment_type_detail, name='detail'),
]
