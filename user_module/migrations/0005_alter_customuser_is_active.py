# Generated by Django 5.0.3 on 2024-04-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0004_alter_customuser_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال/غیرفعال'),
        ),
    ]