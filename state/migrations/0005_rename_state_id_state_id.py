# Generated by Django 4.2.4 on 2023-09-28 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0004_remove_state_id_state_state_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='state_id',
            new_name='id',
        ),
    ]
