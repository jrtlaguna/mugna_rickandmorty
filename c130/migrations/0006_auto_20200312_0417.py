# Generated by Django 3.0.4 on 2020-03-12 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c130', '0005_character_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='api_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
