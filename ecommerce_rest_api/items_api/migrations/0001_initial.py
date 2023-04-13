# Generated by Django 4.2 on 2023-04-11 19:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_category', models.CharField(choices=[('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('Acessories', 'Acessories')], max_length=10)),
                ('image', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Neutral')], max_length=2)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('description', models.CharField(max_length=200)),
                ('clothing_size', models.CharField(choices=[('XS', 'X-Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large'), ('XXL', 'XX-Large')], max_length=3)),
                ('shoe_size', models.IntegerField(choices=[(0, 0), (0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5), (5.5, 5.5), (6, 6), (6.5, 6.5), (7, 7), (7.5, 7.5), (8, 8), (8.5, 8.5), (9, 9), (9.5, 9.5), (10, 10), (10.5, 10.5), (11, 11), (11.5, 11.5), (12, 12), (12.5, 12.5), (13, 13), (13.5, 13.5), (14, 14), (14.5, 14.5), (15, 15), (15.5, 15.5), (16, 16), (16.5, 16.5), (17, 3.4)])),
            ],
        ),
    ]