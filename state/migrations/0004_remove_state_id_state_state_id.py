# Generated by Django 4.2.4 on 2023-09-28 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0003_remove_scholarship_state_scholarship_state_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='id',
        ),
        migrations.AddField(
            model_name='state',
            name='state_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
