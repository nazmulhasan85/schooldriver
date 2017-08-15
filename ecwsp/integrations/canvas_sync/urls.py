from django.conf.urls import *
from ecwsp.integrations.canvas_sync import views

urlpatterns = [url
    (r'^setup/$', views.setup),
)
