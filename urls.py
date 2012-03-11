from django.conf.urls.defaults import * #patterns, include, url,
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'agenda.views.lista'),
    (r'^adiciona/$', 'agenda.views.adiciona'),
    (r'^item/(?P<nr_item>\d+)/$', 'agenda.views.item'),
    # Examples:
    # url(r'^$', 'gerenciador.views.home', name='home'),
    # url(r'^gerenciador/', include('gerenciador.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
)
