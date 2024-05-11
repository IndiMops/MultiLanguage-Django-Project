from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('book/', BookMainViews.as_view(), name = "book_main_page"),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author/', AuthorMainViews.as_view(), name = "author_main_page"),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('publisher/', PublisherMainViews.as_view(), name='publisher_main_page'),
    path('publisher/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
]
