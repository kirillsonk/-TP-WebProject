# Generated by Django 2.0.2 on 2018-04-09 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20180409_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='question',
            new_name='tag_question',
        ),
    ]
