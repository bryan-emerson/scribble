from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^posts$', views.post_list, name='post_list'),
    url(r'^posts/(?P<primary_key>\d+)$', views.post_detail, name='post_detail'),
    url(r'^posts/new$', views.post_create, name='post_create'),
    url(r'^posts/(?P<primary_key>\d+)/comments/new$', views.comment_create, name='comment_create'),
    url(r'^posts/(?P<primary_key>\d+)/edit$', views.post_update, name='post_edit'),
    url(r'^posts/(?P<primary_key>\d+)/delete$', views.post_delete, name='post_delete'),
    url(r'^posts/(?P<post_primary_key>\d+)/comments/(?P<primary_key>\d+)/edit$', views.comment_update, name='comment_update'),
    url(r'^posts/(?P<post_primary_key>\d+)/comments/(?P<primary_key>\d+)/delete$', views.comment_delete, name='comment_delete')
]
