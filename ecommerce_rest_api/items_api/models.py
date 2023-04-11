from django.db import models

# Create your models here.
class Item(models.Model):
    ITEM_CATEGORY = [
        ('Clothing'),
        ('Shoes'),
        ('Acessories')
    ]
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Neutral')
    ]
    CLOTHING_SIZE = [
        ('XS'),
        ('S'),
        ('M'),
        ('L'),
        ('XL'),
        ('XXL')
    ]
    SHOE_SIZE = [
        (0), (0.5), (1), (1.5), (2), (2.5), (3), (3.5), (4), (4.5), (5), (5.5), (6), (6.5), (7), (7.5), (8), (8.5), (9), (9.5), (10), (10.5), (11), (11.5), (12), (12.5), (13), (13.5), (14), (14.5), (15), (15.5), (16), (1.5), (17)
    ]
    category = models.Charfield(max_length=1, choices=ITEM_CATEGORY)
    image = models.Charfield(max_length=100)
    gender = models.Charfield(max_length=2, choices=GENDER)
    name = models.Charfield(max_length=20)
    price = models.IntegerField()
    tags = ArrayField(models.Charfield(max_length=20))
    description = models.Charfield(max_length=200)
    clothing_size = models.Charfield(max_length=1, choices=CLOTHING_SIZE)
    shoe_size = models.Charfield(max_length=1, choices=SHOE_SIZE)
