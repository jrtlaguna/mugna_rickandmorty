# Generated by Django 3.0.4 on 2020-03-12 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c130', '0003_auto_20200312_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
