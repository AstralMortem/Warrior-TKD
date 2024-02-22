from django.contrib import admin
from .models import Competition, Attestation, CompetitionResult, AttestationResult, CompetitionJudgment
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _
# Register your models here.

class CompetitionResultAdmin(admin.StackedInline):
    model = CompetitionResult
    extra = 1


class CompetitionJudgmentResult(admin.StackedInline):
    model = CompetitionJudgment
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "participant":
            kwargs["queryset"] = get_user_model().objects.filter(judge_type__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CompetitionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Головна", {'fields': ('title','place', 'date_start','date_end','competition_type','is_completed', 'is_archived')}),
        ("Місце клубу", {'fields': ('command_sparing','command_tul')}),
    )
    inlines = [CompetitionResultAdmin,CompetitionJudgmentResult]

    list_display = ('title', 'place','get_date','is_completed', 'is_archived')
    search_fields = ('title', 'place')
    ordering = ('is_completed','is_archived','date_start')
    list_filter = [
        "date_start",
        "is_completed",
        "is_archived"
    ]

    def get_date(self,obj):
        if obj.date_end:
            return f"З {obj.date_start} по {obj.date_end}"
        return obj.date_start
    
    get_date.short_description = "Дата"


@admin.action(description="Архівувати обрані атестації")
def make_archived(modeladmin, request, queryset):
    queryset.update(is_archived=True)

@admin.action(description="Завершити обрані атестації")
def make_completed(modeladmin, request, queryset):
    queryset.update(is_completed=True)

class AttestationResultAdmin(admin.StackedInline):
    model = AttestationResult
    extra = 1

class AttestationAdmin(admin.ModelAdmin):
    list_display = ('title', 'place','date_start','is_completed', 'is_archived')
    inlines = [AttestationResultAdmin]

    ordering = ('is_completed','is_archived','date_start')
    actions = [make_completed,make_archived]


admin.site.register(Competition,CompetitionAdmin)
admin.site.register(Attestation,AttestationAdmin)


