from django.shortcuts import render
from .models import Gallery,DishCategory,Dishes,DishCategoryEmporter,DishesAEmporter,MySetting

def main(request):
    gallery = Gallery.objects.all()
    setting = MySetting.objects.get()
    return render(request,'index.html',{'gallery':gallery,'setting':setting})

def menu(request):
    categories = DishCategory.objects.prefetch_related('dishes').all()
    return render(request, 'menu.html', {'cat': categories})


def menuEmporter(request):
    categories = DishCategoryEmporter.objects.prefetch_related('dishes').all()
    return render(request, 'menu_emporte.html', {'cat': categories})
