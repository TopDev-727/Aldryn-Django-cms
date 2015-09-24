#-*- coding: utf-8 -*-
from django.conf.urls import url, include

from cms.sitemaps import CMSSitemap

from .views import check_uninstall_ok


urlpatterns = [
    # Not sure if we should hardcode admin path like this
    url(r'^admin/~cmscloud-api/check-uninstall/$', check_uninstall_ok),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^robots\.txt$', include('robots.urls')),
]
