# Generated by Django 4.2.1 on 2023-09-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APapp', '0006_usermessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='track',
            field=models.CharField(default='', max_length=200),
        ),
    ]