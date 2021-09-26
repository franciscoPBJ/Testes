from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user_view(request):
    return render(request, 'user_view.html',{})