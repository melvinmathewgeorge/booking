from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=255)
    overview = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    booking_date = models.DateField()
    number_of_people = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
