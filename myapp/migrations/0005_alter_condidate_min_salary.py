# Generated by Django 4.1.5 on 2023-01-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_condidate_job_cotegory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condidate',
            name='min_salary',
            field=models.BigIntegerField(default=''),
        ),
    ]
