from django.db import models

from book_module.models import Book

# Create your models here.
class IndexComments(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    sold_book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="کتاب خریداری شده")
    email = models.EmailField(verbose_name="ایمیل")
    comment = models.TextField(verbose_name="نظر")

    def __str__(self):
        return self.name