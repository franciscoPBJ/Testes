from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.forms import SalesForm
from app.models import Sales

'''def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
def home(request):
    data = {}
    data['var'] = Sales.objects.all()
    return render(request, 'index.html',data)

def form(request):
    data = {}
    data['form'] = SalesForm()
    return render(request, 'form.html',data)

def create(request):
    form = SalesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
# Crud do Projeto
def view(request, pk):
    data = {}
    data['var'] = Sales.objects.get(pk=pk)
    return render(request, 'view.html', data)

# recebe o formulario a ser editado
def edit(request, pk):
    data = {}
    data['var'] = Sales.objects.get(pk=pk)
    data['form'] = SalesForm(instance=data['var'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['var'] = Sales.objects.get(pk=pk)
    form = SalesForm(request.POST or None, instance=data['var'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    var = Sales.objects.get(pk=pk)
    var.delete()
    return redirect('home')
