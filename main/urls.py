from django.urls import path
from .views import BooksListView, BookCreateView


urlpatterns = [
    path('', BooksListView.as_view(), name='book-list'),
    path('add-book', BookCreateView.as_view(), name='book-add'),
]