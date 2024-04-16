# Generated by Django 5.0.4 on 2024-04-16 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('duration_tot', models.IntegerField()),
                ('num_songs', models.IntegerField()),
                ('photo', models.TextField(max_length=500)),
                ('desc', models.TextField(max_length=500)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist_gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.gender')),
                ('id_playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.playlist')),
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
                ('gender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.gender')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist_songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.playlist')),
                ('id_song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.song')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('paswword', models.TextField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('create_user', models.DateTimeField(auto_now=True)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.rol')),
            ],
        ),
        migrations.CreateModel(
            name='PlayList_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.playlist')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.user')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('id_type_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.type_message')),
                ('id_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_send_msgt', to='musicfy.user')),
                ('id_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_recibe_msg', to='musicfy.user')),
            ],
        ),
        migrations.CreateModel(
            name='Like_playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.playlist')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.user')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.status')),
                ('id_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_send_requeest', to='musicfy.user')),
                ('id_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_recive_requeest', to='musicfy.user')),
            ],
        ),
        migrations.CreateModel(
            name='Artist_song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.song')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicfy.user')),
            ],
        ),
    ]