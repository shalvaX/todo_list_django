# Generated by Django 3.1 on 2020-09-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeManagement', '0006_auto_20200906_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=''),
        ),
    ]