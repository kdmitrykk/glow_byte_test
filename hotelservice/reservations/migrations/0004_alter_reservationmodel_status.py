# Generated by Django 3.2.16 on 2025-04-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_alter_reservationmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='status',
            field=models.CharField(choices=[('SUCCESS', 'Success'), ('CANСELED', 'Canceled')], default='SUCCESS', max_length=10, verbose_name='Статус'),
        ),
    ]
