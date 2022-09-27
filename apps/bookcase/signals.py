# _*_ coding: utf-8 _*_
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Bookcase
from user.models import AuthUser

__author__ = 'Tim'
__date__ = '26/07/2021 17:40'


@receiver(post_save, sender=Bookcase)
def create_bookfav(sender, instance=None, created=False, **kwargs):
    """
    This function is used to perform increment operation on the book fav count
    """
    if created:
        book = instance.book
        book.fav_num += 1
        book.save()


@receiver(post_delete, sender=Bookcase)
def delete_bookfav(sender, instance=None, created=False, **kwargs):
    """
    This function is used to perform decrement operation on the book fav count
    """
    book = instance.book
    book.fav_num -= 1
    book.save()


@receiver(post_save, sender=AuthUser)
def create_bookcase(sender, instance, created, *args, **kwargs):
    """
    This function is used to create a bookcase for the user,when the user is created
    """
    if created:
        bookcase = Bookcase.objects.create(user=instance)
