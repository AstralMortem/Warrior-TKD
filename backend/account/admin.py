from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import BaseUserCreationForm
from django.utils.html import format_html
from .models import BeltDescription, Belt, BaseUser
from django.utils.translation import gettext_lazy as _





class BeltDescriptionAdmin(admin.StackedInline):
    model = BeltDescription

class BeltAdmin(admin.ModelAdmin):
    inlines = [BeltDescriptionAdmin]


class CustomAddForm(BaseUserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('email','full_name')

class CustomUserAdmin(UserAdmin):
    add_form = CustomAddForm
    
    fieldsets = (
        ("Головна", {'fields': ('email','mobile','full_name', 'password')}),
        ("Персональна інформація", {'fields': ('photo','gender','belt','birthday', 'rating','coach','coach_type', 'judge_type', 
                                         'itf_code', 'itf_link', 'links')}),
        ("Дозволи", {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name','email', 'password1', 'password2'),
        }),
    )
    list_display = ('image_tag', 'full_name', 'belt', 'is_staff','is_active','rating')
    list_display_links = ('image_tag', 'full_name')
    search_fields = ('email', 'full_name')
    ordering = ('email','is_active')
    readonly_fields = ["rating"]
    list_filter = [
        "coach",
        "belt",
        "is_active",
        "is_staff",
        "gender"
    ]


    prepopulated_fields = {'email':('full_name',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "coach":
            kwargs["queryset"] = BaseUser.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:50px; border-radius:9999px;"/>'.format(obj.photo.url if obj.photo else "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"))

    image_tag.short_description = "Фото"


admin.site.register(BaseUser,CustomUserAdmin)
admin.site.register(Belt,BeltAdmin)
