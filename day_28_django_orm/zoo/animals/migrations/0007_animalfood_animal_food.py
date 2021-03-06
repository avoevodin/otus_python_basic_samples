# Generated by Django 4.0.6 on 2022-07-05 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0006_animaldetail"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnimalFood",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name="animal",
            name="food",
            field=models.ManyToManyField(to="animals.animalfood"),
        ),
    ]
