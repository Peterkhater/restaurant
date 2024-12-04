from django.shortcuts import render
from .models import Gallery,DishCategory,Dishes

def main(request):
    gallery = Gallery.objects.all()
    return render(request,'index.html',{'gallery':gallery})

def menu(request):
    categories = DishCategory.objects.prefetch_related('dishes').all()
    return render(request, 'menu.html', {'cat': categories})
