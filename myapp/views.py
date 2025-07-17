from django.shortcuts import render,redirect
from .models import *
from .form import*
from django.shortcuts import render
from .models import Contact


def index(request):
    return render(request,'index.html')

def project(request):    
    return render(request,'project.html')

def skill(request):
    return render(request,'skill.html')

def experience(request):   
    return render(request,'experience.html')

def education(request):   
    return render(request,'education.html')

def about(request):  
    return render(request,'about.html')





def contact_view(request):
    if request.method == 'POST':
        
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')
        category = request.POST.get('category')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        message = request.POST.get('message')

        contact = Contact(
            user_name=user_name,
            user_email=user_email,
            user_phone=user_phone,
            category=category,
            dob=dob,
            age=age,
            gender=gender,
            message=message
        )
        contact.save()
        
        print("Saved:", contact.user_name)

        return render(request, 'contact.html', {'name': user_name})

    return render(request, 'contact.html')
