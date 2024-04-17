from django.shortcuts import render
from book_module.models import Author, Book, Category, Publisher


def best_authors_component(request):
    authors = Author.objects.filter(rate__gte=4)

    context = {
        'authors' : authors
    }
    return render(request, 'components/best_authors_component.html', context)


def newest_books_component(request):
    newest_books = Book.objects.all()[:20]
    categories = Category.objects.all()
    cat_id = request.GET.get('cat_id')
    hame_should_active = True

    if cat_id is not None and cat_id != '':
        cat = Category.objects.filter(id=cat_id).first()
        newest_books = Book.objects.filter(category=cat).all()
        hame_should_active = False

    context = {
        'newest_books': newest_books,
        'cats': categories,
        'hame_should_active': hame_should_active,
        'cat_id': cat_id,
    }
    return render(request, 'components/newest_books_component.html', context)


def best_publishers_component(request):
    best_publishers = Publisher.objects.filter(rate__gte=4)
    for publisher in best_publishers:
        publisher_books = Book.objects.filter(publisher=publisher).all()
        publisher.books = publisher_books.count()
    context = {
        'best_publishers': best_publishers
    }
    return render(request, 'components/best_publishers_component.html', context)


def Index_comments_component(request):
    return render(request, 'components/index_comments_component.html')

