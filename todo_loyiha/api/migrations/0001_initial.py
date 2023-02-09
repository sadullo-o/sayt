# Generated by Django 3.2.16 on 2023-02-09 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 2, 9, 6, 22, 16, 55841))),
            ],
        ),
    ]