from django.conf.urls import url

from sigemh.functionaries.views import functionary_list
from sigemh.functionaries.views import functionary_create
from sigemh.functionaries.views import functionary_update
from sigemh.functionaries.views import functionary_delete

urlpatterns = [
    url(r'^$', functionary_list, name='list'),
    url(r'^novo/$', functionary_create, name='create'),
    url(r'^(?P<pk>\d+)/editar/$', functionary_update, name='update'),
    url(r'^(?P<pk>\d+)/delete/$', functionary_delete, name='delete'),
]