# Generated by Django 2.2.1 on 2019-06-22 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model_car',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cars.ModelCar'),
        ),
    ]
