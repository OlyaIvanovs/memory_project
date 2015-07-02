from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^memory/', include('memory_project.urls', namespace='memory')),
    url(r'^admin/', include(admin.site.urls)),
)
