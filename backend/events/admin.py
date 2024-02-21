from django.contrib import admin
from .models import Competition, Attestation, CompetitionResult, AttestationResult, CompetitionJudgment

from django.utils.translation import gettext_lazy as _
# Register your models here.

class CompetitionResultAdmin(admin.StackedInline):
    model = CompetitionResult
    extra = 1

class CompetitionJudgmentResult(admin.StackedInline):
    model = CompetitionJudgment
    extra = 1

class CompetitionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Головна", {'fields': ('title','place', 'date_start','date_end','competition_type','is_completed', 'is_archived')}),
        ("Місце клубу", {'fields': ('command_sparing','command_tul')}),
    )
    inlines = [CompetitionResultAdmin,CompetitionJudgmentResult]

    list_display = ('title', 'place','get_date','is_completed', 'is_archived')
    search_fields = ('title', 'place','date_start')
    ordering = ('is_completed','is_archived','date_start')

    def get_date(self,obj):
        if obj.date_end:
            return obj.date_start + " - " + obj.date_end
        return obj.date_start
    
    get_date.short_description = "Дата"


class AttestationResultAdmin(admin.StackedInline):
    model = AttestationResult
    extra = 1

class AttestationAdmin(admin.ModelAdmin):
    inlines = [AttestationResultAdmin]


admin.site.register(Competition,CompetitionAdmin)
admin.site.register(Attestation,AttestationAdmin)