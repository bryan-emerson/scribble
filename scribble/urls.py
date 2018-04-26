from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts$', views.post_list, name='post_list'),
]
