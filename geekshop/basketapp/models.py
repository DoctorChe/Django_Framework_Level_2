from django.db import models
from authapp.models import ShopUser
from mainapp.models import Product


# class BasketQuerySet(models.QuerySet):
#
#     def delete(self, *args, **kwargs):
#         for object in self:
#             object.product.quantity += object.quantity
#             object.product.save()
#         super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(ShopUser,
                             verbose_name='пользователь',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                verbose_name='продукт',
                                on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество',
                                                default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления',
                                        auto_now_add=True)

    @property
    def product_cost(self):
        """return cost of all products this type"""
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        """return total quantity for user"""
        # _items = Basket.objects.filter(user=self.user)
        _items = self.user.basket_set.all()
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    @property
    def total_cost(self):
        """return total cost for user"""
        # _items = Basket.objects.filter(user=self.user)
        _items = self.user.basket_set.all()
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    # def delete(self):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super(self.__class__, self).delete()
    #
    # # переопределяем метод, сохранения объекта
    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super(self.__class__, self).save(*args, **kwargs)
