from django.urls import path

from book_module import views

urlpatterns = [
    path('publishers/', views.PublishersView.as_view(), name='publishers_page'),
    path('authors/', views.AuthorsView.as_view(), name='authors_page'),
    #author detail url
    path('books/<str:book_name>/<int:book_id>', views.BookView.as_view(), name='book_detail_page'),
]