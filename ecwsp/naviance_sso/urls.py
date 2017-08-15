from django.conf.urls import *
from ecwsp.naviance_sso import views

urlpatterns = [url
    (r'^login/$', views.login),
)
