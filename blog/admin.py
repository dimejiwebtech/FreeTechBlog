from django.contrib import admin
from .models import Category, BlogPost

# auto generate slugs
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('post_name',)}
    list_display = ('post_name', 'post_category', 'author', 'is_featured', 'status',)
    search_fields = ('id', 'post_name', 'post_category__category_name', 'status',)
    list_editable = ('status', 'is_featured',)



admin.site.register(Category)
admin.site.register(BlogPost, BlogAdmin)