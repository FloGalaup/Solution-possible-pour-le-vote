# Generated by Django 4.0.1 on 2022-02-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_superuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='private_key',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]
