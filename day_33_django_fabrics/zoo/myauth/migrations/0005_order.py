# Generated by Django 4.0.6 on 2022-08-19 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0004_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('awaiting_shipment', 'Awaiting shipment'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending', max_length=30)),
                ('shipped_on', models.DateTimeField(blank=True, null=True)),
                ('delivered_on', models.DateTimeField(blank=True, null=True)),
                ('shipped_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='myauth.employee')),
            ],
        ),
    ]
