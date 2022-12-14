# Generated by Django 3.2.5 on 2022-07-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_email',
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default=0, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='password',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
