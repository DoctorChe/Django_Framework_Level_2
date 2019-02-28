from django.shortcuts import render
import datetime
import json
import csv
from mainapp.models import ProductCategory, Product

links_menu = [
    {'href': 'main:index', 'short_href': 'index', 'name': 'home'},
    {'href': 'main:products', 'short_href': 'products', 'name': 'products'},
    # {'href': 'main:history', 'short_href': 'history', 'name': 'history'},
    # {'href': 'main:showroom', 'short_href': 'showroom', 'name': 'showroom'},
    {'href': 'main:contacts', 'short_href': 'contacts', 'name': 'contact'},
]

categories = ProductCategory.objects.all()

CSV_PRODUCTCATEGORIES = "./csv/productcategories.csv"
CSV_PRODUCTS = "./csv/products.csv"


def today():
    return datetime.date.today()


def index(request):
    context = {
        'page_title': 'home',
        'today': today(),
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):

    # import_categories(CSV_PRODUCTCATEGORIES)
    # import_products(CSV_PRODUCTS)

    products = Product.objects.all()
    category_name = 'all'
    if pk:
        for category in categories:
            if category.pk == int(pk):
                category_name = category.name
    context = {
        'page_title': 'our products range',
        'today': today(),
        'links_menu': links_menu,
        'products': products,
        'categories': categories,
        'category_name': category_name,
    }
    return render(request, 'mainapp/products.html', context)


def product(request):
    product = Product.objects.all()
    category_name = 'all'
    context = {
        'today': today(),
        'links_menu': links_menu,
        'product': product,
        'categories': categories,
        'category_name': category_name,
    }
    return render(request, 'mainapp/product-details.html', context)


def contacts(request):
    with open('json/contact_items.json', 'r', encoding='utf-8') as tmp_file:
        contact_items = json.load(tmp_file)

    context = {
        'page_title': 'contact us',
        'contact_items': contact_items,
        'today': today(),
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/contact.html', context)


def import_categories(csv_filename):
    data_reader = csv.reader(open(csv_filename), delimiter=',', quotechar='"')
    categories = [category.name for category in ProductCategory.objects.all()]
    for row in data_reader:
        if row[0] not in categories:
            category = ProductCategory()
            category.name = row[0]
            category.description = row[1]
            category.save()


def import_products(csv_filename):
    data_reader = csv.reader(open(csv_filename), delimiter=',', quotechar='"')
    products = [product.name for product in Product.objects.all()]
    for row in data_reader:
        if row[0] not in products:
            product = Product()
            product.category = ProductCategory.objects.get(id=int(row[0]))
            product.name = row[1]
            product.image = row[2]
            product.short_desc = row[3]
            product.description = row[4]
            product.price = float(row[5])
            product.quantity = int(row[6])
            product.save()
