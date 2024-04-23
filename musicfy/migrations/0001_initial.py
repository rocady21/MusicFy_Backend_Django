# Generated by Django 5.0.4 on 2024-04-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField(max_length=1000, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_user', models.DateTimeField(auto_now=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
