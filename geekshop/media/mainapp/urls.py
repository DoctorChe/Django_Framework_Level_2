# from django.contrib import admin
from django.urls import path, re_path
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),
    re_path(r'^products/$', mainapp.products, name='products'),
    re_path(r'^products/(\d+)/$', mainapp.products, name='category'),
    re_path(r'^product/$', mainapp.product, name='product'),
    re_path(r'^contacts/$', mainapp.contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
