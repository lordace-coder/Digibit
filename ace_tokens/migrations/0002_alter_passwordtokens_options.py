# Generated by Django 5.0 on 2024-05-04 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ace_tokens', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passwordtokens',
            options={'verbose_name': 'PasswordToken', 'verbose_name_plural': 'PasswordTokens'},
        ),
    ]
