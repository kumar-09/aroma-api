# Generated by Django 5.0.2 on 2024-02-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
