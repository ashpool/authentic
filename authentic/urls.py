from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'main.views.logout'),
    (r'^loggedout/$', 'main.views.loggedout'),
    # url(r'^authentic/', include('authentic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
