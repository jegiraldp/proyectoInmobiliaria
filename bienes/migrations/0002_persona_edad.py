# Generated by Django 2.1.3 on 2018-11-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(default=0),
        ),
    ]
