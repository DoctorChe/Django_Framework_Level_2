from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
import json
import random
from mainapp.models import ProductCategory, Product

links_menu = [
    {'href': 'main:index', 'short_href': 'index', 'name': 'home'},
    {'href': 'main:products', 'short_href': 'products', 'name': 'products'},
    # {'href': 'main:history', 'short_href': 'history', 'name': 'history'},
    # {'href': 'main:showroom', 'short_href': 'showroom', 'name': 'showroom'},
    {'href': 'main:contacts', 'short_href': 'contacts', 'name': 'contact'},
]

JSON_CONTACTS = "mainapp/json/contact_items.json"


def get_basket(user):
    if user.is_authenticated:
        return user.basket_set.all().order_by('product__category')
    else:
        return []


def get_hot_product():
    products = Product.objects.filter(is_active=True)
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category, is_active=True). \
        exclude(pk=hot_product.pk)[:3]
    return same_products


def today():
    return datetime.date.today()


def index(request):

    trending_products = Product.objects.filter(is_active=True)[:6]
    # trending_products = Product.objects.filter(is_active=True, category__is_active=True)[:6]

    context = {
        'page_title': 'home',
        'today': today(),
        'links_menu': links_menu,
        # 'basket': get_basket(request.user),
        'trending_products': trending_products,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None, page=1):
    categories = ProductCategory.objects.filter(is_active=True)
    hot_product = get_hot_product()

    if pk:
        if pk == '0':
            products = Product.objects.filter(is_active=True).order_by('price')
        else:
            products = Product.objects.filter(category__pk=pk, is_active=True).order_by('price')
    else:
        products = Product.objects.filter(is_active=True).order_by('price')

    products_paginator = Paginator(products, 2)
    try:
        products = products_paginator.get_page(page)
    except PageNotAnInteger:
        products = products_paginator.get_page(1)
    except EmptyPage:
        products = products_paginator.get_page(products_paginator.num_pages)

    context = {
        'page_title': 'our products range',
        'today': today(),
        'links_menu': links_menu,
        'products': products,
        'categories': categories,
        # 'basket': get_basket(request.user),
        'hot_product': hot_product,
        'category_pk': pk,
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk=None):
    categories = ProductCategory.objects.filter(is_active=True)
    product = get_object_or_404(Product, pk=pk)
    same_products = get_same_products(product)

    context = {
        'page_title': 'product',
        'today': today(),
        'links_menu': links_menu,
        'product': product,
        'categories': categories,
        # 'basket': get_basket(request.user),
        'same_products': same_products,
    }
    return render(request, 'mainapp/product-details.html', context)


def contacts(request):
    with open(JSON_CONTACTS, 'r', encoding='utf-8') as tmp_file:
        contact_items = json.load(tmp_file)

    context = {
        'page_title': 'contact us',
        'contact_items': contact_items,
        'today': today(),
        'links_menu': links_menu,
        # 'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', context)
