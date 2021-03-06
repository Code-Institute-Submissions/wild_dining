from django.contrib import admin
from .models import Product, Category, Basket

# Register your models here.

"""Classes here used to customise admin panel in application"""
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('name',) #reveres by adding '-' in front of name


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'placeholder_img',
    )


class BasketAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'placeholder_img'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Basket, BasketAdmin)
