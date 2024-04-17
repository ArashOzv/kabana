from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from book_module.models import Author, Book, Publisher

# Create your views here.
class PublishersView(View):
    def get(self, request):
        
        all_publishers = Publisher.objects.all()
        top_publishers = all_publishers.filter(rate__gte=4)
        context = {
            'all_publishers' : all_publishers,
            'top_publishers' : top_publishers
        }
        return render(request, 'publishers.html', context)



class AuthorsView(View):
    def get(self, request):

        all_authors = Author.objects.all()
        top_authors = all_authors.filter(rate__gte=4)
        context = {
            'all_authors' : all_authors,
            'top_authors' : top_authors
        }
        return render(request, 'authors.html', context)




class AuthorDetailView(View):
    def get(self, request, author_id):
        author = Author.objects.filter(id=author_id).first()
        author_books = Book.objects.filter(author=author).all()
        context = {
            'author' : author,
            'author_books' : author_books
        }
        return render(request, 'author_detail.html', context)
    



class BookView(View):
    def get(self, request, book_name, book_id):
        book = Book.objects.filter(id=book_id).first()
        related_books = Book.objects.filter(category=book.category).all().exclude(id=book_id)  
        context = {
            'book' : book,
            'related_books' : related_books,
        }
        return render(request, 'book_detail.html', context)
    



