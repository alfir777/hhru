# Generated by Django 3.2.11 on 2022-04-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20220401_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='watch',
            field=models.BooleanField(default=False, verbose_name='Отклик'),
        ),
    ]
