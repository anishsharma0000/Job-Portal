# Generated by Django 4.1.5 on 2023-01-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='condidate',
            name='max_salary',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='condidate',
            name='min_salary',
            field=models.BigIntegerField(default=None),
        ),
    ]