# Generated by Django 4.0.2 on 2022-02-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_profile_external_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='in_search',
            field=models.BooleanField(default=False, verbose_name='Искать?'),
        ),
    ]