from modeltranslation.translator import register, TranslationOptions
from .models import Author, Publisher, Book

@register(Author)
class AuthorTransOptions(TranslationOptions):
    fields = ("name", "country")
    
    
@register(Publisher)
class PublisherTransOptions(TranslationOptions):
    fields = ("name", )
    
    
@register(Book)
class BookTransOptions(TranslationOptions):
    fields = ("title", )