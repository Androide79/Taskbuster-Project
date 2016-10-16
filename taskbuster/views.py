# -*- coding: utf-8 -*-
from django.shortcuts import render
import datetime
 
def home(request):    
    today = datetime.date.today()
    return render(request, "taskbuster/index.html", {'today': today})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")