# Generated by Django 4.1.5 on 2023-01-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_company_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='Description',
            field=models.CharField(default='', max_length=500),
        ),
    ]