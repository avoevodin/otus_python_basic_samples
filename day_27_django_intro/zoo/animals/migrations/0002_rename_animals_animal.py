# Generated by Django 4.0.6 on 2022-07-05 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Animals',
            new_name='Animal',
        ),
    ]
