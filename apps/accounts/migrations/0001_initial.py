# Generated by Django 4.0.1 on 2022-01-14 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(help_text='Email Address', max_length=50, unique=True)),
                ('username', models.CharField(help_text='Username', max_length=50, unique=True)),
                ('name', models.CharField(help_text='Name of User', max_length=50)),
                ('is_staff', models.BooleanField(default=False, help_text='This user can access admin panel')),
                ('is_admin', models.BooleanField(default=False, help_text='This user has all permissions without explicitly assigning them')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], help_text='Gender of the user', max_length=50, null=True)),
                ('password', models.CharField(max_length=150)),
                ('location', models.CharField(blank=True, help_text='Location of the user', max_length=200)),
                ('summary', models.CharField(blank=True, help_text='Summary of the user', max_length=500)),
                ('date_of_birth', models.DateField(blank=True, help_text='Date of Birth of the user', null=True)),
                ('website', models.CharField(blank=True, help_text='Website of the user', max_length=100)),
                ('education', models.CharField(blank=True, help_text='Education of the user', max_length=150)),
                ('work', models.CharField(blank=True, help_text='Work of the user', max_length=100)),
                ('profile_pic', models.CharField(blank=True, help_text='Profile pic url of the user', max_length=300)),
                ('skills', models.CharField(default='[]', help_text='Skill set of the user', max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
