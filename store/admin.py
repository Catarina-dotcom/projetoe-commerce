from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created_at', 'stock', 'discount')
    list_filter = ('available', 'category', 'tags')
    search_fields = ('name', 'description', 'category', 'tags')
    prepopulated_fields = {'slug': ('name',)}
   
    
    