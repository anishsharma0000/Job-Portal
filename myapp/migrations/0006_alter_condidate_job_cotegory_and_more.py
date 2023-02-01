# Generated by Django 4.1.5 on 2023-01-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_condidate_min_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condidate',
            name='job_cotegory',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='condidate',
            name='job_type',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='condidate',
            name='max_salary',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='condidate',
            name='min_salary',
            field=models.BigIntegerField(default=0),
        ),
    ]
