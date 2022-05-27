import re
from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
    char = list('abcdemghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        char.extend(list('1234567890'))
    if request.GET.get('symbol'):
        char.extend(list('!@#$%^&*()_+-=<>'))

    length=int(request.GET.get('length'))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(char)
    # number = list('1234567890')
    return render(request,'generator/password.html',{'password':thepassword})