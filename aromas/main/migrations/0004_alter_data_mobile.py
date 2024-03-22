# Generated by Django 5.0.2 on 2024-03-22 15:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_session_id_alter_session_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='mobile',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(6000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
