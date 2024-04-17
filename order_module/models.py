from django.db import models

from book_module.models import Book
from user_module.models import CustomUser

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="کاربر")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="کتاب")
    quantity = models.IntegerField(verbose_name="تعداد")
    totla_price = models.IntegerField(verbose_name="هزینه")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده/نشده")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return f"{self.user} - {self.book}"
    
    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش ها"