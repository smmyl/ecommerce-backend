# Generated by Django 4.2 on 2023-04-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='shoe_size',
            field=models.FloatField(choices=[(0, 0), (0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5), (5.5, 5.5), (6, 6), (6.5, 6.5), (7, 7), (7.5, 7.5), (8, 8), (8.5, 8.5), (9, 9), (9.5, 9.5), (10, 10), (10.5, 10.5), (11, 11), (11.5, 11.5), (12, 12), (12.5, 12.5), (13, 13), (13.5, 13.5), (14, 14), (14.5, 14.5), (15, 15), (15.5, 15.5), (16, 16), (16.5, 16.5), (17, 17)]),
        ),
    ]
