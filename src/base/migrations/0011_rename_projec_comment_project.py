# Generated by Django 3.2.8 on 2021-10-19 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_rename_project_comment_projec'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='projec',
            new_name='project',
        ),
    ]
