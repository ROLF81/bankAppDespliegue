# Generated by Django 5.0.3 on 2024-03-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
