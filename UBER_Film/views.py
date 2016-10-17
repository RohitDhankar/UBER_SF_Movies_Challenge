from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def directions(request):
    return render(request, 'directions.html')
