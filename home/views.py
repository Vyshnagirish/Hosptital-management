from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def loginview(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'bookings.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    dep=Department.objects.all()
    return render(request,'department.html',{'dep':dep})

def add_department(request):
    if request.method == "POST":
        frm= DepForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('add_department')
        
        error= "Invalid"   
        return render(request,'add_department.html',{'error':error, 'frm':frm})
    else:
        frm=DepForm()
        return render(request,'add_department.html',{'frm':frm})
    
def add_doctor(request):
    if request.method == "POST":
        frm = DocForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('doctors')
        error = "Data invalid"
        return render(request,'add_doctor.html',{'frm':frm, 'error':error})
    else:
        frm = DocForm()
        return render(request,'add_doctor.html',{'frm':frm})
    
def doctors(request):
    doc=Doctors.objects.all()
    return render(request,'doctors.html',{'doc':doc})

def view_doctor(request,id):
    doc=Doctors.objects.get(id=id)
    return render(request, 'view_doctor.html',{'doc':doc})

def add_booking(request):
    if request.method=="POST":
        book = BookingForm(request.POST)
        if book.is_valid:
            book.save()
            return redirect('bookings')
        error = "Data invalid"
        return render(request,'add_booking.html',{'book':book, 'error':error})
    else:
        book = BookingForm()
        return render(request,'add_booking.html',{'book':book})

def bookings(request):
    book=Booking.objects.all()
    return render(request, 'bookings.html',{'book':book})
