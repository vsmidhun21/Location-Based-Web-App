# Generated by Django 5.1.7 on 2025-03-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0003_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
