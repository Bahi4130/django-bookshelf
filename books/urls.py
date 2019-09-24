from django.urls import path
from books.views import BooksListView, AddBookView

urlpatterns = [
    path('', BooksListView.as_view(), name='index'),
    path('add-book/', AddBookView.as_view(), name='add_book'),
]