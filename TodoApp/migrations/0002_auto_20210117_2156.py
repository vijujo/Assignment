# Generated by Django 3.1.5 on 2021-01-17 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
