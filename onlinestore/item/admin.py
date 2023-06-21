from django.contrib import admin
from .models import Category, Item #importo la categoria para que el admin la vea.

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)

