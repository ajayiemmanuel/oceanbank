# Generated by Django 5.0.2 on 2024-02-18 22:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_deposit_currency_alter_deposit_crypto_balance_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('card_type', models.CharField(default='0', max_length=200, null=True)),
                ('card_number', models.CharField(default='**** **** **** 2563', max_length=200, null=True)),
                ('exp_date', models.CharField(default='12/24', max_length=200, null=True)),
                ('cvv', models.CharField(default='***', max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
