# Generated by Django 3.2.4 on 2022-12-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0006_pair'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
