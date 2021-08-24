from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.

def root(request):
    return redirect('/course')

def course(request):
    context = {
    'course':Course.objects.all(),
    }
    return render(request,'course_app/course.html',context)

def new_course():
    pass
