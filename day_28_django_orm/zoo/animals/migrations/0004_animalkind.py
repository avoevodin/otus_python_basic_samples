# Generated by Django 4.0.6 on 2022-07-05 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_remove_animal_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
