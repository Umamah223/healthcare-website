from django.contrib import admin
from . import views
from django.urls import path
from django.views.generic import TemplateView  # Importing to make a custom landing page

urlpatterns = [
    path('', views.index, name="index"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about_us/', views.about_us, name="about_us"),
    path('doctors/', views.doctors, name="doctors"),
    path('book_appointment/', views.book_appointment, name="book_appointment"),
    path('appointment_data/', views.appointment_data, name='appointment_data'),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('home/', views.home, name="home"),  # Add this line for the "home" view
    path('subscribe_to_newsletter/', views.subscribe_to_newsletter, name="subscribe_to_newsletter"),
]