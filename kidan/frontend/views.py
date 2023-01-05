from django.shortcuts import render


#this function allows as to work with index.html file on the frontend
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')
