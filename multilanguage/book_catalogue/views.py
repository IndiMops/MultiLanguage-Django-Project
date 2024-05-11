from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Author, Publisher
from Menu.models import MenuItem


class BookMainViews(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book_catalogue/book_main.html', {"books": books, "nodes": MenuItem.objects.all()})


class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'book_catalogue/book_detail.html', {'book': book, "nodes": MenuItem.objects.all()})
    


class AuthorMainViews(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'book_catalogue/author_main.html', {"authors": authors, "nodes": MenuItem.objects.all()})

class AuthorDetailView(View):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return render(request, 'book_catalogue/author_detail.html', {'author': author, "nodes": MenuItem.objects.all()})


class PublisherMainViews(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        return render(request, 'book_catalogue/publisher_main.html', {"publishers": publishers, "nodes": MenuItem.objects.all()})

class PublisherDetailView(View):
    def get(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        return render(request, 'book_catalogue/publisher_detail.html', {'publisher': publisher, "nodes": MenuItem.objects.all()})
