# Generated by Django 5.0.2 on 2024-02-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='rating',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AddField(
            model_name='beltdescription',
            name='kicks',
            field=models.TextField(blank=True, verbose_name='Удари'),
        ),
        migrations.AddField(
            model_name='beltdescription',
            name='power_breaking',
            field=models.TextField(blank=True, verbose_name='Силове розбивання'),
        ),
        migrations.AddField(
            model_name='beltdescription',
            name='self_defence',
            field=models.TextField(blank=True, verbose_name='Самозахист'),
        ),
        migrations.AddField(
            model_name='beltdescription',
            name='sparings',
            field=models.TextField(blank=True, verbose_name='Cпаринг'),
        ),
        migrations.AddField(
            model_name='beltdescription',
            name='spec_tech',
            field=models.TextField(blank=True, verbose_name='Спец.Техніка'),
        ),
        migrations.AddField(
            model_name='beltdescription',
            name='theory',
            field=models.TextField(blank=True, verbose_name='Теорія'),
        ),
        migrations.AddField(
            model_name='beltdescription',
            name='tul',
            field=models.TextField(blank=True, verbose_name='Туль'),
        ),
    ]