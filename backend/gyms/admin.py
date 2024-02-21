
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Gym, Group
from django.contrib.auth import get_user_model



class GroupAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title','gym', 'coach')}),
        (_('Participants'), {'fields': ('participants',)}),
    )
    filter_horizontal = ('participants',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'participants':
            kwargs['queryset'] = get_user_model().objects.filter(is_staff=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Gym)
admin.site.register(Group,GroupAdmin)