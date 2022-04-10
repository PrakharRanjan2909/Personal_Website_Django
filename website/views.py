from email import message
from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request,'home.html',{})  #empty context-dictionary backend to front end

def contact(request):

    if request.method == "POST":
        your_name =request.POST['your_name']
        your_email = request.POST['your_email']
        your_subject=request.POST['your_subject']
        your_message=request.POST['your_message']

        send_mail(
            your_subject + your_name, #subject
            your_message, #message
            your_email, #from email
            ['rprakhar007@gmail.com'],
            fail_silently=False,



        )
        
        return render(request,'contact.html',{'your_name': your_name})
    else: 
        return render(request,'contact.html',{})

