# Generated by Django 4.2.4 on 2023-09-28 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0006_remove_scholarship_id_scholarship_scholarship_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scholarship',
            old_name='state_user',
            new_name='state',
        ),
    ]
