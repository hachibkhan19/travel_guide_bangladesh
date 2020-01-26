from django.shortcuts import render
from .models import Flag
# Create your views here.
def index(request):
    bangladesh = Flag.objects.all()
    
    return render(request, 'index.html', {"bangla": bangladesh})
