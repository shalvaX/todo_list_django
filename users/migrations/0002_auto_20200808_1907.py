# Generated by Django 3.0.8 on 2020-08-08 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='conf_password',
            new_name='confirm_password',
        ),
    ]
