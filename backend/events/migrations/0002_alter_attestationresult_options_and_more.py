# Generated by Django 5.0.2 on 2024-02-21 21:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_baseuser_links'),
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attestationresult',
            options={'verbose_name': 'Результат спортсмена', 'verbose_name_plural': 'Результати спортсменів'},
        ),
        migrations.AlterModelOptions(
            name='competitionresult',
            options={'verbose_name': 'Результат спортсмена', 'verbose_name_plural': 'Результати спортсменів'},
        ),
        migrations.AlterField(
            model_name='attestation',
            name='participants',
            field=models.ManyToManyField(related_name='attestation_participant', through='events.AttestationResult', to=settings.AUTH_USER_MODEL, verbose_name='Спортсмени'),
        ),
        migrations.AlterField(
            model_name='attestationresult',
            name='comment',
            field=models.CharField(blank=True, max_length=300, verbose_name='Коментар'),
        ),
        migrations.AlterField(
            model_name='attestationresult',
            name='from_belt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attestation_from_belt', to='account.belt', verbose_name='З поясу'),
        ),
        migrations.AlterField(
            model_name='attestationresult',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_to_attestation', to=settings.AUTH_USER_MODEL, verbose_name='Спортмен'),
        ),
        migrations.AlterField(
            model_name='attestationresult',
            name='to_belt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attestation_to_belt', to='account.belt', verbose_name='На пояс'),
        ),
        migrations.AlterField(
            model_name='competitionjudgment',
            name='comment',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Коментар'),
        ),
        migrations.AlterField(
            model_name='competitionjudgment',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='judge_to_competition', to=settings.AUTH_USER_MODEL, verbose_name='Суддя'),
        ),
        migrations.AlterField(
            model_name='competitionresult',
            name='comment',
            field=models.CharField(blank=True, max_length=300, verbose_name='Коментар'),
        ),
        migrations.AlterField(
            model_name='competitionresult',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_to_competition', to=settings.AUTH_USER_MODEL, verbose_name='Спортсмен'),
        ),
    ]
