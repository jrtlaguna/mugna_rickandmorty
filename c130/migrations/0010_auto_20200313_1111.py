# Generated by Django 3.0.4 on 2020-03-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c130', '0009_character_localimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='localImage',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to=''),
        ),
    ]
