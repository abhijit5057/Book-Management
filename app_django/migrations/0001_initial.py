# Generated by Django 3.2.5 on 2022-07-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('day_started', models.DateField()),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
