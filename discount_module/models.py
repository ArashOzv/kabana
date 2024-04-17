from django.db import models
from book_module.models import Book

# Create your models here.
class Discount(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="کتاب")
    percentage = models.FloatField(default=0, verbose_name="درصد تخفیف")
    description = models.TextField(blank=True, null=True, verbose_name="علت تخفیف")
    end_time = models.DateTimeField(verbose_name="تاریخ پایان")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")

