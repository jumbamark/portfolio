# Generated by Django 3.2.8 on 2021-10-19 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='project',
            new_name='projec',
        ),
    ]