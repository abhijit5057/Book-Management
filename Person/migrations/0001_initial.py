# Generated by Django 3.2.5 on 2022-07-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('birth_date', models.DateField()),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
