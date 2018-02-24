from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/$', views.gallery, name = 'gallery'),
    url(r'^specialfeatures/$', views.specialfeatures, name = 'specialfeatures'),
]