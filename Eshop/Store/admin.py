from django.contrib import admin
from .models import Product
from .category import Category

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']  # Assuming 'name' is a field in Category

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
