from django.contrib import admin

from .models import *

class ProductPhotosInline(admin.TabularInline):
    model = ProductPhotos
    extra = 1


from django.contrib import admin
from .models import Product
from modeltranslation.admin import TranslationAdmin

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductPhotosInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(UserProfile)
admin.site.register(Category)

admin.site.register(Rating)
admin.site.register(Review)