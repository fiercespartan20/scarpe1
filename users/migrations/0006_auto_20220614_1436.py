# Generated by Django 3.0.5 on 2022-06-14 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220607_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_supplier',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_yard',
        ),
    ]