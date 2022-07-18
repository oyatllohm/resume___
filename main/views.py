from django.shortcuts import render
from django.views import View
from .models import  Partfolyo ,Tehnalogya ,Resume ,Services ,Contact
# Create your views here.

class Home(View):
    def get(self,request):

        partfolyo = Partfolyo.objects.all()

        tehnalogya = Tehnalogya.objects.all()

        resume = Resume.objects.all()

        services = Services.objects.all()
        context ={
            'partfolyo':partfolyo,
            'tehnalogya':tehnalogya,
            'resume':resume,
            'services':services
        }
        return render (request,'index.html',context)

class ContactView(View):
    def get(self,request):
        partfolyo = Partfolyo.objects.all()
        context ={
            'partfolyo':partfolyo,
            }
        return render (request,'contact.html',context)

    def post(self,request):
        partfolyo = Partfolyo.objects.all()
        context ={
            'partfolyo':partfolyo,
            }
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            text=message
        )
        return render (request,'contact.html',context )
