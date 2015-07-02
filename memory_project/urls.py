from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_card$', views.add_card, name='add_card'),
    url(r'^all', views.all, name='all'),
    url(r'^(?P<card_id>[0-9]+)/card_renew$', views.card_renew, name='card_renew'),
    url(r'^(?P<card_id>[0-9]+)/card_change$', views.card_change, name='card_change'),
    url(r'^(?P<card_id>[0-9]+)/card_delete$', views.card_delete, name='card_delete'),
]