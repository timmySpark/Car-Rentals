# Generated by Django 4.0.4 on 2022-08-09 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
    ]
