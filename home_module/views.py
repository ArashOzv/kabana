from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from book_module.models import Author, Book, Category

# Create your views here.
def header_render_partial(request):
    #add user database query
    cats = Category.objects.all()

    context = {
        'cats' : cats
    }
    return render(request, 'header_component.html', context)

def footer_render_partial(request):
    #add user database query
    cats = Category.objects.all()

    context = {
        'cats' : cats
    }
    return render(request, 'footer_component.html', context)


class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        most_sold_books = Book.objects.filter(sales__gt=0).order_by('-sales')[:15]


        context = {
            'categories': categories,
            'most_sold_books': most_sold_books,
        }
        return render(request, 'home.html', context)
    
