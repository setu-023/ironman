from django.shortcuts import render

# Create your views here.

def get_all_brands(request):


    obj = brands.objects.all()


























def homepage(request):

    html = "homepage.html"
    return render(request,html)
