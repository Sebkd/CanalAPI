# Generated by Django 3.2.13 on 2022-05-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheetapi', '0005_alter_spreadscheet_is_send'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spreadscheet',
            name='is_send',
            field=models.DateTimeField(blank=True, default='0000-00-00 00:00:00.0+00'),
        ),
    ]
