from django.conf.urls import patterns, include, url
import app1.urls

urlpatterns = patterns('',
    url(r'', include(app1.urls)),
)
