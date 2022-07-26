from django.contrib import admin
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.


class TaggedItemsList(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem

# create descendant of TaggedItem
class CustomProduct(ProductAdmin):
    inlines = [TaggedItemsList]

admin.site.unregister(Product)
admin.site.register( Product, CustomProduct )
