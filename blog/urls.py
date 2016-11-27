from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

import blog.views


urlpatterns = [
    url(r'^articles/all/$', blog.views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', blog.views.article),
    url(r'^$', blog.views.articles),
]

urlpatterns += staticfiles_urlpatterns()
