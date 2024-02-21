from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import BaseUserCreationForm
from django.utils.html import format_html

from .models import BeltDescription, Belt, BaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.forms import SimpleArrayField
from django import forms
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
# Register your models here.



class BeltDescriptionAdmin(admin.StackedInline):
    model = BeltDescription

class BeltAdmin(admin.ModelAdmin):
    inlines = [BeltDescriptionAdmin]


class CustomAddForm(BaseUserCreationForm):
    class Meta:
        model = BaseUser
        fields = ('email','full_name')

class CustomUserAdmin(UserAdmin,DynamicArrayMixin):
    add_form = CustomAddForm
    
    fieldsets = (
        (None, {'fields': ('email','mobile', 'password')}),
        (_('Personal info'), {'fields': ('photo','full_name','gender','belt', 'coach_type', 'judge_type', 
                                         'itf_code', 'itf_link', 'links', 'coach')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('birthday','last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name','email', 'password1', 'password2'),
        }),
    )
    list_display = ('image_tag','email', 'full_name', 'belt', 'is_staff','is_active')
    list_display_links = ('image_tag','email', 'full_name')
    search_fields = ('email', 'full_name')
    ordering = ('email','is_active')


    prepopulated_fields = {'email':('full_name',)}


    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:50px; border-radius:9999px;"/>'.format(obj.photo.url if obj.photo else "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"))



admin.site.register(BaseUser,CustomUserAdmin)
admin.site.register(Belt,BeltAdmin)
