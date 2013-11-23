from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf import settings
from main.views import *




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sync.views.home', name='home'),
    # url(r'^sync/', include('sync.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',(r'^$',homeController),
			(r'^downloads/$',downloads),
              )



urlpatterns += patterns('',
               (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
              )
