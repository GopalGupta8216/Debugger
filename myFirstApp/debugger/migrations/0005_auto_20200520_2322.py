# Generated by Django 3.0.5 on 2020-05-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debugger', '0004_auto_20200520_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='enrollment',
            field=models.CharField(default=12345678, max_length=8, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
