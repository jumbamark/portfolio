# Generated by Django 3.2.8 on 2021-10-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]