from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^[home]?$', 'datavis.views.index'),
    url(r'^settings/', 'datavis.views.settings'),
    url(r'^visualization/', 'datavis.views.visualize'),
)
