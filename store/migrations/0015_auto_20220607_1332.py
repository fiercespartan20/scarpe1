# Generated by Django 3.0.5 on 2022-06-07 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_materialmixp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MaterialMix',
            new_name='MixMaterial',
        ),
        migrations.CreateModel(
            name='MatMix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cha', models.IntegerField()),
                ('oil', models.IntegerField()),
                ('vp', models.IntegerField()),
                ('oh', models.IntegerField()),
                ('dep', models.IntegerField()),
                ('trans', models.IntegerField()),
                ('flux', models.IntegerField()),
                ('cusi', models.IntegerField()),
                ('extrasi', models.IntegerField()),
                ('gst', models.IntegerField()),
                ('extracost', models.IntegerField()),
                ('total', models.IntegerField()),
                ('yard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Yard')),
            ],
        ),
    ]
