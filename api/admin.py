from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
  list_display = ("title", "price", "description", "created_at", "updated_at")
  
admin.site.register(Product, ProductAdmin)