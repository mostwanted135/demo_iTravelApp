from django.db import models

# Create your models here.

class HotelDetails:
    hotel_id: str
    hotel_name: str
    hotel_street: str
    hotel_city: str
    hotel_state: str
    hotel_country: str
    hotel_zip: str
    hotel_curr: str
    hotel_amt: float
    hotel_pic: str

class ApiReturnList(models.Model):
    hotel_id = models.CharField(max_length=10)
    hotel_destination_code = models.CharField(max_length=3)
    hotel_name = models.CharField(max_length=100)
    hotel_street = models.CharField(max_length=100)
    hotel_city = models.CharField(max_length=100)
    hotel_state = models.CharField(max_length=100)
    hotel_country = models.CharField(max_length=100)
    hotel_zip = models.CharField(max_length=100)
    hotel_curr = models.CharField(max_length=10)
    hotel_amt = models.FloatField()
    hotel_inserted = models.DateTimeField(auto_now=True)
    hotel_pic = models.CharField(max_length=50)

class PnrConfirmedList(models.Model):
    pnr_id = models.CharField(max_length=10)
    pnr_user_id = models.CharField(max_length=10)
    pnr_hotel_name = models.CharField(max_length=100)
    pnr_destination_code = models.CharField(max_length=3)
    pnr_email_id = models.EmailField(max_length=100)
    pnr_amount = models.FloatField()
    pnr_curr = models.CharField(max_length=3)
    pnr_booked_date = models.DateField()
    pnr_pic = models.CharField(max_length=50)
