# Generated by Django 4.0.2 on 2022-02-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_area_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.CharField(max_length=255, verbose_name='Зарплата'),
        ),
    ]
