from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^catalog/(?P<id>[0-9]+)$', views.catalog, name='catalog'),
    url(r'^info/(?P<id>[0-9]+)$', views.info, name='info'),
]