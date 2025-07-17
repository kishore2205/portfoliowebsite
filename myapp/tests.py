from django.test import TestCase

from myapp import models

# Create your tests here.
class Visitor(models.Model):
    visitor_id = models.PositiveIntegerField(unique=True)  # Unique ID
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    category = models.CharField(max_length=50)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()
    designated_attendee = models.CharField(max_length=100)
    document = models.FileField(upload_to='visitor_documents/', null=True, blank=True)