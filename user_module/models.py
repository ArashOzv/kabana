from django.db import models
from django.contrib.auth.models import AbstractUser

from book_module.models import Book
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=11, verbose_name="شماره تلفن", unique=True)
    password = models.CharField(max_length=100, verbose_name="رمز عبور", editable=False)
    repeat_password = models.CharField(max_length=100, verbose_name="تکرار رمز عبور", editable=False)
    cart = models.ManyToManyField(Book, related_name="cart", verbose_name="سبد خرید", blank=True, null=True)

    #validators:
    is_active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'
    
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"

