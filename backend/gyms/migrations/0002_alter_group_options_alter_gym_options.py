# Generated by Django 5.0.2 on 2024-02-21 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Групу', 'verbose_name_plural': 'Групи'},
        ),
        migrations.AlterModelOptions(
            name='gym',
            options={'verbose_name': 'Спортзал', 'verbose_name_plural': 'Спортзали'},
        ),
    ]
