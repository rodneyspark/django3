# Generated by Django 2.2.8 on 2020-10-19 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
    ]