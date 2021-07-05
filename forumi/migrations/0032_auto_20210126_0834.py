# Generated by Django 3.0.5 on 2021-01-26 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forumi', '0031_auto_20210125_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakulteti',
            name='Fakultet',
            field=models.IntegerField(choices=[(2, 'Privat'), (1, 'Publik')], default=1),
        ),
        migrations.AlterField(
            model_name='pergjigjje',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pyetje',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]