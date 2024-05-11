from modeltranslation.translator import register, TranslationOptions
from .models import MenuItem

@register(MenuItem)
class MenuTransOptions(TranslationOptions):
    fields = ("name",)