# Generated by Django 3.0.4 on 2020-03-12 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c130', '0002_auto_20200311_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='api_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
