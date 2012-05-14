from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'main.views.logout'),
    (r'^loggedout/$', 'main.views.loggedout'),
    (r'^register/$', 'main.views.register'),
    (r'^register/create_user/$', 'main.views.create_user'),
    # url(r'^authentic/', include('authentic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

