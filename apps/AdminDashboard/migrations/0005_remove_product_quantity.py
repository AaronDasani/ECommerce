# Generated by Django 2.1.2 on 2018-10-29 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminDashboard', '0004_auto_20181029_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]