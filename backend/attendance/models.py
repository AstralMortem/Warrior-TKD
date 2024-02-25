from django.db import models
from django.contrib.postgres.fields import DateRangeField

# Create your models here.
class Attendance(models.Model):
    coach = models.ForeignKey('account.BaseUser', on_delete=models.SET_NULL, null=True, verbose_name="Тренер")
    gym = models.ForeignKey('gyms.Gym', on_delete=models.CASCADE,verbose_name="Спортзал")
    group = models.ForeignKey('gyms.Group',on_delete=models.CASCADE,verbose_name="Група")
    date = models.DateField("Дата")

    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField('account.BaseUser', through="AttendanceUser", related_name='attendance_participants',verbose_name="Спортсмен")

    def __str__(self):
        return f'Відвідування за {str(self.created_at)}'
    
    class Meta:
        verbose_name = "Відвідування"
        verbose_name_plural = "Відвідування"
    
ATTENDANCE_TYPE = (
    ('pre','Присутній'),
    ('ill','Захворів'),
    ('aps', 'Відсутній'),
    ('gre', 'Поважна причина')
)

class AttendanceUser(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE,verbose_name="Спортсмен",related_name="attendance_to_participant")
    attendance = models.ForeignKey('Attendance', on_delete=models.CASCADE,verbose_name="Відвідування", related_name="participant_to_attendance")
    attendance_type = models.CharField("Причина",max_length=3, choices=ATTENDANCE_TYPE, default="pre")
    comment = models.CharField("Коментар",max_length=100, blank=True)

    def __str__(self):
        return str(self.participant)
    
    class Meta:
        verbose_name = "Запис відвідування"
        verbose_name_plural = "Записи відвідувань"
