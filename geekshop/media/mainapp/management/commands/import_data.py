from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User
# from authapp.models import ShopUser
import json
import os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as fin:
        return json.load(fin)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory(**category).save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            Product(**product).save()

        # Создаём суперпользователя при помощи менеджера модели
        if not User.objects.filter(username='django'):
            print('Создаём нового суперпользователя')
            User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')

        # # Создаём суперпользователя при помощи менеджера модели
        # user = ShopUser.objects.filter(username='django')
        # if not user:
        #     print('Создаём нового суперпользователя')
        #     ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')

