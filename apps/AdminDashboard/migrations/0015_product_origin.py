# Generated by Django 2.1.2 on 2018-12-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminDashboard', '0014_auto_20181101_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='origin',
            field=models.CharField(default='inventory', max_length=20),
            preserve_default=False,
        ),
    ]
