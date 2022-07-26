from django.contrib import admin, messages
from .models import Collection, Product, Customer, Order, OrderItem
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.


class InventoryFilter(admin.SimpleListFilter):
    title = 'price'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Small'),
            ('>10', 'Large')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(price__lt=1000)
        elif self.value() == '>10':
            return queryset.filter(price__gt=1000)


class InventoryState(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Low'),
            ('>50', 'High')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(inventory__lt=40)
        else:
            return queryset.filter(inventory__gt=40)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    search_fields = ['title']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'inventory', 'inventory_state',
                    'price', 'description', 'collection_state']
    list_editable = ['price', 'inventory']
    list_filter = ['collection', InventoryState]
    list_select_related = ['collection']

    def inventory_state(self, product):
        if product.inventory < 40:
            return 'Low'
        else:
            return 'High'

    def collection_state(self, product):
        if product.price > 1000:
            return 'It\'s larger'
        else:
            return "it's smaller"

# To apply ordering in this column we write
    @admin.display(ordering='price')
    def oldPrice(self, product):
        if product.price < 100:
            return 'normal'
        else:
            return 'old'

    @admin.action(description='clear inventory')
    def clear_inventory(self, request, queryset):
        querycount = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{querycount} product updated sufcessfullty',
            messages.SUCCESS
        )


@admin.register(Collection)
class collectionAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'product_count']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        url = (reverse("admin:store_product_changelist")
               + "?"
               + urlencode({
                   'collection': str(collection.id)
               })
               )
        return format_html("<a href='{}'>{}</a>", url, collection.product_count)


# overide the method from ModelAdmin class


    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('product')
        )


# sure thing that this thing gives use a lot of good
# stuff. For more list go to
# django model admin

@admin.register(Customer)
class adminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone']
    list_editable = ['phone']
    search_fields = ['first_name__istartswith']


class OrderItemList(admin.StackedInline):
    autocomplete_fields = ['product']
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemList]
    list_display = ['placed_at', 'customer', 'customer_phone']
    list_select_related = ['customer']

    def customer_phone(self, order):
        return order.customer.phone


# format_html
# reverse
# urlencode
