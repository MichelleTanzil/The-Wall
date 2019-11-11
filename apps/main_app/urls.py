from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^wall$', views.wall),
    url(r'^new_message/(?P<user_id>\d+)$', views.new_message),
    url(r'^new_comment$', views.new_comment),
    url(r'^delete_message$', views.delete_message),
]
