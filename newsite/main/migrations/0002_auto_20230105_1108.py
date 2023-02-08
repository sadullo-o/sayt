# Generated by Django 3.2.16 on 2023-01-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('img', models.TextField()),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'Biz haqimizda',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'yangilik', 'verbose_name_plural': 'Yangiliklar'},
        ),
    ]