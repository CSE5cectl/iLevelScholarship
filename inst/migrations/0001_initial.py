# Generated by Django 4.2.4 on 2023-09-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('institution_name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]