# Generated by Django 4.1.5 on 2023-01-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_applylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]