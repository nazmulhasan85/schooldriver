from django.conf.urls import include,  url
from ecwsp.sis import views as sis_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from api.routers import api_urls
from responsive_dashboard import views as dashboard_views
from ecwsp.sis.views import AttendanceReportView
from django.http import HttpResponse

dajaxice_autodiscover()
admin.autodiscover()
admin.site.login = login_required(admin.site.login)

def robots(request):
    ''' Try to prevent search engines from indexing
    uploaded media. Make sure your web server is
    configured to deny directory listings. '''
    return HttpResponse(
        'User-agent: *\r\nDisallow: /media/\r\n',
        content_type='text/plain'
    )

urlpatterns =[
    url(r'^robots.txt', robots),
    url(r'^admin/', include("massadmin.urls")),
    url(r'^admin_export/', include("admin_export.urls")),
    url(r'^ckeditor/', include('ecwsp.ckeditor_urls')),#include('ckeditor.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^$', 'ecwsp.sis.views.index'),
    url(r'^sis/', include('ecwsp.sis.urls')),
    url(r'^admin/jsi18n', 'django.views.i18n.javascript_catalog'),

    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^simple_import/', include('simple_import.urls')),
    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change'),
    url(r'^accounts/password_change_done/$', 'django.contrib.auth.views.password_change_done', name="password_change_done"),

    url(r'^logout/$', sis_views.logout_view),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^admin/', include(admin.site.urls) ),
    url(r'^autocomplete/', include('dal.urls')),
    url(dajaxice_config.dajaxice_url, include('ecwsp.dajaxice_urls')),
    url(r'^reports/(?P<name>attendance_report)/$', AttendanceReportView.as_view()),
    url(r'^reports/', include('scaffold_report.urls')),
    url(r'^impersonate/', include('impersonate.urls')),
    url(r'^api/', include(api_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.GAPPS:
    urlpatterns += [url(r'^accounts/login/$', 'google_auth.views.login'), ]
else:
    urlpatterns += [ url(r'^accounts/login/$', 'django.contrib.auth.views.login'),]

if 'ldap_groups' in settings.INSTALLED_APPS:
    urlpatterns += [ url(r'^ldap_grp/', include('ldap_groups.urls'))]
if 'ecwsp.discipline' in settings.INSTALLED_APPS:
    urlpatterns += [ url(r'^discipline/', include('ecwsp.discipline.urls')), ]
if 'ecwsp.attendance' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^attendance/', include('ecwsp.attendance.urls')), ]
if 'ecwsp.schedule' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^schedule/', include('ecwsp.schedule.urls'))]
    # Course is a nicer looking url
    urlpatterns += [url(r'^course/', include('ecwsp.schedule.urls'))]
if 'ecwsp.grades' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^grades/', include('ecwsp.grades.urls'))]
    urlpatterns += [url(r'^course/', include('ecwsp.grades.urls'))]
if 'ecwsp.work_study' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^work_study/', include('ecwsp.work_study.urls'))]
if 'ecwsp.admissions' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^admissions/', include('ecwsp.admissions.urls'))]
if 'ecwsp.volunteer_track' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^volunteer_track/', include('ecwsp.volunteer_track.urls'))]
if 'ecwsp.benchmark_grade' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^benchmark_grade/', include('ecwsp.benchmark_grade.urls'))]
if 'ecwsp.inventory' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^inventory/', include('ecwsp.inventory.urls'))]
if 'ecwsp.engrade_sync' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^engrade_sync/', include('ecwsp.engrade_sync.urls'))]
if 'ecwsp.naviance_sso' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^naviance_sso/', include('ecwsp.naviance_sso.urls'))]
if 'ecwsp.alumni' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^alumni/', include('ecwsp.alumni.urls'))]
if 'ecwsp.counseling' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^counseling/', include('ecwsp.counseling.urls'))]
if 'ecwsp.integrations.canvas_sync' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^canvas_sync/', include('ecwsp.integrations.canvas_sync.urls'))]
if 'ecwsp.integrations.schoolreach' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^schoolreach/', include('ecwsp.integrations.schoolreach.urls'))]
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^rosetta/', include('rosetta.urls')),
    ]
if 'social.apps.django_app.default' in settings.INSTALLED_APPS:
    urlpatterns += [url(include('social.apps.django_app.urls', namespace='social')),]
if 'file_import' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^file_import/', include('file_import.urls')),]

urlpatterns += [url(r'^administration/', include('ecwsp.administration.urls'))]
urlpatterns += [url(r'^', include('responsive_dashboard.urls'))]

if settings.DEBUG:
    urlpatterns += [url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,})
    ]
