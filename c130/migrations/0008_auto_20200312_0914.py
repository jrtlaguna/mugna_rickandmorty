# Generated by Django 3.0.4 on 2020-03-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c130', '0007_auto_20200312_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='air_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
