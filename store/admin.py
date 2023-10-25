from django.contrib import admin
from .models import Category, Products, Cart

# Register your models here.
admin.site.register(Cart)
admin.site.register(Products)
admin.site.register(Category)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('name',)
#
#
# @admin.register(Products)
# class ProductsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'amount')
#     list_display_links = ('name',)
