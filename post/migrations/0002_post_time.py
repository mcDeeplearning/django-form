# Generated by Django 2.1.3 on 2018-11-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateField(auto_now=True),
        ),
    ]
