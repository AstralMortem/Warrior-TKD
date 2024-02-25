from django.contrib import admin
from .models import Attendance, AttendanceUser
from django.utils.html import format_html
from django.contrib.auth import get_user_model
# Register your models here.

class AttendanceUserAdmin(admin.StackedInline):
    model = AttendanceUser
    extra = 0

class AttendanceAdmin(admin.ModelAdmin):
    inlines = [AttendanceUserAdmin]
    list_display = ("group","date","gym","coach","get_stat")
    list_filter = [
        "date","gym","group"
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "coach":
            kwargs["queryset"] = get_user_model().objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_stat(self,obj):
        res = [0,0,0,0]
        for i in obj.participant_to_attendance.all():
            if i.attendance_type == "pre":
                res[0] += 1
            if i.attendance_type == "ill":
                res[1] += 1
            if i.attendance_type == "aps":
                res[2] += 1
            if i.attendance_type == "gre":
                res[3] += 1
    
        # return format_html(f"<button type='button' class='collapsible'>Відкрити</button><p class='content d-inline-flex flex-column' style='padding: 0 18px;background-color: white;max-height: 0;overflow: hidden;transition: max-height 0.2s ease-out;'>Присутні:<span style='color:green;'>{res[0]}</span> Відсутні:<span style='color:red;'>{res[2]}</span> Хворі:<span style='color:blue;'>{res[1]}</span> Поваж:<span style='color:orange;'>{res[3]}</span></p>")

        return format_html(f"""
                            <p>
                            <a class="btn btn-primary" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
                                Переглянути
                            </a>
                            </p>
                            <div class="collapse z-3" id="collapseExample">
                            <div class="card card-body">
                                <h4 class="d-flex flex-column">Присутні:<span style='color:green;'>{res[0]}</span> Відсутні:<span style='color:red;'>{res[2]}</span> Хворі:<span style='color:blue;'>{res[1]}</span> Поваж:<span style='color:orange;'>{res[3]}</span></h4>
                            </div>
                            </div>
                """)


    get_stat.short_description = "Статистика"



admin.site.register(Attendance,AttendanceAdmin)
