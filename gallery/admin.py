from django.contrib import admin
from gallery.models import Category, Gallery


@admin.register(Category, Gallery)
class CategoryAdmin(admin.ModelAdmin):
    pass