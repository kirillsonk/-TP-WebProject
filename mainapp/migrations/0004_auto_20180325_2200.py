# Generated by Django 2.0.2 on 2018-03-25 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_questions_dislikes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='content',
            new_name='text',
        ),
    ]