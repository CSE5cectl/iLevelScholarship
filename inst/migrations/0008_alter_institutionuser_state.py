# Generated by Django 4.2.4 on 2023-09-28 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inst', '0007_alter_institutionuser_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutionuser',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]