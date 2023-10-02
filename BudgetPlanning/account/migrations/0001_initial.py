# Generated by Django 4.2.5 on 2023-10-01 04:58

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('permission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='auth.permission')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Username')),
                ('telegram_id', models.CharField(default=0, primary_key=True, serialize=False, verbose_name='Telegram id')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='UZ', verbose_name='Telefon raqami')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Foydalanuvchilar',
                'db_table': 'useraccount',
            },
            bases=('auth.permission', models.Model),
        ),
    ]
