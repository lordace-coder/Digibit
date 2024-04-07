# Generated by Django 5.0.3 on 2024-04-07 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email_address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('state_of_origin', models.CharField(max_length=100)),
                ('state_of_residence', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('recovery_phone_number', models.CharField(max_length=50)),
                ('verified_phone_number', models.BooleanField(default=False)),
                ('verified_email_address', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
