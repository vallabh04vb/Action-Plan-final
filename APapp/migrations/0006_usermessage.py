# Generated by Django 4.2.1 on 2023-08-31 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APapp', '0005_remove_useraccount_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=12)),
                ('message', models.CharField(default='', max_length=50)),
            ],
        ),
    ]