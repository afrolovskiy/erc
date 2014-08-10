from django.conf.urls import patterns, include, url
from django.contrib import admin

from erc import views


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
)
