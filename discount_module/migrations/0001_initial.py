# Generated by Django 5.0.3 on 2024-04-11 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(default=0, verbose_name='درصد تخفیف')),
                ('description', models.TextField(blank=True, null=True, verbose_name='علت تخفیف')),
                ('end_time', models.DateTimeField(verbose_name='تاریخ پایان')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_module.book', verbose_name='کتاب')),
            ],
        ),
    ]
