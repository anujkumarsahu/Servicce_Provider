# Generated by Django 4.1.2 on 2023-02-01 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0011_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('H', 'homecleaning'), ('E', 'Electric'), ('P', 'Plumbing'), ('CS', 'Car Care & Service'), ('C', 'Carpenters'), ('S', 'Salon At Home'), ('HP', 'Home Painting')], max_length=3),
        ),
    ]
