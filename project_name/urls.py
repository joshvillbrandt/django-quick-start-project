from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', '{{ project_name }}.views.home'),
    
    # Include an application:
    # url(r'^app_name/', include('app_name.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
