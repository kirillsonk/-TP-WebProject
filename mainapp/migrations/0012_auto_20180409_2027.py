# Generated by Django 2.0.2 on 2018-04-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20180409_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='text',
            field=models.CharField(default='', max_length=100),
        ),
    ]