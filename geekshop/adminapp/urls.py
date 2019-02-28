from django.urls import path, re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path('^user/create/$', adminapp.AdminShopUserCreateView.as_view(), name='user_create'),
    re_path('^users/read/$', adminapp.UsersListView.as_view(), name='index'),
    re_path('^user/update/(?P<pk>\d+)/$', adminapp.AdminShopUserUpdateView.as_view(), name='user_update'),
    re_path('^user/delete/(?P<pk>\d+)/$', adminapp.AdminShopUserDeleteView.as_view(), name='user_delete'),
    re_path('^user/activate/(?P<pk>\d+)/$', adminapp.AdminShopUserActivateView.as_view(), name='user_activate'),

    re_path('^categories/$', adminapp.ProductCategoryListView.as_view(), name='categories'),
    re_path('^category/create/$', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    re_path('^category/update/(?P<pk>\d+)/$', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    re_path('^category/delete/(?P<pk>\d+)/$', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),
    re_path('^category/activate/(?P<pk>\d+)/$', adminapp.ProductCategoryActivateView.as_view(), name='category_activate'),

    re_path('^products/category/(?P<pk>\d+)/$', adminapp.ProductListView.as_view(), name='products'),
    re_path('^products/category/(?P<pk>\d+)/page/(?P<page>\d+)/$', adminapp.ProductListView.as_view(), name='products'),
    re_path('^product/read/(?P<pk>\d+)/$', adminapp.ProductDetailView.as_view(), name='product_read'),
    re_path('^product/create/(?P<pk>\d+)/$', adminapp.ProductCreateView.as_view(), name='product_create'),
    re_path('^product/update/(?P<pk>\d+)/$', adminapp.ProductUpdateView.as_view(), name='product_update'),
    re_path('^product/delete/(?P<pk>\d+)/$', adminapp.ProductDeleteView.as_view(), name='product_delete'),
    re_path('^product/activate/(?P<pk>\d+)/$', adminapp.ProductActivateView.as_view(), name='product_activate'),

    # re_path('^user/create/$', adminapp.user_create, name='user_create'),
    # re_path('^users/read/$', adminapp.index, name='index'),
    # re_path('^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    # re_path('^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),
    # re_path('^user/activate/(?P<pk>\d+)/$', adminapp.user_activate, name='user_activate'),

    # re_path('^categories/$', adminapp.categories, name='categories'),
    # re_path('^category/create/$', adminapp.category_create, name='category_create'),
    # re_path('^category/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),
    # re_path('^category/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete'),
    # re_path('^category/activate/(?P<pk>\d+)/$', adminapp.category_activate, name='category_activate'),

    # re_path('^products/category/(?P<pk>\d+)/$', adminapp.products, name='products'),
    # re_path('^products/category/pk<int:pk>/$', adminapp.ProductListView.as_view(), name='products'),
    # re_path('^product/read/(?P<pk>\d+)/$', adminapp.product_read, name='product_read'),
    # re_path('^product/create/(?P<pk>\d+)/$', adminapp.product_create, name='product_create'),
    # re_path('^product/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    # re_path('^product/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),
    # re_path('^product/activate/(?P<pk>\d+)/$', adminapp.product_activate, name='product_activate'),
]
