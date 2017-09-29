from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^all_items.html$', views.all_items),
    url(r'^show/(?P<item_id>\d+)$', views.item),
    url(r'^addcart$', views.addcart),
<<<<<<< Updated upstream
    url(r'^search$', views.search),
    url(r'^searchcat$', views.searchcat),
    url(r'^sortby$', views.sortby),
    url(r'^admin$', views.admin),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^orders$', views.orders),
    url(r'^products$', views.products),
=======
    url(r'^cart$', views.cart),
>>>>>>> Stashed changes

]
