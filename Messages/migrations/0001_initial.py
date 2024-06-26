# Generated by Django 5.0.4 on 2024-05-08 00:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicfy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('id_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_send_msgt', to='musicfy.user')),
                ('id_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_recibe_msg', to='musicfy.user')),
                ('id_type_message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Messages.type_message')),
            ],
        ),
    ]
