# Generated by Django 2.2.10 on 2020-02-23 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200223_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='author',
            new_name='user_in_group',
        ),
    ]
