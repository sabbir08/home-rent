from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=100, null=True)
  phone = models.CharField(max_length=100, null=True)
  nid = models.CharField(max_length=250, null=True)
  nationality = models.CharField(max_length=100, null=True)
  parmanent_address = models.CharField(max_length=250, null=True)
  dob = models.CharField(max_length=250, null=True)
  bkash_number = models.CharField(max_length=250, null=True)
  trxid = models.CharField(max_length=250, null=True)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  
  
  def __str__(self):
    return self.name