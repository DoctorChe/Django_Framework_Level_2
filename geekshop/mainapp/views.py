from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
import json
import random
import os.path
from mainapp.models import ProductCategory, Product

from django.conf import settings
from django.core.cache import cache

links_menu = [
    {'href': 'main:index', 'short_href': 'index', 'name': 'home'},
    {'href': 'main:products', 'short_href': 'products', 'name': 'products'},
    # {'href': 'main:history', 'short_href': 'history', 'name': 'history'},
    # {'href': 'main:showroom', 'short_href': 'showroom', 'name': 'showroom'},
    {'href': 'main:contacts', 'short_href': 'contacts', 'name': 'contact'},
]

# JSON_CONTACTS = "mainapp/json/contact_items.json"
JSON_PATH = "mainapp/json/"


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', errors='ignore') as infile:
        return json.load(infile)


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
    # trending_products = Product.objects.filter(is_active=True)[:6]
    trending_products = get_products()[:6]
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
            # products = Product.objects.filter(is_active=True).order_by('price')
            products = get_products_orederd_by_price()
        else:
            # products = Product.objects.filter(category__pk=pk, is_active=True).order_by('price')
            products = get_products_in_category_orederd_by_price(pk)
    else:
        # products = Product.objects.filter(is_active=True).order_by('price')
        products = get_products_orederd_by_price()

    products_paginator = Paginator(products, 2)
    try:
        products = products_paginator.get_page(page)
    except PageNotAnInteger:
        products = products_paginator.get_page(1)
    except EmptyPage:
        products = products_paginator.get_page(products_paginator.num_pages)

    # links_menu = get_links_menu()

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
    # product = get_object_or_404(Product, pk=pk)
    product = get_product(pk)
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
    # with open(JSON_CONTACTS, 'r', encoding='utf-8') as tmp_file:
    #     contact_items = json.load(tmp_file)

    # contact_items = load_from_json('contact_items')

    if settings.LOW_CACHE:
        key = f'contact_items'
        contact_items = cache.get(key)
        if contact_items is None:
            # contact_items = load_from_json('contacts__contact_items')
            contact_items = load_from_json('contact_items')
            cache.set(key, contact_items)
    else:
        # contact_items = load_from_json('contacts__contact_items')
        contact_items = load_from_json('contact_items')

    context = {
        'page_title': 'contact us',
        'contact_items': contact_items,
        'today': today(),
        'links_menu': links_menu,
        # 'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', context)


# def get_links_menu():
#     if settings.LOW_CACHE:
#         key = 'links_menu'
#         links_menu = cache.get(key)
#         if links_menu is None:
#             links_menu = ProductCategory.objects.filter(is_active=True)
#             cache.set(key, links_menu)
#         return links_menu
#     else:
#         return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
