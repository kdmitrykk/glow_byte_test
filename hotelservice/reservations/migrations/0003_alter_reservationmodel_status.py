# Generated by Django 3.2.16 on 2025-04-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20250406_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='status',
            field=models.CharField(choices=[('SUCCESS', 'Success'), ('CANSELED', 'Canceled')], default='SUCCESS', max_length=10, verbose_name='Статус'),
        ),
    ]
