from django.db import models
from datetime import datetime
from realtors.models import Realtor # From realtors app

class Listing(models.Model):
  # Don't delete listing if Realtor goes away
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True) # This field is optional but is longer than CharField
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1) # No longer than 2 digits
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/') # Where photo should reference
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Where photo should reference
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Where photo should reference
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Where photo should reference
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Where photo should reference
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Where photo should reference
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Where photo should reference
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self) -> str:
    return self.title