from django.contrib import admin
from myApp.models import Contact
from myApp.models import Subscriber
from myApp.models import Appointment, Doctor

# Register your models here.
admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(Appointment)
admin.site.register(Doctor)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_filter = ['subscribed_at']
    search_fields = ['email']
    
class AppointmentAdmin(admin.ModelAdmin):
      list_display = ('Name', 'Number', 'form_email', 'form_date', 'choose_schedule')



    
    
    
    
