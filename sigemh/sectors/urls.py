from django.conf.urls import url
from sigemh.sectors.views import sector_list
from sigemh.sectors.views import sector_create
from sigemh.sectors.views import sector_update
from sigemh.sectors.views import sector_delete


urlpatterns = [
    url(r'^$', sector_list, name='list'),
    url(r'^novo/$', sector_create, name='create'),
    url(r'^(?P<pk>\d+)/editar/$', sector_update, name='update'),
    url(r'^(?P<pk>\d+)/delete/$', sector_delete, name='delete'),
]
