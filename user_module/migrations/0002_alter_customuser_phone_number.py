# Generated by Django 5.0.3 on 2024-04-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن'),
        ),
    ]
