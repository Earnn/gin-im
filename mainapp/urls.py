from django.conf.urls import url,include
from . import views
from django.utils.encoding import python_2_unicode_compatible

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^graph/?$',views.graph, name='graph'),
    url(r'^questionnaire/?$',views.questionnaire, name='questionnaire'),
    # url(r'^profile/?$',views.profile, name='profile'),
    url(r'^delivery/?$',views.delivery, name='delivery'),
    url(r'^success/(?P<order_id>\d+)/?$',views.success, name='success'),
    url(r'^addStore/?$', views.addStore, name='add_store'),
    url(r'^(?P<pk>\d+)/addMenu/?$', views.addMenu, name='add_menu'),
    url(r'^store/(?P<pk>\d+)/?$', views.shop, name='shop'),
    url(r'^search/(?P<cate>.*)?$',views.searchBycate, name='search_cate'),
    url(r'^search/?$',views.searchAll, name='search_input'),
    url(r'^about-ginim/?$',views.about_us, name='about_us'),
    url(r'^contact/?$',views.contact, name='contact'),
    url(r'^order/?$',views.order, name='order'),
    url(r'^like/$', views.like_button, name='like_button'),
    url(r'^checkIsSell/$', views.checkIsSell, name='checkIsSell'),
    url(r'^edit/store/$', views.outofstock, name='outofstock'),
    url(r'^inf$', views.fill_in, name='inf'),
    url(r'^inf-complete$', views.fill_in_complete, name='inf-complete'),
    url(r'^inf-edit$', views.fill_in_edit, name='is_inf'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

