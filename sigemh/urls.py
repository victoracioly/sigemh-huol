from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from sigemh.core.views import home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^equipamentos/', include('sigemh.equipments.urls', namespace='equipments')),
    url(r'^setores/', include('sigemh.sectors.urls', namespace='sectors')),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGIN_URL}, name='logout'),
    url(r'^admin/', admin.site.urls),
]
