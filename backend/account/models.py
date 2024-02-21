from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django_jsonform.models.fields import ArrayField
from django.utils import timezone
import uuid

# Create your models here.


class Belt(models.Model):
    code = models.CharField("Куп",max_length=20,primary_key=True)
    photo = models.ImageField("Фото",upload_to='belts')
    title = models.CharField("Назва поясу",max_length=250)

    def __str__(self):
        return f"{self.title} ({self.code})"
    
    class Meta:
        verbose_name = "Пояс"
        verbose_name_plural = "Пояси"


    
class BeltDescription(models.Model):
    id = models.OneToOneField(Belt, verbose_name="Норматив поясу", on_delete=models.CASCADE, primary_key=True, related_name='description')
    ofp = models.TextField("ОФП",blank=True)
    
    #TODO: expand model

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "Норматив"
        verbose_name_plural = "Нормативи"

    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Ви повинні ввести пошту")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            generated = self.make_random_password()
            user.set_password(generated)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    

class BaseUser(AbstractBaseUser,PermissionsMixin):
    JUDGE_TYPE = [
        ('judge_1','Суддя 2-ї категорії'),
        ('judge_2','Суддя 1-ї категорії'),
        ('judge_3','Суддя національної категорії'),
        ('judge_4','Суддя міжнародної категорії B'),
        ('judge_5','Суддя міжнародної категорії A')
    ]

    COACH_TYPE = [
        ('coach_1','Помічник тренера'),
        ('coach_2','Тренер початкової підготовки'),
        ('coach_3','Тренер національного класу'),
        ('coach_4','Інструктор міжнародного класу'),
        ('coach_5','Майстер-інструктор міжнародного класу')
    ]

    GENDER = [
        ('m', 'Чоловік'),
        ('f', 'Жінка')
    ]



    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    photo = models.ImageField("Аватар",upload_to='users/avatars', blank=True, null=True)
    full_name = models.CharField("ПІБ", max_length=250)
    email = models.EmailField("Пошта", unique=True)
    mobile = models.CharField("Телефон", blank=True)
    gender = models.CharField("Стать", max_length=1, choices=GENDER, default='m')
    judge_type = models.CharField("Категорія судді", max_length=7, choices=JUDGE_TYPE, null=True, blank=True)
    coach_type = models.CharField("Категорія тренера", max_length=7, choices=COACH_TYPE, null=True, blank=True)
    belt = models.ForeignKey(Belt,verbose_name="Пояс",on_delete=models.SET_NULL, null=True)
    birthday = models.DateField("День народження",null=True,blank=True)
    itf_code = models.PositiveBigIntegerField("Код в базі itf-ua",null=True,blank=True)
    itf_link = models.URLField("Силка на itf-ua",null=True,blank=True)
    links = ArrayField(models.URLField("Силка на соціальну мережу",blank=True,null=True), size=8,blank=True,null=True)
    coach = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,blank=True, verbose_name="Тренер")



    is_active = models.BooleanField("Акаунт активний?", default=True)
    is_staff = models.BooleanField("Акаунт Тренера?",default=False)

    date_joined = models.DateTimeField("Дата приєднання",default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        if(self.full_name):
            return self.full_name
        return self.email

    class Meta:
        verbose_name = "Учасник"
        verbose_name_plural = "Учасники"
