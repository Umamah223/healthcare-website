from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=30)
    Phone = models.CharField(max_length=13)
    Email = models.EmailField()
    Subject = models.CharField(max_length=20)
    Message = models.CharField(max_length=60)
    
# Departments Models
class Department(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='departments/')

    def __str__(self):
        return self.name
    
# Model for Doctors
class Doctor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=70)

    def __str__(self):
        return self.name
    
# Newsletter Subscription through Email
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
# Appointment Booking
class Appointment(models.Model):
    Name = models.CharField(max_length=30)
    Number = models.IntegerField()
    form_email = models.EmailField(max_length=70, unique=True)
    form_date = models.DateField()
    choose_schedule = models.CharField(max_length=20, default="9 AM to 10 AM")
    
    def __str__(self):
        return f"{self.Name} {self.form_date} {self.choose_schedule}"
    

    
    
    
    
    


