# Generated by Django 3.2.12 on 2022-04-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comingsoon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify_me',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, unique=True),
        ),
    ]