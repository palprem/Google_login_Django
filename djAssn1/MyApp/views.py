from django.shortcuts import render
from . models import *
def login(request):
    return render(request, 'block/login.html')

def index(request):
    images = Profile.objects.all()
    print(images)
    return render(request, 'index.html',  {"images":images})

def img(request):
    if request.method =="POST":
        profile = request.POST.get('profile', '')
        student=Profile(profile=profile)
        pro = Dp.objects.all()
        student.save()
        images = Profile.objects.all()

        return render(request, 'index.html',{"images":images})

def dp(request):
    if request.method =="POST":
        dp = request.POST.get('dp', '')
        student=Dp(dp=dp)

        student.save()
        return render(request, 'index.html')





