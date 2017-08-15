from django.conf.urls import *
from ecwsp.integrations.schoolreach import views

urlpatterns = [url
    (r'^setup/$', views.setup),
)
