from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(requesst):
   Blogsdata =Blog.objects.all()  
   context={"blogs":Blogsdata}
   return render(requesst, "index.html", context=context)
