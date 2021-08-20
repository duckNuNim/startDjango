from typing import Generic
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from .models import Book,Author, BookInstance, BMI
from django.views import generic
from django import forms
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    
    # return HttpResponse('<h1> My first Http</h1>')
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    context={
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_available' : num_available,
        'num_authors' : num_authors
    }
    return render(request, 'index.html', context= context)


class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

 # ====================================================================== #   

 
def addbmi(request):
	return render(request, 'catalog/bmi.html')

def addConbmi(request):
    myname = request.POST['name']
    myweight = float(request.POST['Myweight'])
    myheight = float(request.POST['Myheight'])
    mybmi = float((myweight/(myheight**2))*(100**2))
    residentBmi = BMI(name = myname, weight = myweight, height = myheight, bmi = mybmi)
    residentBmi.save()
    return HttpResponseRedirect("http://127.0.0.1:8000/catalog/bmis/")


class BmiListView(generic.ListView):
    model = BMI

class BmiDetailView(generic.DetailView):
    model = BMI

