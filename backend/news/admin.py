from django.contrib import admin
from .models import News, NewsImage
from django.contrib.auth import get_user_model



class NewsImageAdmin(admin.StackedInline):
    model = NewsImage

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    inlines = [NewsImageAdmin]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = get_user_model().objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(News,NewsAdmin)
