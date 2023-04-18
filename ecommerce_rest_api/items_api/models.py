from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Items(models.Model):
    ITEM_CATEGORY = [
        ('Clothing','Clothing'),
        ('Shoes','Shoes'),
        ('Accessories','Accessories')
    ]
    GENDER = [
        ('M', 'M'),
        ('F', 'F'),
        ('N', 'Neutral')
    ]
    CLOTHING_SIZE = [
        ('None', 'None'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL')
    ]
    SHOE_SIZE = [
        ('None', 'None'), ('0', '0'), ('0.5', '0.5'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5'), ('5.5', '5.5'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9'), ('9.5', '9.5'), ('10', '10'), ('10.5', '10.5'), ('11', '11'), ('11.5', '11.5'), ('12', '12'), ('12.5', '12.5'), ('13', '13'), ('13.5', '13.5'), ('14', '14'), ('14.5', '14.5'), ('15', '15'), ('15.5', '15.5'), ('16', '16'), ('16.5', '16.5'), ('17', '17')
    ]
    item_category = models.CharField(choices=ITEM_CATEGORY, blank=True)
    image = models.CharField()
    gender = models.CharField(choices=GENDER, blank=True)
    name = models.CharField()
    price = models.IntegerField()
    tags = models.CharField()
    description = models.CharField()
    clothing_size = models.CharField(choices=CLOTHING_SIZE, blank=True)
    shoe_size = models.CharField(choices=SHOE_SIZE)
