# Generated by Django 2.1.2 on 2018-11-01 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminDashboard', '0008_auto_20181029_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='upload',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='image/'),
        ),
    ]
