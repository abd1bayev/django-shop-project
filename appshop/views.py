from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    
def error(request):
    return render(request, '404.html')

def about(request):
    return render(request, 'about.html')

def address(request):
    return render(request, 'address.html')

def alerts(request):
    return render(request, 'alerts.html')



