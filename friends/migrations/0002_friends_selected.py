# Generated by Django 3.2.4 on 2022-12-24 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
