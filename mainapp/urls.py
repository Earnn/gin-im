from django.conf.urls import url,include
from . import views
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
import os
from django.conf.urls.static import static


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^report/?$',views.report, name='report'),
    # url(r'^profile/?$',views.profile, name='profile'),
    url(r'^delivery/?$',views.delivery, name='delivery'),
    url(r'^ud-delivery/?$',views.ud_delivery, name='ud_delivery'),
    url(r'^update-status/$', views.update_status, name='update_status'),
    url(r'^change-status/$', views.change_status, name='change_status'),
    url(r'^โรงอาหารโต้รุ่ง/$', views.home_tohrung, name='tohrung'),
    
    url(r'^success/(?P<order_id>\d+)/?$',views.success, name='success'),
    url(r'^addStore/?$', views.addStore, name='add_store'),
    url(r'^(?P<pk>\d+)/addMenu/?$', views.addMenu, name='add_menu'),
    url(r'^store/(?P<store_name>.*)/(?P<store_id>\d+)$', views.shop, name='shop'),
    url(r'^โรงอาหารโต้รุ่ง/(?P<store_name>.*)?$', views.until_dawn_canteen, name='until_dawn_canteen'),

    # url(r'^add_to_cart/(?P<menu_iud>\d+)/(?P<quantity>\d+)$', views.add_to_cart, name='add_to_cart'),
    url(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart'),
    url(r'^remove_from_cart/$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^check-out/$', views.ud_checkout, name='ud_checkout'),
    
    # url(r'^store/(?P<store_name>.*)/(?P<store_id>\d+)/delivery$',views.night_canteen, name="night_canteen"),
    url(r'^search/(?P<cate>.*)?$',views.searchBycate, name='search_cate'),
    url(r'^usecoupon/(?P<coupon>\d+)?$',views.use_coupon, name='use_coupon'),
    url(r'^search/?$',views.searchAll, name='search_input'),
    url(r'^about-ginim/?$',views.about_us, name='about_us'),
    url(r'^contact/?$',views.contact, name='contact'),
    url(r'^order/?$',views.order, name='order'),
    url(r'^like/$', views.like_button, name='like_button'),
    url(r'^checkIsSell/$', views.checkIsSell, name='checkIsSell'),
    url(r'^changeDelivery/$', views.changeDelivery, name='changeDelivery'),
    url(r'^select-payment/(?P<pk>\d+)/$', views.payment, name='select_payment'),

    url(r'^ud-select-payment/(?P<order_id>\d+)/$', views.ud_payment, name='ud-select-payment'),
   
    url(r'^edit-store/$', views.outofstock, name='outofstock'),
    url(r'^edit-delivery/$', views.edit_delivery, name='edit_delivery'),
    url(r'^inf$', views.fill_in, name='inf'),
    url(r'^inf-complete$', views.fill_in_complete, name='inf-complete'),
    url(r'^inf-edit$', views.fill_in_edit, name='is_inf'),
    url(r'^code/$', views.use_code, name='code'),
    url(r'^show-slip-(?P<pk>\d+)/$', views.showSlip, name='show-slip'),
    # showSlip


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG404: :
#     urlpatterns += staticfiles_urlpatterns()