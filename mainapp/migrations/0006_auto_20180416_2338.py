# Generated by Django 2.0.2 on 2018-04-16 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20180416_2331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='dislikes',
            new_name='count',
        ),
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
    ]
