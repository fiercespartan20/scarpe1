# Generated by Django 3.1 on 2022-06-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220602_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_buyer',
            field=models.BooleanField(default=False),
        ),
    ]