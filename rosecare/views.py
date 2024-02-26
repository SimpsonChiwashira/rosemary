from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
# views.py


# Create your views here.
def home(request):
    return render(request, "index.html")

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send email (you might need to configure EMAIL_BACKEND and related settings in settings.py)
        #send_mail(
         #   subject,
          #  message,
           # settings.DEFAULT_FROM_EMAIL,
            #[settings.CONTACT_US_EMAIL],  # Add your email address here
            #fail_silently=False,
       # )
        EmailMessage(
               subject,
               message,
               settings.EMAIL_HOST_USER, # Send from (your website)
               [email] # Email from the form to get back to
           ).send()

        return redirect('success_email')
    else:
        return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def success_email(request):
    return render(request, "success_email.html")

def services(request):
    return render(request, "services.html")