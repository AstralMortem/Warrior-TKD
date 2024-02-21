from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field



class News(models.Model):
    title = models.CharField("Заголовок",max_length=250)
    text = CKEditor5Field("Текст")
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)
    author = models.ForeignKey("account.BaseUser",on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    is_archived = models.BooleanField("Архівувати",default=False)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новини"
        verbose_name_plural = "Новини"


class NewsImage(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE, related_name='news_images', verbose_name="Новина")
    image = models.ImageField(upload_to='news/%Y/%m/%d',verbose_name="Фото")

    def __str__(self):
        return self.news.title
    class Meta:
        verbose_name = "Фото новини"
        verbose_name_plural = "Фото новин"
