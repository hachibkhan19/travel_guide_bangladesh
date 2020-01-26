from django.urls import path
from .import views

urlpatterns = [
    path('dhaka', views.dhaka, name='dhaka'),
    path('chittagong', views.chittagong, name='chittagong'),
    path('barishal', views.barishal, name='barishal'),
    path('mymensingh', views.mymensingh, name='mymensingh'),
    path('khulna', views.khulna, name='khulna'),
    path('rajshahi', views.rajshahi, name='rajshahi'),
    path('rangpur', views.rangpur, name='rangpur'),
    path('sylhet', views.sylhet, name='sylhet'),
    
]