from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Profile

# Create your views here.


def index(request):
    
    return render(request,'index.html')


def display_profile(request,username):
    profile = Profile.objects.get(user__username= username)

    user_projects = Projects.objects.filter(author_profile =profile).order_by('created_date')

    context={
        "profile":profile,
        "user_projects":user_projects
    }
    return render(request,'profile_details.html',context)