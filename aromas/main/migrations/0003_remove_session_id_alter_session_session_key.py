# Generated by Django 5.0.2 on 2024-03-21 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_users_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='id',
        ),
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
