from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    date=datetime.datetime.now()
    print("test function is called from views")
    #return HttpResponse("<h1> Hello this is index page</h1>"+str(date))
    return render(request,"home.html",{})