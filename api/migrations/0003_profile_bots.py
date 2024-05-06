# Generated by Django 5.0 on 2024-05-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_miningbot_alter_profile_wallet_alter_wallet_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bots',
            field=models.ManyToManyField(blank=True, related_name='owned_bot', to='api.miningbot'),
        ),
    ]
