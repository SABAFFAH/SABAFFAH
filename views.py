from django import template
from django.db.models.fields.related import ForeignKey
from django.shortcuts import render,HttpResponse
from django.template import loader
from .models import Departments, projects

# Create your views here.
def home(request):
    return render(request, "INDEX.HTML")

def About(request):
    return render(request, "ABOUT.HTML")

def Department(request):
    All_Departments = Departments.objects.all()
    return render(request,'DEPARTMENTS.HTML', {'All_Departments': All_Departments})

def my_project(request):
    all_projects = projects.objects.all()
    return render(request, 'PROJECT.HTML', {'all_projects': all_projects})