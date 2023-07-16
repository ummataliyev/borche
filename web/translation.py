from modeltranslation.translator import register
from modeltranslation.translator import TranslationOptions

from .models import Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
