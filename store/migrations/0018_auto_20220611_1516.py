# Generated by Django 3.0.5 on 2022-06-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20220611_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='user',
            field=models.CharField(max_length=120),
        ),
    ]
