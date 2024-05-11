from django.contrib import admin
from django import forms
from .models import *
from django_select2.forms import Select2Widget
from modeltranslation.admin import TranslationAdmin

import datetime


@admin.register(Author)
class AuthorAdmin(TranslationAdmin):
    list_display = ("name", "get_books")
    search_fields = ("name", )
    
    def get_books(self, obj):
        return ", ".join([book.title for book in obj.books.all()])

    get_books.short_description = 'Книги'


@admin.register(Publisher)
class PublisherAdmin(TranslationAdmin):
    list_display = ("name", "get_books")
    search_fields = ("name", )
    
    def get_books(self, obj):
        return ", ".join([book.title for book in obj.book_set.all()])

    get_books.short_description = 'Книги'



current_year = datetime.date.today().year
years_choices = [(year, year) for year in range(current_year, 1799, -1)]


class BookPublicationYearForm(forms.ModelForm):
    publication_year = forms.ChoiceField(choices = years_choices, label = "Рік публікації", widget=Select2Widget)
    
    class Meta:
        model = Book
        fields = "__all__"


@admin.register(Book)
class BookAdmin(TranslationAdmin):
    form = BookPublicationYearForm
    list_display = ("title", "publication_year", "publisher", "author")
    list_filter = ("publication_year", "publisher", "author")
    search_fields = ("title", "publisher", "author")