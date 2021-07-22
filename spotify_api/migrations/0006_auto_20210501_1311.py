# Generated by Django 3.2 on 2021-05-01 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_api', '0005_auto_20210501_0253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curatedplaylist',
            name='songs',
        ),
        migrations.AddField(
            model_name='curatedplaylist',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spotify_api.artist'),
        ),
    ]
