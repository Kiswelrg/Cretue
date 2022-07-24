from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from bs4 import BeautifulSoup
from django.utils import timezone
import pytz

# Create your views here.
def Index(request):
    
    return render(request,'tools/ai-animate.html')