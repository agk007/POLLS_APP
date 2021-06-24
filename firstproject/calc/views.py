from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about(request):
    return HttpResponse("about page")
def index(request):
    return render(request, 'addpage.html')