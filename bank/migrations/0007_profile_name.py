# Generated by Django 5.0.2 on 2024-02-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_rename_customer_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
