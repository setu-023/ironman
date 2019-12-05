
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Brands


def brand_index(request):
    obj = Brands.objects.all()
    data = {}
    data['object_list'] = obj
    return render(request, data)

def brand_view(request,id):
    obj = get_object_or_404(Brands, id=id)
    return render(request, {'object':obj})

def brand_create(request):
    html = "homepage.html"
    return render(request,html)

def brand_update(request):
    html = "homepage.html"
    return render(request,html)



def brand_delete(request, id):
    brand= get_object_or_404(Brands, id=id)
    if request.method=='POST':
        brand.delete()
        return redirect('brand_list')






def homepage(request):

    html = "homepage.html"
    return render(request,html)
