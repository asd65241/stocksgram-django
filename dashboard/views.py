from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'dashboard/index.html')
