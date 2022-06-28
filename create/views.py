from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages

from .models import contacts
# Create your views here.

def add(request):
    con=contacts.objects.all()
    return render(request,'add.html',{'con':con})

def insert(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phno']
        email=request.POST['email']
        contact=contacts(name=name,phone_number=phone,email=email)
        contact.save()
    messages.add_message(request, messages.INFO, 'contact added successfully')
    return redirect('home')


def delete(request,pk):
    con=contacts.objects.get(id=pk)
    con.delete()
    messages.add_message(request, messages.INFO, 'contact deleted successfully')
    return redirect('home')

def update(request):
    if request.method=="POST":
        id=request.POST['id']
        name = request.POST['name']
        ph = request.POST['pn']
        email = request.POST['em']
        con=contacts.objects.get(id=id)
        con.name=name
        con.phone_number=ph
        con.email=email
        con.save()
        messages.add_message(request, messages.INFO, 'contact updated successfully')
    return redirect('home')