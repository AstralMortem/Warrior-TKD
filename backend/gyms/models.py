from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.

class Gym(models.Model):
    title = models.CharField("Заголовок",max_length=250)
    coach = models.ForeignKey("account.BaseUser",on_delete=models.SET_NULL, null=True,verbose_name="Тренер")
    phone = models.CharField("Телефон",max_length=13)
    email = models.EmailField("Пошта")
    calendar = models.CharField("Дні занять",max_length=250)
    time = models.CharField("Час заняття",max_length=250)
    address = models.CharField("Адреса",max_length=250)
    location = PlainLocationField(zoom=4,verbose_name="Координати")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Спортзал"
        verbose_name_plural="Спортзали"

class Group(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.SET_NULL, null=True,verbose_name="Спортзал")
    title = models.CharField("Заголовок",max_length=250)
    coach = models.ForeignKey("account.BaseUser",on_delete=models.CASCADE,verbose_name="Тренер")

    calendar = models.CharField("Дні занять групи",max_length=250)
    time = models.CharField("Час заняття групи",max_length=250)

    participants = models.ManyToManyField('account.BaseUser', related_name='group_participants',verbose_name="Спортсмени")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + f"({self.gym.title})"
    
    class Meta:
        verbose_name = "Групу"
        verbose_name_plural = "Групи"

