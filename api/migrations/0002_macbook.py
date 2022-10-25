# Generated by Django 4.1.2 on 2022-10-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Macbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.IntegerField()),
                ('title', models.CharField(max_length=400)),
                ('region', models.CharField(max_length=200)),
                ('written_date', models.CharField(max_length=200)),
                ('manner_temperature', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('chat_count', models.CharField(max_length=30)),
            ],
        ),
    ]
