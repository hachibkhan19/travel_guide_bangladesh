from django.shortcuts import render
from .models import Dhaka, Chittagong, Barishal, Mymensingh, Khulna, Rajshahi, Rangpur, Sylhet
# Create your views here.
def dhaka(request):
    dh = Dhaka.objects.all()
    return render(request, 'dhaka.html', {"dhaka": dh})

def chittagong(request):
    ch = Chittagong.objects.all()
    return render(request, 'chittagong.html', {"chittagong": ch})

def barishal(request):
    bar = Barishal.objects.all()
    return render(request, 'barishal.html', {"barishal": bar})

def mymensingh(request):
    my = Mymensingh.objects.all()
    return render(request, 'mymensingh.html', {"mymensingh": my})

def khulna(request):
    khul = Khulna.objects.all()
    return render(request, 'khulna.html', {"khulna": khul})

def rajshahi(request):
    raj = Rajshahi.objects.all()
    return render(request, 'rajshahi.html', {"rajshahi": raj})

def rangpur(request):
    rang = Rangpur.objects.all()
    return render(request, 'rangpur.html', {"rangpur": rang})

def sylhet(request):
    sylh = Sylhet.objects.all()
    return render(request, 'sylhet.html', {"sylhet": sylh})
