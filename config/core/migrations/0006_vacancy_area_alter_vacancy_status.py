# Generated by Django 4.0.2 on 2022-02-18 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_vacancy_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='area',
            field=models.ForeignKey(default=99, on_delete=django.db.models.deletion.PROTECT, to='core.area', verbose_name='Область'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='status',
            field=models.CharField(choices=[('new', 'активно'), ('archive', 'в архиве'), ('unavailable', 'недоступна')], default='new', max_length=150, verbose_name='Статус'),
        ),
    ]
