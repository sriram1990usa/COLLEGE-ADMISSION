from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def home(request):
    courses=Courses.objects.all()
    context={
        'courses':courses,
        }
    return render(request,'index.html',context)

def createCourse(request):
    if request.user.is_authenticated:
        form=CourseForm()
        if(request.method=='POST'):
            form=CourseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'createCourse.html',context)
    else:
        return redirect('home')

def deleteCourse(request,pk):
    if request.user.is_authenticated:
        course=Courses.objects.get(id=pk)
        if(request.method=='POST'):
            course.delete()
            return redirect('/')
        context={
            'course':course,
            }
        return render(request,'delete.html',context)
    else:
        return redirect('home')

def description(request,pk):
    course=Courses.objects.get(id=pk)
    context={
        'course':course,
        }
    return render(request,'description.html',context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=UserCreationForm()
        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context={
            'form':form
        }
        return render(request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
       context={}
       return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')
