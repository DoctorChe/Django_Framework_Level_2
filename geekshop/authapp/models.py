from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.timezone import now
from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    # age = models.PositiveSmallIntegerField(verbose_name='age')
    age = models.PositiveSmallIntegerField(verbose_name='age', default=18)
    activation_key = models.CharField(verbose_name='activation key', max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(verbose_name='activation key expires',
                                                  default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='tags', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='about me', max_length=512, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    language = models.CharField(max_length=64, blank=True)
    vk_page = models.CharField(verbose_name='VK page', max_length=128, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
