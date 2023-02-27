from django.shortcuts import render
from djangoformjk.forms import StudentForm


def index(request):
    student = StudentForm()
    return render(request, 'index.html', {'form': student})
def car(request):
    cars = CarsForm()
    return render(request,'cars.html', {'form': cars})