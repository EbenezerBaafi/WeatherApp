from django.shortcuts import render, httpResponse

# Create your views here.
def home(request):
    return httpResponse("Hello, welcome to The Weather Today!")