from django.shortcuts import render, HttpResponse
from APapp.models import UserAccount, UserMessage
from django.conf import settings  
from django.core.mail import send_mail  
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMessage


# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def message(request):
    return render(request, "message.html")

def speakers(request):
    return render(request, "speakers.html")

def partners(request):
    return render(request, "partners.html")
def compitition(request):
    return render(request, "compitition.html")
def incentive(request):
    return render(request, "incentive.html")
def sector(request):
    return render(request, "sector.html")
def Account(request):
    if request.method == "POST":
        atrack = request.POST.get('track')
        aname = request.POST.get('name') 
        aleader = request.POST.get('leader')   
        aemail = request.POST.get('email')   
        aphone = request.POST.get('phone')  
        areferral = request.POST.get('referral') 
        aCity = request.POST.get('City')  
        astate = request.POST.get('stateName') 
        aprofession = request.POST.get('profession') 
        aorganisation = request.POST.get('organisation') 

        account = UserAccount( track=atrack, name=aname, leader=aleader, email=aemail, phone=aphone, referral=areferral, City=aCity, state=astate, profession=aprofession, organisation=aorganisation)
        account.save()

        sub = "Registration Successful | Action Plan'23 | Abhyuday, IIT Bombay"
        msg = """
        Dear {},\n

Greetings from Abhyuday, IIT Bombay!\n

Congratulations on successfully registering as a team leader for the Action Plan: Asia's fastest-growing social entrepreneurship competition!

To move ahead and make your mark in this competition, you are required to fill in the Team Information and Questionnaire Form, which contains the details of all of your team members, along with a basic questionnaire on your venture/idea. Make sure to fill it in thoughtfully as your answers are your ticket to round 2.\n
Form Link - https://forms.gle/sio9LhCC37wq4QFy8\n
Deadline to fill this form - 28th October 11:59pm\n

To get all the details about the competition, explore our website at www.abhyudayiitb.org/actionplan. All the further updates will be conveyed to you via mail, and do follow us on our Instagram handle @iitbombay_abhyuday to stay connected to us!\n

For any queries, write to us @info.actionplan.iitbombay@gmail.com.\n

So, get ready to dream big and bring your Action Plan to life!\n

Best Regards,\n
Team Action Plan 2023-24\n
Abhyuday, IIT Bombay.""".format(aleader)

        email = EmailMessage(sub, msg, 'info.actionplan.iitbombay@gmail.com', [aemail])
        pdf_path = './static/attachment.pdf'
        email.attach_file(pdf_path)

        # Send the email
        email.send()
        messages.success(request, "You have successfully registered for ActionPlan2023! please check your registered email.")
        return render(request, "register.html")

    print("mail sent")

def Message(request):
    if request.method == "POST":
        aname = request.POST.get('name') 
        aemail = request.POST.get('email')   
        aphone = request.POST.get('phone')  
        amessage = request.POST.get('message') 
        MESSAGE = UserMessage(name=aname, email=aemail, phone=aphone, message=amessage)
        MESSAGE.save()
    
    messages.success(request , "Message has been successfully sent!")
    return render(request , "message.html")

    print("message sent")
