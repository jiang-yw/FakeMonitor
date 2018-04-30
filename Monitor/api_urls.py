
from django.conf.urls import url

import Monitor.views

urlpatterns = [

    url(r'client/config/(\d+)/$', Monitor.views.client_configs),
    url(r'client/service/report/$',Monitor.views.service_data_report),
]