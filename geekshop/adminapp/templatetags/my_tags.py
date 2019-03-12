from django import template

register = template.Library()

from django.conf import settings

MEDIA_URL = settings.MEDIA_URL
LANGUAGE_CODE = settings.LANGUAGE_CODE
# MEDIA_URL = '/media/'

EXCHANGE_RATE = 65.0


def media_folder_products(string):
    if not string:
        string = "product_images/default.jpg"
    return f"{MEDIA_URL}{string}"


@register.filter(name="media_folder_users")
def media_folder_users(string):
    if not string:
        string = "users_avatars/default.png"
    return f"{MEDIA_URL}{string}"


@register.filter(name="local_currency")
def local_currency(string):
    if LANGUAGE_CODE == "ru-ru":
        return f"{string}₽" if string and float(string) != 0 else f"0.00₽"
    return f"${(float(string) / EXCHANGE_RATE):.2f}" if string and float(string) != 0 else f"$0.00"


register.filter("media_folder_products", media_folder_products)
# register.filter('media_folder_users', media_folder_users)
