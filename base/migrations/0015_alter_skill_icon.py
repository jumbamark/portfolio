# Generated by Django 3.2.8 on 2021-10-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_skill_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.ImageField(default='Skill.png', null=True, upload_to=''),
        ),
    ]