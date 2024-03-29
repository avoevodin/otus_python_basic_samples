# Generated by Django 4.0.6 on 2022-08-19 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0002_remove_userprofile_id_alter_userprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=32)),
                ('birth_date', models.DateField()),
                ('birth_month', models.IntegerField(db_index=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
            ],
        ),
    ]
