# Generated by Django 3.1.5 on 2021-01-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumi', '0012_auto_20210107_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakulteti',
            name='Fakultet',
            field=models.IntegerField(choices=[(1, 'Publik'), (2, 'Privat')], default=1),
        ),
    ]
