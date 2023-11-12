from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact, Subscriber, Appointment
from .forms import SubscribeForm, AppointmentForm


# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

# Home page
def home(request):
    return render(request, "home.html")

# About us page
def about_us(request):
    return render(request, "about_us.html")

# Doctors
def doctors(request):
    return render(request, "doctors.html")

# Appointment Function
def book_appointment(request):
    return render(request, "book_appointment.html") #it returns the corresponding html file

# Contact us page function
def contact_us(request):
    if request.method =="POST" :
        fName = request.POST.get("Name")
        fPhone = request.POST.get("Phone")
        fEmail = request.POST.get("Email")
        fSubject = request.POST.get("Subject")
        fMessage = request.POST.get("Message")
        
    #  To get the data from the website to the admin page, first import the table to the views.py page
    # then use the query = nameOfTheTable followed by the particular name
        query = Contact(Name= fName,Email= fEmail,Phone= fPhone, Subject= fSubject,Message=fMessage) 
        query.save()
        
    # redirect the user to the contact page itself after sending the request about inquiry
    # Sending the email to the user 

    """
        subject = f'Contact Form Submission - {fSubject}'  # Define the subject
        message = f'Name: {fName}\nPhone: {fPhone}\nEmail: {fEmail}\nMessage: {fMessage}'
        from_email = 'umamahali68@gmail.com'  # Admin's email
        recipient_list = ['umamahali68@gmail.com']
    
    # Send email function
        
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )

        return HttpResponseRedirect('/success/')
        """

    return render(request, "contact_us.html")

# Function for the subscribe_to_newsletter footer
def subscribe_to_newsletter(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            Subscriber.objects.create(email=email) #creating and saving a subscriber
            return redirect('doctors')
    
    else:
        form= SubscribeForm()
    return render(request,"book_appointment.html" ,{'form' : form})

# Appointment Form Data
def appointment_data(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('home')
        
    else:
        form = AppointmentForm()
        
    appointments = Appointment.objects.all()
    
    return render(request,"book_appointment.html", {'form':form})
            
    

    



    