# Generated by Django 5.0.4 on 2024-05-08 00:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Song', '0001_initial'),
        ('musicfy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist_song',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicfy.user'),
        ),
    ]