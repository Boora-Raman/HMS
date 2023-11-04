from django.db import models



# Create your models here.
class Rooms_details(models.Model):
    room_type = models.CharField(max_length=35)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    number_of_rooms= models.IntegerField()
    def __str__(self):
        return self.room_type

class Room(models.Model):
    room_number = models.CharField(max_length=255)
    current_status = models.CharField(max_length=255, choices=[
        ('Checked In', 'Checked In'),
        ('Checked Out & Clean', 'Checked Out & Clean'),
        ('Checked Out', 'Checked Out'),
    ])

    def __str__(self):
        return self.room_number


class Booking(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    room_type = models.CharField(max_length=100)
    guest_count = models.IntegerField()
    username = models.CharField(max_length=100)
    coupon = models.CharField(max_length=100,default="Coupon")
    
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

