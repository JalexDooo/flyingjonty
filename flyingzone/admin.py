from django.contrib import admin
from .models import Artical, Tag, Category
# Register your models here.

class ArticalAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'create_time']

admin.site.register(Artical, ArticalAdmin)
admin.site.register(Tag)
admin.site.register(Category)