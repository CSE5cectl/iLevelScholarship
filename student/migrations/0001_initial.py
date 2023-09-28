# Generated by Django 4.2.4 on 2023-09-28 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inst', '0009_alter_institutionuser_state'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('state', '0007_rename_state_user_scholarship_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_text', models.TextField()),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inst.institutionuser')),
                ('scholarship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='state.scholarship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('home_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='state.state')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScholarshipApplicationNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_received', to=settings.AUTH_USER_MODEL)),
                ('scholarship_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.scholarshipapplication')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_sent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
