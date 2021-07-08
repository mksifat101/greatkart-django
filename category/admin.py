from django.db import models
from category.models import Category
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')


admin.site.register(Category, CategoryAdmin)
