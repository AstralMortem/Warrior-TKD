
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Gym, Group
from django.contrib.auth import get_user_model


class GymAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "coach":
            kwargs["queryset"] = get_user_model().objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class GroupAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title','gym', 'coach')}),
        (_('Participants'), {'fields': ('participants',)}),
    )
    filter_horizontal = ('participants',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "coach":
            kwargs["queryset"] = get_user_model().objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'participants':
            kwargs['queryset'] = get_user_model().objects.filter(is_staff=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Gym, GymAdmin)
admin.site.register(Group,GroupAdmin)