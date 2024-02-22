# Generated by Django 4.2.10 on 2024-02-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_competition_is_rating_calculated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attestation',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='Архівовано'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Завершено'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='Архівовано'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Завершено'),
        ),
    ]
