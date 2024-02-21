from django.contrib import admin
from .models import News, NewsImage



class NewsImageAdmin(admin.StackedInline):
    model = NewsImage

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    inlines = [NewsImageAdmin]

admin.site.register(News,NewsAdmin)
