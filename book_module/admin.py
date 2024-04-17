from django.contrib import admin
from book_module.models import Book, Publisher, Category, Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'author', 'language', 'publisher', 'stock', 'weight', 'price']
    list_editable = ['category', 'author', 'language', 'publisher', 'price', 'stock']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name','image']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','image']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','image', 'birth_date', 'death_date']

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)