from django.urls import path, re_path
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    re_path('^$', mainapp.index, name='index'),
    re_path('^products/$', mainapp.products, name='products'),
    re_path('^catalog/category/(?P<pk>\d+)/$', mainapp.products, name='catalog'),
    # re_path('^catalog/category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='catalog'),
    re_path('^catalog/category/(None|[\d+])/page/(?P<page>\d+)/$', mainapp.products, name='catalog'),
    re_path('^catalog/product/(?P<pk>\d+)/$', mainapp.product, name='product'),
    re_path('^contacts/$', mainapp.contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
