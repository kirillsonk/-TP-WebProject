# Generated by Django 2.0.2 on 2018-04-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20180416_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='mainapp/images/cookie.png'),
        ),
    ]
