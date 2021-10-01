from django import forms
from django.forms.forms import Form
from django.http.response import HttpResponse
from django.shortcuts import render#, redirect
from django.core.files.storage import FileSystemStorage
"""import numpy as np
import urllib
import json
import cv2
import os"""
#from django.views.decorators.csrf import csrf_exempt
#from django.http import JsonResponse
from django.conf import settings

   

from django.http import HttpResponse

from .models import Coffee
from .forms import CoffeeForm

#def coffee_view(request):
#    return render(request, 'coffee/buy.html', {})

def coffee_view(request):
    if request.method == 'POST':
        form = CoffeeForm(request.POST, request.FILES)
        #result = Coffee.objects.values()
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'coffee/thanks.html', {})

    else:
        form = CoffeeForm()
    return render(request, 'coffee/buy.html',{'form':form})