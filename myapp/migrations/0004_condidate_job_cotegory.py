# Generated by Django 4.1.5 on 2023-01-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_condidate_country_condidate_exprience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='condidate',
            name='job_cotegory',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
