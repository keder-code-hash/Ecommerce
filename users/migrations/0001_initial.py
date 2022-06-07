# Generated by Django 3.1.14 on 2022-06-07 10:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddressModel',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='default', max_length=255)),
                ('description', models.CharField(blank=True, default=' default description', max_length=255)),
                ('address_line_1', models.CharField(blank=True, max_length=300)),
                ('address_line_2', models.CharField(blank=True, max_length=300)),
                ('street_name', models.CharField(blank=True, max_length=100)),
                ('city_name', models.CharField(blank=True, max_length=50)),
                ('state_name', models.CharField(blank=True, max_length=50)),
                ('country_name', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, verbose_name='email address')),
                ('ph_NO_code', models.CharField(max_length=50)),
                ('ph_NO', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('profile_pic_url', models.CharField(default='https://res.cloudinary.com/dvcjj1k7a/image/upload/v1636390885/Blog/Profile/663328_ti7cnp.png', max_length=300, null=True)),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('date_of_birth', models.DateField(null=True)),
                ('interests', models.TextField(max_length=200, null=True)),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=100, verbose_name='email address')),
                ('ph_NO_code', models.CharField(max_length=50)),
                ('ph_NO', models.CharField(max_length=50)),
                ('address', models.ManyToManyField(blank=True, related_name='address', to='users.UserAddressModel', verbose_name='user address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
