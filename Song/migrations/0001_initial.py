# Generated by Django 5.0.4 on 2024-05-07 23:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
                ('photo', models.TextField(max_length=500)),
                ('url_song', models.TextField(max_length=500)),
                ('duration', models.FloatField(default=0)),
                ('gender_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Song.gender')),
            ],
        ),
        migrations.CreateModel(
            name='Artist_song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_song', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Song.song')),
            ],
        ),
    ]
