from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Item(models.Model):
    ITEM_CATEGORY = [
        ('C','Clothing'),
        ('S','Shoes'),
        ('A','Acessories')
    ]
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Neutral')
    ]
    CLOTHING_SIZE = [
        ('XS', 'X-Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X-Large'),
        ('XXL', 'XX-Large')
    ]
    SHOE_SIZE = [
        (0, 0), (0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5), (5.5, 5.5), (6, 6), (6.5, 6.5), (7, 7), (7.5, 7.5), (8, 8), (8.5, 8.5), (9, 9), (9.5, 9.5), (10, 10), (10.5, 10.5), (11, 11), (11.5, 11.5), (12, 12), (12.5, 12.5), (13, 13), (13.5, 13.5), (14, 14), (14.5, 14.5), (15, 15), (15.5, 15.5), (16, 16), (16.5, 16.5), (17, 17/5)
    ]
    item_category = models.CharField(max_length=10, choices=ITEM_CATEGORY)
    image = models.CharField(max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    tags = ArrayField(models.CharField(max_length=20))
    description = models.CharField(max_length=200)
    clothing_size = models.CharField(max_length=3, choices=CLOTHING_SIZE, blank=True)
    shoe_size = models.IntegerField(choices=SHOE_SIZE)
