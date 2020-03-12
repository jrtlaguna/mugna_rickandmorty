# Generated by Django 3.0.4 on 2020-03-11 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c130', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='character',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='location',
            name='date_created',
        ),
        migrations.AddField(
            model_name='character',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('air_date', models.DateField()),
                ('code', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('characters', models.ManyToManyField(related_name='Characters', to='c130.Character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='episodes',
            field=models.ManyToManyField(to='c130.Episode', verbose_name='Episodes'),
        ),
    ]
