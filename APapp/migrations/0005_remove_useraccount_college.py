# Generated by Django 4.2.1 on 2023-08-31 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APapp', '0004_rename_tname_useraccount_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='college',
        ),
    ]
