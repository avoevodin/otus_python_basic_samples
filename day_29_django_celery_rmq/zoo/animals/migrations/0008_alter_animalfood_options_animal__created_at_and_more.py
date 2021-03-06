# Generated by Django 4.0.6 on 2022-07-06 08:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0007_animalfood_animal_food"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="animalfood",
            options={"verbose_name_plural": "Animal food"},
        ),
        migrations.AddField(
            model_name="animal",
            name="created_at",
            field=models.DateTimeField(
                auto_created=True,
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="food",
            field=models.ManyToManyField(
                related_name="animals", to="animals.animalfood"
            ),
        ),
        migrations.AlterField(
            model_name="animaldetail",
            name="animal",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="details",
                serialize=False,
                to="animals.animal",
            ),
        ),
    ]
