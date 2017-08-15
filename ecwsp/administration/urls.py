from django.conf.urls import *
from responsive_dashboard.views import generate_dashboard

urlpatterns = [url
    (r'^$', generate_dashboard, {'app_name': 'administration'}),
)
