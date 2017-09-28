from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^main$', views.main),
    url(r'^show/(?P<item_id>\d+)$', views.item),
    url(r'^addcart$', views.addcart),
]
