from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^all_items.html$', views.all_items),
    url(r'^show/(?P<item_id>\d+)$', views.item),
    url(r'^addcart$', views.addcart),
    url(r'^search$', views.search),
    url(r'^searchcat$', views.searchcat),
    url(r'^sortby$', views.sortby),
]
