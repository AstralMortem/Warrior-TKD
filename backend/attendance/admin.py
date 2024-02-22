from django.contrib import admin
from .models import Attendance, AttendanceUser
# Register your models here.

class AttendanceUserAdmin(admin.StackedInline):
    model = AttendanceUser
    extra = 1

class AttendanceAdmin(admin.ModelAdmin):
    inlines = [AttendanceUserAdmin]

admin.site.register(Attendance,AttendanceAdmin)
