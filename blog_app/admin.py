from django.contrib import admin
from .models import *

class CategoryModelAdmin(admin.ModelAdmin):
    pass

class BlogModelAdmin(admin.ModelAdmin):
    ordering = ("-updated_at", )


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Blog, BlogModelAdmin)