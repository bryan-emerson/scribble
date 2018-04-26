from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts$', views.post_list, name='post_list'),
    url(r'^posts/(?P<primary_key>\d+)$', views.post_detail, name='post_detail'),
    url(r'^posts/new$', views.post_create, name='post_create')
]
